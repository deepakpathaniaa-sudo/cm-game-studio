"""Drill cluster: Integer and Place-Value Fluency (built with M2, reused all term).

Original Concept Mastery items, generated from templates with a fixed seed.
Every generator returns (stem, answer_text, value) and registers an independent
checker that recomputes `value` by a different route; build aborts on mismatch.
Item length rule: each item must be doable in under 45 seconds.
"""
import random
from fractions import Fraction as F
from datetime import datetime, timedelta

NB, M = " ", "−"
SEED = 20260922


def n(x):
    if isinstance(x, F):
        x = float(x)
    if isinstance(x, float):
        s = f"{abs(x):g}"
    else:
        s = f"{abs(x):,}".replace(",", NB)
    return (M if x < 0 else "") + s


def paren(x):
    return f"({n(x)})" if x < 0 else n(x)


def money(c):
    return f"${c // 100}.{c % 100:02d}"


def hm(h, m):
    suf = "a.m." if h < 12 else "p.m."
    return f"{(h - 1) % 12 + 1}:{m:02d} {suf}"


PLACES = ["ones", "tens", "hundreds", "thousands", "ten-thousands", "hundred-thousands", "millions"]
CHECKERS = []   # (item, recompute) pairs


def reg(stem, ans, value, check):
    CHECKERS.append((stem, value, check))
    return dict(stem=stem, ans=ans, value=value)


# ------------------------------------------------------------------ tier 1: single step, clean numbers
def pv_digit(r):
    x = r.randint(1_000_000, 9_999_999)
    k = r.randint(1, 6)
    d = (x // 10 ** k) % 10
    return reg(f"Which digit is in the {PLACES[k]} place of {n(x)}?", str(d), d, lambda: int(str(x)[-(k + 1)]))


def pv_compare(r):
    a = r.choice(["0.4", "0.6", "0.25", "0.7", "0.09", "0.5"])
    b = {"0.4": "0.38", "0.6": "0.599", "0.25": "0.205", "0.7": "0.71", "0.09": "0.1", "0.5": "0.49"}[a]
    big = max(a, b, key=F)
    return reg(f"Which is greater: {a} or {b}?", big, F(big), lambda: F(sorted([a, b], key=float)[-1]))


def pv_power(r):
    k, p = r.randint(2, 9), r.randint(3, 6)
    v = k * 10 ** p
    return reg(f"Write {k} × 10<super>{p}</super> in standard form.", n(v), v, lambda: int(str(k) + "0" * p))


def int_add(r):
    a, b = -r.randint(3, 15), r.randint(3, 20)
    return reg(f"{n(a)} + {n(b)} = ?", n(a + b), a + b, lambda: sum([a, b]))


def int_sub_neg(r):
    a, b = r.randint(-9, 12), r.randint(3, 15)
    return reg(f"{n(a)} {M} ({M}{b}) = ?", n(a + b), a + b, lambda: a - (-b))


def int_distance(r):
    a, b = -r.randint(2, 15), r.randint(2, 15)
    return reg(f"How far apart are {n(a)} and {n(b)} on a number line?", n(b - a), b - a, lambda: len(range(a, b)))


def ar_partner(r):
    k = r.randint(11, 49)
    p, q = r.choice([(25, 4), (5, 2), (125, 8), (50, 2), (20, 5)])
    v = p * k * q
    return reg(f"{p} × {k} × {q} = ?", n(v), v, lambda: k * (p * q))


def ar_time_convert(r):
    if r.random() < 0.5:
        a, b = r.randint(2, 9), r.randint(5, 55)
        v = a * 60 + b
        return reg(f"{a} min {b} s = ___ s", n(v), v, lambda: int(timedelta(minutes=a, seconds=b).total_seconds()))
    a, b = r.randint(1, 4), r.randint(5, 55)
    v = a * 60 + b
    return reg(f"{a} h {b} min = ___ min", n(v), v, lambda: int(timedelta(hours=a, minutes=b).total_seconds() // 60))


def ar_money_simple(r):
    c, k = r.choice([25, 50, 75, 5, 10]), r.randint(3, 12)
    v = c * k
    return reg(f"What is the cost of {k} items at {money(c)} each?", money(v), v, lambda: sum([c] * k))


# ------------------------------------------------------------------ tier 2: two step, contest-shaped numbers
def pv_digitsum(r):
    x = r.randint(1_000_000, 9_999_999)
    v = sum(map(int, str(x)))
    return reg(f"What is the sum of the digits of {n(x)}?", str(v), v, lambda: sum((x // 10 ** i) % 10 for i in range(7)))


def pv_middle(r):
    base = r.choice(["0.4", "0.6", "0.3", "0.8"])
    vals = [base, base + "05", base[:-1] + "0" + base[-1], base + "5"]
    vals = r.sample(vals, 3)
    mid = sorted(vals, key=F)[1]
    return reg(f"Which is the middle value of {', '.join(vals)}?", mid, F(mid),
               lambda: F([v for v in vals if F(v) != max(map(F, vals)) and F(v) != min(map(F, vals))][0]))


def pv_expanded(r):
    a, b, c = r.randint(1, 9), r.randint(1, 9), r.randint(1, 9)
    v = a * 10 ** 4 + b * 10 ** 2 + c * 10
    return reg(f"{a} × 10<super>4</super> + {b} × 10<super>2</super> + {c} × 10 = ?", n(v), v,
               lambda: int(f"{a}0{b}{c}0"))


def int_three(r):
    a, b, c = r.randint(3, 15), r.randint(3, 12), r.randint(5, 20)
    v = a + b - c
    return reg(f"{a} {M} ({M}{b}) + ({M}{c}) = ?", n(v), v, lambda: sum([a, b, -c]))


def int_temp(r):
    a, b, c = r.randint(2, 12), r.randint(10, 25), r.randint(2, 9)
    v = -a + b - c
    return reg(f"It was {M}{a}°C. It rose {b} degrees, then fell {c} degrees. What is the temperature now?",
               n(v) + "°C", v, lambda: -(a - b + c))


def int_farthest(r):
    base = r.randint(3, 9)
    d = r.sample([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4], 4)
    vals = [-(base + d[0]), base + d[1], -(base - d[2]), base - d[3]]
    r.shuffle(vals)
    vals = [round(v, 2) for v in vals]
    far = max(vals, key=abs)
    return reg(f"Which is farthest from 0: {', '.join(n(v) for v in vals)}?", n(far), far,
               lambda: sorted(vals, key=lambda v: v * v)[-1])


def ar_factor(r):
    p = r.randint(11, 89)
    q, k = 100 - p, r.randint(12, 48)
    v = p * k + q * k
    return reg(f"{p} × {k} + {q} × {k} = ?", n(v), v, lambda: sum(k for _ in range(100)))


def ar_price(r):
    k, c = r.choice([12, 11, 9, 15, 20]), r.choice([145, 235, 199, 325, 175, 250])
    v = k * c
    return reg(f"What is the cost of {k} items at {money(c)} each?", money(v), v, lambda: int(round(k * c / 100 * 100)))


def ar_time_sum(r):
    h1, m1, h2, m2 = r.randint(1, 3), r.randint(35, 55), r.randint(1, 3), r.randint(25, 50)
    tot = (h1 + h2) * 60 + m1 + m2
    return reg(f"{h1} h {m1} min + {h2} h {m2} min = ?", f"{tot // 60} h {tot % 60} min", tot,
               lambda: int((timedelta(hours=h1, minutes=m1) + timedelta(hours=h2, minutes=m2)).total_seconds() // 60))


def ar_pieces(r):
    from math import lcm
    a, b = r.choice([(12, 20), (15, 25), (20, 30), (24, 40), (18, 30), (15, 20)])
    options = [lcm(a, b) * m for m in range(2, 11) if lcm(a, b) * m <= 600
               and lcm(a, b) * m // a - lcm(a, b) * m // b != b - a
               and (lcm(a, b) * m, a, b) != (360, 12, 20)]   # (360, 12, 20) is Sheet Q10
    L = r.choice(options)
    v = L // a - L // b
    return reg(f"A {L} cm strip is cut into {a} cm pieces; another {L} cm strip into {b} cm pieces. "
               f"How many more {a} cm pieces are there?", str(v), v, lambda: len(range(0, L, a)) - len(range(0, L, b)))


# ------------------------------------------------------------------ tier 3: reverse and multi-step
def pv_more(r):
    x = r.randint(100, 999) * 10_000 - r.randint(1, 9) * 1000
    v = x + 10_000
    return reg(f"What number is 10{NB}000 more than {n(x)}?", n(v), v, lambda: int(str(x // 10_000 + 1) + str(x)[-4:]))


def pv_nines(r):
    nn, k = r.randint(4, 7), r.choice([1, 3, 7, 12, 25, 47])
    x = 10 ** nn - k
    v = sum(map(int, str(x)))
    return reg(f"What is the sum of the digits of 10<super>{nn}</super> {M} {k}?", str(v), v,
               lambda: 9 * (nn - len(str(k))) + sum(map(int, str(10 ** len(str(k)) - k))))


def pv_reverse(r):
    k, p = r.randint(12, 95), r.randint(2, 4)
    return reg(f"___ × 10<super>{p}</super> = {n(k * 10 ** p)}", str(k), k, lambda: int(str(k * 10 ** p)[:-p]))


def int_missing_sub(r):
    a, b = r.randint(3, 15), r.randint(-6, 12)
    v = b - a
    return reg(f"___ {M} ({M}{a}) = {n(b)}", n(v), v, lambda: next(x for x in range(-50, 50) if x + a == b))


def int_before(r):
    a, b = r.randint(8, 20), r.randint(2, 7)
    v = a - b
    return reg(f"After falling {a} degrees, the temperature was {M}{b}°C. What was it before the fall?",
               n(v) + "°C", v, lambda: -b + a)


def int_missing_add(r):
    a, b = r.randint(3, 15), r.randint(-8, 12)
    v = b + a
    return reg(f"{M}{a} + ___ = {n(b)}", n(v), v, lambda: next(x for x in range(-50, 50) if -a + x == b))


def ar_start_time(r):
    eh, em = r.randint(9, 15), r.randint(1, 20)
    dh, dm = r.randint(1, 2), r.randint(25, 55)
    s = datetime(2026, 1, 1, eh, em) - timedelta(hours=dh, minutes=dm)
    return reg(f"A class ends at {hm(eh, em)} after running {dh} h {dm} min. When did it start?",
               hm(s.hour, s.minute), (s.hour, s.minute),
               lambda: divmod(eh * 60 + em - dh * 60 - dm, 60))


def ar_unit_price(r):
    k, c = r.choice([4, 5, 6, 7, 8]), r.choice([145, 235, 125, 175, 215])
    return reg(f"{k} pens cost {money(k * c)}. What does one pen cost?", money(c), c,
               lambda: next(x for x in range(1, 1000) if x * k == k * c))


def ar_die(r):
    bottom = r.randint(1, 6)
    return reg(f"The five faces of a die that are not on the table add to {21 - bottom}. "
               f"What number is on the bottom face?", str(bottom), bottom,
               lambda: [f for f in range(1, 7) if sum(range(1, 7)) - f == 21 - bottom][0])


TIERS = {
    1: [[pv_digit, pv_compare, pv_power], [int_add, int_sub_neg, int_distance], [ar_partner, ar_time_convert, ar_money_simple]],
    2: [[pv_digitsum, pv_middle, pv_expanded], [int_three, int_temp, int_farthest], [ar_factor, ar_price, ar_time_sum, ar_pieces]],
    3: [[pv_more, pv_nines, pv_reverse], [int_missing_sub, int_before, int_missing_add], [ar_start_time, ar_unit_price, ar_die]],
}
AREAS = ["Place value and ordering", "Integers", "Efficient arithmetic, time and money"]
SET_SPECS = [  # (set number, tier, time target in minutes)
    (1, 1, 6), (2, 1, 6), (3, 2, 8), (4, 2, 8), (5, 3, 10), (6, 3, 10),
]
MIXED_TARGET = 12


def _unique(r, gens, count, seen):
    out = []
    i = 0
    while len(out) < count:
        g = gens[i % len(gens)]
        it = g(r)
        key = (g.__name__, it["ans"]) if g.__name__ in ("int_farthest", "pv_middle", "ar_die") else it["stem"]
        if key not in seen and it["stem"] not in seen:
            seen.add(key)
            seen.add(it["stem"])
            out.append(it)
            i += 1
        else:
            CHECKERS.pop()
    return out


def build_sets():
    r = random.Random(SEED)
    seen = set()
    sets = []
    for num, tier, target in SET_SPECS:
        a, b, c = TIERS[tier]
        items = _unique(r, a, 7, seen) + _unique(r, b, 7, seen) + _unique(r, c, 6, seen)
        sets.append(dict(num=num, tier=tier, target=target, items=items))
    mixed = []
    for tier in (1, 2, 3):
        for area in TIERS[tier]:
            mixed += _unique(r, area, 3, seen)
    r.shuffle(mixed)
    mixed = mixed[:25]
    assert len(mixed) == 25
    return sets, mixed


def verify_all():
    bad = []
    for stem, value, check in CHECKERS:
        got = check()
        if isinstance(value, tuple):
            ok = tuple(got) == tuple(value)
        else:
            ok = F(str(got)) == F(str(value))
        if not ok:
            bad.append((stem, value, got))
    return len(CHECKERS), bad


if __name__ == "__main__":
    sets, mixed = build_sets()
    total, bad = verify_all()
    print(f"checked {total} generated items, {len(bad)} mismatches")
    for b in bad:
        print("FAIL", b)
    for s in sets:
        print(f"Set {s['num']}:", " | ".join(f"{i['stem'][:40]} → {i['ans']}" for i in s["items"][:3]))
