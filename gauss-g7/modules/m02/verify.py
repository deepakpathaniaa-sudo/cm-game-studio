"""Independent second-method verification for every M2 sheet and homework item.
Each check recomputes the answer by a route different from the written solution
(brute force, string manipulation, datetime, Fraction) and confirms that exactly
one of the five options equals it."""
import sys, os
from fractions import Fraction as F
from datetime import datetime, timedelta
sys.path.insert(0, os.path.dirname(__file__))
from content import SHEET, HOMEWORK, WE1, WE2

def num(s):
    s = s.replace("−", "-").replace(" ", "").replace("$", "").replace("°C", "")
    if ":" in s:
        h, m = s.split()[0].split(":"); pm = "p.m." in s
        return (int(h) + (12 if pm and int(h) != 12 else 0), int(m))
    return F(s)

def t(h, m): return datetime(2026, 1, 1, h, m)

checks = {
 # sheet (1-based numbering on the sheet)
 1: int(str(7350912)[-5]),
 2: max([-8.2, 7.9, -0.85, 8.1, -8.02], key=abs),
 3: len(range(-11, 6)),                                  # unit steps from -11 to 6
 4: divmod(sum(x * 60 + y for x, y in [(3, 48), (4, 25)]), 60),
 5: 125 * 13 * 8,
 6: sum([19 * 46, 81 * 46]),
 7: F(sorted(["0.305", "0.35", "0.3", "0.053", "0.53"], key=F)[2]),
 8: sum(map(int, "4070809")),
 9: F(235 * 12, 100),
 10: len(range(0, 360, 12)) - len(range(0, 360, 20)),
 11: int("4" + "0" + "3" + "5" + "0"),
 12: 12 - (-7) + (-15),
 13: 21 - 17,
 14: ((t(19, 48) + timedelta(hours=2, minutes=37)).hour, (t(19, 48) + timedelta(hours=2, minutes=37)).minute),
 15: sum(map(int, str(10**30 - 47))),
 16: len(str(5**20 * 2**18)),
 17: 250 * 17 * 4,
 18: 999 + 998 + 1002 + 1001,
}
hw = {
 1: 10 * 5 + 5 * 6,
 2: sum(range(1, 40, 2)),
 3: next(x for x in range(-100, 100) if 4 * x - 9 == 55),
 4: min(["0.7", "0.07", "0.707", "0.077", "0.0707"], key=F),
 5: 480 // 30 - 480 // 40,
 6: F(175 * -(-int((t(11, 20) - t(9, 52)).total_seconds() // 60) // 15), 100),
 7: -6 - 9 + 23,
 8: ((t(8, 17) - timedelta(minutes=18 + 25 + 12 + 4)).hour, (t(8, 17) - timedelta(minutes=18 + 25 + 12 + 4)).minute),
 9: [s for s in [52, 63, 74, 81, 95] if any(sum(range(k, k + 5)) == s for k in range(0, 100))],
 10: sum(map(int, str(7 * int("9" * 50)))),
}
hw[4] = F(hw[4])
hw[9] = hw[9][0] if len(hw[9]) == 1 else None
fails = 0
def check(label, item, val):
    global fails
    av = item["ans_val"]
    ok = (tuple(av) == tuple(val)) if isinstance(av, tuple) else F(str(av)) == F(str(val))
    if item.get("opts"):
        hits = []
        for L, o in zip("ABCDE", item["opts"]):
            ov = num(o)
            if (isinstance(ov, tuple) and ov == tuple(val)) or (not isinstance(ov, tuple) and not isinstance(val, tuple) and ov == F(str(val))):
                hits.append(L)
        ok = ok and hits == [item["key"]]
        extra = f"options matching={hits} key={item['key']}"
    else:
        extra = f"key={item['key']}"
    print(f"{'PASS' if ok else 'FAIL'}  {label:8s} recomputed={val}  {extra}")
    fails += not ok

for i, it in enumerate(SHEET, 1): check(f"Sheet{i}", it, checks[i])
for i, it in enumerate(HOMEWORK, 1): check(f"HW{i}", it, hw[i])
# worked examples
assert 36 * 7 + 64 * 7 == WE1["answer"]; assert sum(range(2, 51, 2)) - sum(range(1, 50, 2)) == WE2["answer"]
# extension answers used in solutions
assert min(k for k in range(1, 26) if max(sum(sorted([5]*10 + [6]*10 + [8]*5)[-k:]) for _ in [0]) >= 100) == 15
assert sum(range(1, 100, 2)) == 2500 and sum(map(int, str(13 * int("9" * 50)))) == 450
assert str(13 * 9999) == "129987" and [s for s in [52,63,74,81,95] if (s-6) % 4 == 0] == [74]
print("Worked examples + extension answers: PASS")
sys.exit(1 if fails else 0)
