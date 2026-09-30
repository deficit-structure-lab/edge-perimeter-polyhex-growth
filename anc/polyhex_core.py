"""Shared primitives for the ancillary verification scripts.

Axial coordinates (q, r); third key s = q + r.  Standard library only.
"""
import math

DIRS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]


def nbrs(c):
    q, r = c
    return [(q + dq, r + dr) for dq, dr in DIRS]


def p(S):
    S = set(S)
    return sum(1 for c in S for n in nbrs(c) if n not in S)


def lines(S):
    return ({('q', q) for q, r in S} | {('r', r) for q, r in S}
            | {('s', q + r) for q, r in S})


def trace(S, t, k):
    if t == 'q':
        return sorted(r for q, r in S if q == k)
    if t == 'r':
        return sorted(q for q, r in S if r == k)
    return sorted(q for q, r in S if q + r == k)


def runs(S):
    R = 0
    for t, k in lines(S):
        cs = trace(S, t, k)
        R += 1 + sum(1 for i in range(len(cs) - 1) if cs[i + 1] - cs[i] > 1)
    return R


def connected(S):
    S = set(S)
    if not S:
        return False
    st = [next(iter(S))]
    seen = set(st)
    while st:
        c = st.pop()
        for n in nbrs(c):
            if n in S and n not in seen:
                seen.add(n)
                st.append(n)
    return len(seen) == len(S)


def dir_convex(S):
    return runs(S) == len(lines(S))


def norm(S):
    a = min(q for q, r in S)
    b = min(r for q, r in S)
    return tuple(sorted((q - a, r - b) for q, r in S))


def g(N):
    return math.isqrt(12 * N - 4) + 1 if not _is_sq(12 * N - 3) else math.isqrt(12 * N - 3)


def _is_sq(x):
    r = math.isqrt(x)
    return r * r == x


def M(t):
    return (t * t + 3) // 12 if t >= 0 else 0


def hexagon(L, u, v, w):
    A, B = L - u, L - v
    return [(q, r) for q in range(A) for r in range(B) if w <= q + r <= L - 1]


def admissible(L, u, v, w):
    return (L >= 1 and min(u, v, w) >= 0
            and u + v <= L - 1 and v + w <= L - 1 and u + w <= L - 1)


def hull_params(S):
    A = 1 + max(q for q, r in S)
    B = 1 + max(r for q, r in S)
    L = 1 + max(q + r for q, r in S)
    w = min(q + r for q, r in S)
    return L, L - A, L - B, w


def side_sets(S, L, u, v, w):
    """The six support traces, in the cyclic order of the paper."""
    A, B = L - u, L - v
    return [[c for c in S if c[0] == 0],
            [c for c in S if c[1] == B - 1],
            [c for c in S if c[0] + c[1] == L - 1],
            [c for c in S if c[0] == A - 1],
            [c for c in S if c[1] == 0],
            [c for c in S if c[0] + c[1] == w]]


def rho(S):
    return min(len(x) for x in side_sets(S, *hull_params(S)))


def grow(cells, keep=None):
    """All one-cell extensions, normalized; keep is an optional filter."""
    out = set()
    for S in cells:
        Ss = set(S)
        for c in Ss:
            for n in nbrs(c):
                if n not in Ss:
                    T = Ss | {n}
                    if keep is None or keep(T):
                        out.add(norm(T))
    return out
