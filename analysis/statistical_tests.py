#!/usr/bin/env python3
"""
statistical_tests.py — VERIFIED EDITION (July 2026)
Exact binomial and Monte Carlo permutation tests for the archive's findings.
Inputs below are transcribed directly from data/Master_History_Workbook.xlsx
(Crashes Detail and Assassinations tabs). Standard library only:
    python3 analysis/statistical_tests.py
Deterministic: fixed seed. Rules: pattern never intent; complete counts stated
as counts; counter-examples kept in view; researcher choices shown as switches.
"""
import math, random
SEED = 18650414
MC = 200_000

def binom_ge(n, k, p):
    return sum(math.comb(n,i)*p**i*(1-p)**(n-i) for i in range(k, n+1))

# ---- Verified inputs (Master_History_Workbook.xlsx) ------------------------
# Presidential terms by calendar year, 1907-2025 (annual granularity).
TERMS = [("R",1907,1912),("D",1913,1920),("R",1921,1932),("D",1933,1952),
         ("R",1953,1960),("D",1961,1968),("R",1969,1976),("D",1977,1980),
         ("R",1981,1992),("D",1993,2000),("R",2001,2008),("D",2009,2016),
         ("R",2017,2020),("D",2021,2024),("R",2025,2025)]

# 15 crash events: (id, start_year, start_month, period_end_year, party, severity_class)
# Party attribution rule (pre-committed, METHODOLOGY.md): the president in
# office for the majority of the decline period. Settles C-1980 (3 mo Carter /
# 19 mo Reagan -> R) and C-2000 (decline Mar 2000-Oct 2002, majority Bush -> R).
CRASHES = [
 ("C-1907",1907,10,1907,"R","CrashTerm"),
 ("C-1929",1929,10,1932,"R","CrashTerm"),
 ("C-1937",1937, 5,1938,"D","MidTerm"),
 ("C-1957",1957, 8,1958,"R","MidTerm"),
 ("C-1962",1962, 5,1962,"D","MidTerm"),
 ("C-1970",1970, 1,1970,"R","CrashTerm"),
 ("C-1973-74",1973,1,1974,"R","CrashTerm"),
 ("C-1980",1980,11,1982,"R","MidTerm"),
 ("C-1987",1987,10,1987,"R","CrashTerm"),
 ("C-1990",1990, 7,1990,"R","MidTerm"),
 ("C-2000",2000, 3,2002,"R","CrashTerm"),
 ("C-2007",2007,10,2009,"R","CrashTerm"),
 ("C-2020",2020, 2,2020,"R","CrashTerm"),
 ("C-2022",2022, 1,2022,"D","MidTerm"),
 ("C-2025",2025, 1,2025,"R","CrashTerm"),
]
# 13 documented attempts (Assassinations tab; complete record 1865-2024).
ATTEMPTS = [1865,1881,1901,1912,1933,1950,1963,1974,1975,1975,1981,2024,2024]
SPAN = (1865, 2024)

def party_in(year):
    for p,lo,hi in TERMS:
        if lo <= year <= hi: return p

def f1():
    print("="*70); print("FINDING 1 — Partisan crash asymmetry (verified inputs)"); print("="*70)
    yR = sum(hi-lo+1 for p,lo,hi in TERMS if p=="R"); yD = sum(hi-lo+1 for p,lo,hi in TERMS if p=="D")
    pR = yR/(yR+yD); n=len(CRASHES); k=sum(1 for c in CRASHES if c[4]=="R")
    print(f"Null p(R) = {yR}/{yR+yD} = {pR:.4f} | observed k = {k} of {n} under R")
    print(f"One-sided exact p = {binom_ge(n,k,pR):.4f}")
    for lbl,kk,nn in [("C-1980 counted D",11,15),("C-1980 excluded",11,14)]:
        print(f"  Sensitivity, {lbl}: p = {binom_ge(nn,kk,pR):.4f}")
    for L in (1,2):
        kl = sum(1 for c in CRASHES if party_in(c[1]-L)=="R")
        print(f"  Lag attribution L={L}: k(R)={kl}, p = {binom_ge(n,kl,pR):.4f}")
    ct = [c for c in CRASHES if c[5]=="CrashTerm"]; kct = sum(1 for c in ct if c[4]=="R")
    print(f"Severity split: CrashTerm events = {len(ct)}, all R = {kct==len(ct)}")
    print(f"  P({kct} of {len(ct)} same party) = {binom_ge(len(ct),kct,pR):.5f}")
    print("  NOTE: CrashTerm/MidTerm criteria must be pre-registered and re-derived")
    print("  blind to party before this severity result is claimed as a finding.")

def f2():
    print(); print("="*70); print("FINDING 2 — Attempt clustering (verified inputs)"); print("="*70)
    rng = random.Random(SEED)
    periods = [(c[1], c[3]) for c in CRASHES]
    for w in (1,2):
        wins=[]
        for lo,hi in sorted((a-w,b+w) for a,b in periods):
            if wins and lo<=wins[-1][1]: wins[-1]=(wins[-1][0],max(wins[-1][1],hi))
            else: wins.append((lo,hi))
        inw = lambda y: any(a<=y<=b for a,b in wins)
        cov = sum(1 for y in range(SPAN[0],SPAN[1]+1) if inw(y))/(SPAN[1]-SPAN[0]+1)
        k = sum(1 for y in ATTEMPTS if inw(y)); n=len(ATTEMPTS)
        mc = sum(1 for _ in range(MC) if sum(1 for _ in range(n) if inw(rng.randint(*SPAN)))>=k)/MC
        print(f"±{w}yr around crash periods: coverage {cov:.1%} | in-window {k} of {n} "
              f"| exact p = {binom_ge(n,k,cov):.4f} | MC = {mc:.4f}")
    print("Out-of-window (±2): 1865, 1881, 1901, 1912, 1950 — four of five predate the")
    print("crash table's 1907 start. Pre-1907 extension (blind, NBER dates) in progress;")
    print("no ratio is claimed until it completes. Prior 10-of-13 @22% claim: RETIRED.")
    print("Modern-era count (fact, not ratio): all 7 attempts since 1963 fall in-window.")

def seasonality():
    print(); print("="*70); print("CANDIDATE — Crash start-month seasonality"); print("="*70)
    months = [c[2] for c in CRASHES]; n=len(months)
    from collections import Counter
    cnt = Counter(months)
    print("Start months:", dict(sorted(cnt.items())))
    top2 = cnt.most_common(2); s2 = sum(v for _,v in top2)
    print(f"October = {cnt.get(10,0)}, January = {cnt.get(1,0)} -> top-2 months hold {s2} of {n}")
    rng = random.Random(SEED+7)
    any4=0; two8=0
    for _ in range(MC):
        c = Counter(rng.randint(1,12) for _ in range(n))
        mc2 = c.most_common(2)
        if mc2[0][1] >= max(v for _,v in top2): any4+=1
        if sum(v for _,v in mc2) >= s2: two8+=1
    print(f"MC, post-hoc honest denominators (any month / any month-pair):")
    print(f"  P(some month >= {top2[0][1]})            = {any4/MC:.4f}")
    print(f"  P(some two months together >= {s2}) = {two8/MC:.4f}")
    print("  Caveat: start-month depends on dating convention (peak vs panic month);")
    print("  convention must be fixed blind before this graduates from candidate.")

def term_year_timing():
    print(); print("="*70); print("CANDIDATE — Crash timing across the presidential term"); print("="*70)
    # (crash_year, crash_month, term_start_year, term_start_month) — second terms are new terms
    T=[(1907,10,1905,3),(1929,10,1929,3),(1937,5,1937,1),(1957,8,1957,1),(1962,5,1961,1),
       (1970,1,1969,1),(1973,1,1973,1),(1980,11,1977,1),(1987,10,1985,1),(1990,7,1989,1),
       (2000,3,1997,1),(2007,10,2005,1),(2020,2,2017,1),(2022,1,2021,1),(2025,1,2025,1)]
    from collections import Counter
    yrs=[((cy-ty)*12+(cm-tm))//12+1 for cy,cm,ty,tm in T]
    d=Counter(yrs); dist=[d.get(i,0) for i in (1,2,3,4)]
    print("Term-year distribution y1..y4:", dist, "(uniform expectation 3.75 each)")
    k=max(dist); n=len(yrs)
    print(f"Raw P(X>={k} in a chosen year | n={n}, p=0.25) = {binom_ge(n,k,0.25):.4f}")
    rng=random.Random(11)
    hits=sum(1 for _ in range(MC) if max(Counter(rng.randint(1,4) for _ in range(n)).values())>=k)
    print(f"Post-hoc honest: P(some term-year >= {k}) = {hits/MC:.4f} — uniform; no timing structure.")
    print(f"Election-year (y4) crashes: {d.get(4,0)}/{n} — below uniform expectation.")

if __name__ == "__main__":
    f1(); f2(); seasonality(); term_year_timing()
    print("\nVerified edition, July 2026. Inputs = Master_History_Workbook.xlsx.")
