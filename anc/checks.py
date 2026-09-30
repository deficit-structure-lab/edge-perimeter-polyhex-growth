"""Section 9.2: the consistency checks.

Each block re-checks a statement of the paper with an implementation independent of
its proof.  No proof in the paper depends on any of this.
"""
import math
from itertools import combinations
from polyhex_core import *


def hull_identities(Lmax=16):
    n = bad = 0
    T = lambda k: k * (k + 1) // 2
    for L in range(1, Lmax + 1):
        for u in range(L):
            for v in range(L):
                for w in range(L):
                    if not admissible(L, u, v, w):
                        continue
                    n += 1
                    H = hexagon(L, u, v, w)
                    lam = len(lines(H))
                    l = [L-v-w, v+1, L-u-v, u+1, L-u-w, w+1]
                    sd = side_sets(H, L, u, v, w)
                    d = L - u - v - w - 1
                    Q = (l[0]-l[2])**2 + (l[2]-l[4])**2 + (l[4]-l[0])**2
                    ok = ([len(x) for x in sd] == l
                          and lam == 3*L - (u+v+w) == p(H)//2
                          and sum(l) == lam + 3
                          and l[0]-l[3] == l[2]-l[5] == l[4]-l[1] == d
                          and len(H) == T(L)-T(u)-T(v)-T(w)
                          and lam*lam + 3 - 12*len(H) == 3*d*d + 2*Q
                          and connected(H) and dir_convex(H))
                    bad += 0 if ok else 1
    return n, bad


def peelings(nmax=10):
    cur = {norm([(0, 0)])}
    n = bad = 0
    for k in range(2, nmax + 1):
        cur = grow(cur, keep=dir_convex)
    seen = {norm([(0, 0)])}
    cur = {norm([(0, 0)])}
    allc = [set(cur)]
    for k in range(2, nmax + 1):
        cur = grow(cur, keep=dir_convex)
        allc.append(set(cur))
    for fam in allc:
        for S in fam:
            S = set(S)
            L, u, v, w = hull_params(S)
            for R in side_sets(S, L, u, v, w):
                Sp = S - set(R)
                if not Sp:
                    continue
                n += 1
                if not (connected(Sp) and dir_convex(Sp)
                        and p(Sp)//2 <= p(S)//2 - 1):
                    bad += 1
    return n, bad


def capacity(nmax=11):
    cur = {norm([(0, 0)])}
    n = bad = 0
    for k in range(2, nmax + 1):
        cur = grow(cur)
        for S in cur:
            S = set(S)
            n += 1
            sg = p(S)//2
            lam = len(lines(S))
            ok = (len(S) <= M(sg) and lam >= g(len(S))
                  and (p(S) - 2*g(len(S)) <= 2) == (len(S) > M(sg - 2)))
            if dir_convex(S):
                ok = ok and (p(S) - 2*g(len(S))) == 2*(lam - g(len(S)))
            if p(S) == 2*g(len(S)):
                ok = ok and dir_convex(S) and sg == g(len(S))
            bad += 0 if ok else 1
    return n, bad


def residue_table(smax=2999):
    """Section 6, Step 2: M(s-1)-M(s-2) and floor((s+3)/6) by residue s mod 6, and the
    two plateau-start counts of Section 5."""
    bad = 0
    for sg in range(6, smax + 1):
        m, s = divmod(sg, 6)
        d = M(sg - 1) - M(sg - 2)
        L = (sg + 3)//6
        if d != (m + 1 if s == 4 else m) or L != (m if s <= 2 else m + 1):
            bad += 1
    Nb = lambda ga: M(ga - 1) + 1
    for m in range(1, 60):
        if Nb(6*m+3) != 3*m*m + 2*m + 1 or Nb(6*m+5) != 3*m*m + 4*m + 2:
            bad += 1
    return bad


def pmin_formula(nmax=3000):
    return sum(1 for N in range(1, nmax + 1)
               if 2*min(t for t in range(3, 400) if M(t) >= N) != 2*g(N))


if __name__ == '__main__':
    n, b = hull_identities();  print(f"hull identities: {n} hexagons (L<=16), failures {b}")
    n, b = peelings();         print(f"side peelings:   {n} peelings (N<=10), failures {b}")
    n, b = capacity();         print(f"capacity/excess: {n} polyhexes (N<=11), failures {b}")
    print(f"residue table and plateau-start counts, failures: {residue_table()}")
    print(f"p_min formula failures (N<=3000): {pmin_formula()}")
