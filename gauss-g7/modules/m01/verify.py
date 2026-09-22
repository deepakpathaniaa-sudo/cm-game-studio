"""Independent second-method verification for M1 diagnostic Form A and the core-move examples."""
import sys, os, itertools
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(__file__))
from content import DIAG, TIERS

def opt_val(o):
    o = o.replace("<super>", "").replace("</super>", "").replace("<sub>", "").replace("</sub>", "")
    o = o.replace("$", "").replace(" cm", "").replace("°", "")
    try: return F(o)
    except ValueError: return o

solve = {
 1: F(36) * F(3, 4),
 2: sum(F(80, 100) for _ in range(15)),                       # 1% repeated 15 times
 3: next(n for n in range(100) if 4 * n + 7 == 43),
 4: list(itertools.islice(itertools.count(5, 7), 10))[-1],
 5: len([1 for _ in range(12)]) * 2 + 7 * 2,
 6: 180 - 48 - 67,
 7: F(sum([8, 11, 12, 15, 24]), 5),
 8: [p for p in [59, 39, 51, 57, 91] if all(p % d for d in range(2, p))][0],
 9: min(m for m in range(1, 100) if m % 6 == 0 and m % 8 == 0),
 10: [perm for perm in itertools.permutations(["cat", "dog", "fish"])       # (Ana, Ben, Cy)
      if perm[1] != "dog" and perm[2] == "cat"],
 11: F(80) * F(75, 100) * F(113, 100),
 12: (lambda k: 5 * k - 3 * k)(next(k for k in range(1, 48) if 8 * k == 48)),
 13: 1 - F(1, 3) - F(1, 4) * (1 - F(1, 3)),
 14: 4 + 3 * 19,
 15: sum(1 for x in range(10) for y in range(8) if not (x >= 6 and y >= 5)),   # unit squares
 16: next(x for x in range(1, 180) if x + 2 * x + 54 == 180),
 17: F(360, 8 * 9),
 18: next(g for g in range(0, 100) if F(5, 9 + g) == F(1, 3)),
 19: sum(1 for i in range(1, 101) if i % 3 == 0 or i % 5 == 0),
 20: [o for o in itertools.permutations("ABCD") if o.index("A") < o.index("B") < o.index("D")
      and o.index("C") == o.index("D") + 1],
 21: next(2 * (4 * k) for k in range(1, 50) if 3 * k + 6 == 4 * k),
 22: next(m + 4 for m in range(0, 200, 2) if 5 * m == 170),
 23: sum(1 for x, y, z in itertools.product(range(4), repeat=3)
         if sum(c in (0, 3) for c in (x, y, z)) == 2),
 24: F(sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == 8), 36),
 25: sum(1 for n in range(100, 1000) if sum(map(int, str(n))) == 5),
}
assert len(solve[10]) == 1 and solve[10][0][1] == "fish"; solve[10] = "Ben"
assert len(solve[20]) == 1; solve[20] = "Dee" if solve[20][0][2] == "D" else "?"
fails = 0
for i, it in enumerate(DIAG, 1):
    val = solve[i]
    kv = it["v"]
    ok = (F(str(kv)) == F(str(val))) if not isinstance(kv, str) or kv.replace(".", "").replace("/", "").isdigit() else kv == val
    extra = ""
    if "opts" in it:
        hits = [L for L, o in zip("ABCDE", it["opts"]) if (opt_val(o) == (F(str(val)) if not isinstance(val, str) else val))]
        ok = ok and hits == [it["key"]]
        extra = f"matching options={hits} key={it['key']}"
    else:
        ok = ok and F(it["key"]) == F(str(val))
        extra = f"written key={it['key']}"
    print(f"{'PASS' if ok else 'FAIL'}  Q{i:<3} recomputed={val}  {extra}")
    fails += not ok
# blueprint + scoring
from collections import Counter
cnt = Counter(it["s"] for it in DIAG)
assert cnt == Counter({"N": 6, "A": 4, "G": 6, "D": 3, "T": 4, "L": 2}), cnt
assert sum((b - a + 1) * p for _, a, b, p in TIERS) == 100
# core-move examples
x = next(x for x in range(1, 12) if x + 2 * x + 2 * x + 2 == 12); assert 2 * x + 2 == 6
assert sum(1 for d in range(4) for n in range(7) if 10 * d + 5 * n == 30) == 4
assert len(list(itertools.combinations(range(10), 2))) == 45
assert (6 + 4) * 2 == 20 and 20 / 2 - 4 == 6
assert [p for p in [41, 55, 72, 89, 91] if any(k * (k + 1) == p for k in range(20))] == [72]
assert 19 * 21 == 399
print("Blueprint 6/4/6/3/4/2 and 20/50/30 scoring: PASS; core-move examples: PASS")
sys.exit(1 if fails else 0)
