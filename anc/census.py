"""Section 9.1: the census of edge-perimeter minimizers and their reachability.

Reproduces the table for N <= 13 and, with --n34, the N = 34 cross-check.
Minimizers are enumerated through their tight hulls, using Theorem 4.4(d).
"""
import sys
from itertools import combinations
from polyhex_core import (M, g, hexagon, admissible, connected, p, norm)


def minimizers(N, slack=4):
    """All N-cell edge-perimeter minimizers, normalized up to translation."""
    ga = g(N)
    out = set()
    for L in range(1, ga + 2):
        for u in range(L):
            for v in range(L):
                for w in range(L):
                    if not admissible(L, u, v, w):
                        continue
                    if 3 * L - (u + v + w) != ga:
                        continue
                    H = hexagon(L, u, v, w)
                    d = len(H) - N
                    if d < 0 or d > slack:
                        continue
                    for rem in combinations(H, d):
                        S = set(H) - set(rem)
                        if len(S) == N and connected(S) and p(S) == 2 * ga:
                            out.add(norm(S))
    return out


def run(nmax):
    Mn = {N: minimizers(N) for N in range(1, nmax + 1)}
    reach = {1: set(Mn[1])}
    for N in range(2, nmax + 1):
        reach[N] = {S for S in Mn[N]
                    if any(norm(set(S) - {c}) in reach[N - 1]
                           for c in set(S) if connected(set(S) - {c}))}
    print(f"{'N':>3} {'|M_N|':>7} {'reachable':>10} {'unreachable':>12}")
    for N in range(1, nmax + 1):
        a, b = len(Mn[N]), len(reach[N])
        print(f"{N:>3} {a:>7} {b:>10} {a-b:>12}")
    return Mn, reach


if __name__ == '__main__':
    nmax = 34 if '--n34' in sys.argv else 13
    run(nmax)
