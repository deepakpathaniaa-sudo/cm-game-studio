#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
# One-shot Vercel deploy for the Teacher Availability app.
# Run it from your OWN machine (it needs your Vercel login):
#
#   cd teacher-availability
#   ./deploy.sh
#
# Prereqs: Node.js + npm installed, and a Vercel account.
# Running from THIS folder makes it the Vercel project root, so no
# "Root Directory" setting is needed.
# ─────────────────────────────────────────────────────────────
set -euo pipefail
cd "$(dirname "$0")"

SUPABASE_URL_VALUE="https://cqzpzhdleqyrmedymypg.supabase.co"

# Use a locally-installed vercel if present, else npx (no global install needed).
if command -v vercel >/dev/null 2>&1; then VERCEL="vercel"; else VERCEL="npx --yes vercel@latest"; fi

echo "▶ 1/5  Logging in to Vercel (opens a browser if you're not already logged in)…"
$VERCEL login

echo "▶ 2/5  Linking this folder to a Vercel project…"
$VERCEL link

# Helper: set an env var for both Production and Preview, ignoring "already exists".
set_env () {
  local key="$1" value="$2"
  for target in production preview; do
    printf '%s' "$value" | $VERCEL env add "$key" "$target" >/dev/null 2>&1 \
      && echo "   • set $key ($target)" \
      || echo "   • $key ($target) already set — leaving as is (change it in the dashboard if needed)"
  done
}

echo "▶ 3/5  Setting SUPABASE_URL…"
set_env "SUPABASE_URL" "$SUPABASE_URL_VALUE"

echo "▶ 4/5  Setting SUPABASE_SECRET_KEY (service_role / secret key)…"
echo "   Get it from: Supabase → project 'cm-whiteboard' → Settings → API → service_role secret."
read -rsp "   Paste SUPABASE_SECRET_KEY (input hidden): " SECRET; echo
if [ -z "${SECRET:-}" ]; then
  echo "   ! No key entered — skipping. The app will run on the file backend and NOT persist."
else
  set_env "SUPABASE_SECRET_KEY" "$SECRET"
fi

echo "▶ 5/5  Deploying to production…"
$VERCEL --prod

echo
echo "✅ Done. Open  https://<your-domain>/healthz  — it should say {\"ok\":true,\"backend\":\"supabase\"}."
echo "   If it says \"backend\":\"file\", the env vars didn't load — re-run and paste the secret key."
