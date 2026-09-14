// ═══════════════════════════════════════════════════════════
// Supabase Edge Function: generate-quiz
// Turns raw PDF text into multiple-choice quiz questions using Claude.
//
// This function is OPTIONAL. The admin page works without it — it falls
// back to an in-browser parser for PDFs that already contain multiple-
// choice questions. Deploy this to also generate questions from plain
// prose (notes, passages, articles).
//
// DEPLOY (one time, from a machine with the Supabase CLI + Docker):
//   supabase functions deploy generate-quiz --project-ref <your-project-ref>
//   supabase secrets set ANTHROPIC_API_KEY=sk-ant-... --project-ref <ref>
//   # optional: supabase secrets set QUIZ_MODEL=claude-sonnet-5 --project-ref <ref>
//
// The client invokes it with the signed-in user's JWT, so only signed-in
// staff can call it in practice (the browser refuses to call it otherwise).
// ═══════════════════════════════════════════════════════════

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};

function json(body: unknown, status = 200): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...CORS, "Content-Type": "application/json" },
  });
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  if (req.method !== "POST") return json({ error: "Use POST" }, 405);

  const apiKey = Deno.env.get("ANTHROPIC_API_KEY");
  if (!apiKey) {
    return json(
      { error: "ANTHROPIC_API_KEY not configured on this function." },
      501,
    );
  }

  let payload: { text?: string; count?: number; grade?: number | null };
  try {
    payload = await req.json();
  } catch {
    return json({ error: "Invalid JSON body." }, 400);
  }

  const text = (payload.text || "").trim();
  if (!text) return json({ error: "No text supplied." }, 400);

  // Guard the model's context / cost: cap the source text.
  const MAX_CHARS = 40000;
  const source = text.length > MAX_CHARS ? text.slice(0, MAX_CHARS) : text;
  const count = Math.min(Math.max(payload.count || 10, 1), 30);
  const grade = payload.grade ?? null;
  const model = Deno.env.get("QUIZ_MODEL") || "claude-opus-5";

  const gradeLine = grade
    ? `The audience is Grade ${grade} students; keep wording age-appropriate.`
    : "";

  const system =
    "You write multiple-choice quiz questions. You always return ONLY a " +
    "single JSON object, no prose, no markdown fences. Every question has " +
    "exactly 4 options and exactly one correct answer.";

  const prompt =
    `From the study material below, create up to ${count} multiple-choice ` +
    `questions. ${gradeLine}\n` +
    `Rules:\n` +
    `- If the material already contains multiple-choice questions, faithfully ` +
    `extract them (question, its 4 options, and the correct one).\n` +
    `- Otherwise, generate new questions that test understanding of the material.\n` +
    `- Each question MUST have exactly 4 distinct options.\n` +
    `- Exactly one option is correct.\n` +
    `- Keep every option plausible; avoid "all of the above".\n\n` +
    `Return JSON in EXACTLY this shape:\n` +
    `{"questions":[{"question":"...","options":["...","...","...","..."],` +
    `"correct_index":0,"explanation":"short reason (optional)"}]}\n\n` +
    `STUDY MATERIAL:\n"""\n${source}\n"""`;

  let apiRes: Response;
  try {
    apiRes = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "x-api-key": apiKey,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
      },
      body: JSON.stringify({
        model,
        max_tokens: 8000,
        system,
        messages: [{ role: "user", content: prompt }],
      }),
    });
  } catch (e) {
    return json({ error: "Failed to reach Anthropic API: " + String(e) }, 502);
  }

  if (!apiRes.ok) {
    const detail = await apiRes.text();
    return json(
      { error: `Anthropic API error ${apiRes.status}`, detail },
      502,
    );
  }

  const data = await apiRes.json();
  // Concatenate all returned text blocks (skip thinking blocks).
  const raw = (data.content || [])
    .filter((b: { type: string }) => b.type === "text")
    .map((b: { text: string }) => b.text)
    .join("\n")
    .trim();

  const parsed = extractJson(raw);
  if (!parsed || !Array.isArray(parsed.questions)) {
    return json(
      { error: "Model did not return usable questions.", raw },
      502,
    );
  }

  // Normalise / validate so the client always gets clean data.
  const questions = parsed.questions
    .map((q: Record<string, unknown>) => {
      const opts = Array.isArray(q.options)
        ? (q.options as unknown[]).map((o) => String(o)).slice(0, 4)
        : [];
      while (opts.length < 4) opts.push("");
      let ci = Number(q.correct_index);
      if (!Number.isInteger(ci) || ci < 0 || ci > 3) ci = 0;
      return {
        question: String(q.question || "").trim(),
        options: opts,
        correct_index: ci,
        explanation: q.explanation ? String(q.explanation) : "",
      };
    })
    .filter(
      (q: { question: string; options: string[] }) =>
        q.question && q.options.every((o) => o.length > 0),
    );

  return json({ questions });
});

// Pull the first balanced {...} JSON object out of arbitrary model text.
function extractJson(s: string): { questions?: unknown[] } | null {
  try {
    return JSON.parse(s);
  } catch {
    /* fall through to brace scan */
  }
  const start = s.indexOf("{");
  if (start === -1) return null;
  let depth = 0;
  for (let i = start; i < s.length; i++) {
    if (s[i] === "{") depth++;
    else if (s[i] === "}") {
      depth--;
      if (depth === 0) {
        try {
          return JSON.parse(s.slice(start, i + 1));
        } catch {
          return null;
        }
      }
    }
  }
  return null;
}
