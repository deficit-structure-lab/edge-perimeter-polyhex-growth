# Ancillary files

Verification scripts for

> *Shortest-side skeletons of edge-perimeter-minimizing polyhexes*

**No proof in the paper depends on any of this output.** The scripts re-derive the
numbers quoted in Section 9 and re-check statements proved analytically in Sections 2–7.

## Environment

Python 3.8 or later. Standard library only: no third-party packages, no input files.
`census.py --n34` takes roughly ten minutes on a single core; everything else runs in
seconds to a few minutes.

## Files

| file | covers |
|---|---|
| `polyhex_core.py` | shared primitives (axial coordinates, perimeter, runs, hulls, support traces). Imported by `census.py` and `checks.py`; not run directly |
| `census.py` | Section 9.1 — the table of \|M_N\|, reachable and unreachable, and the N = 34 cross-check |
| `checks.py` | Section 9.2, rows 1–6 — hull identities, side peelings, capacity and excess, p_min, the residue table and plateau-start counts |
| `skeleton_check.py` | Section 9.2, row 7 — Theorem 6.1, with an implementation independent of `polyhex_core.py` (cube coordinates); also reports the non-shortest peelings |

## Commands and expected output

```
$ python3 census.py
  N   |M_N|  reachable  unreachable
  1       1          1            0
  2       3          3            0
  3       2          2            0
  4       3          3            0
  5       6          6            0
  6      14         14            0
  7       1          1            0
  8       6          6            0
  9      27         27            0
 10       3          3            0
 11      24         24            0
 12       2          2            0
 13      27         18            9
```

```
$ python3 census.py --n34          # additionally, at N = 34:
 34     392        102          290
```

```
$ python3 checks.py
hull identities: 5220 hexagons (L<=16), failures 0
side peelings:   145374 peelings (N<=10), failures 0
capacity/excess: 2177462 polyhexes (N<=11), failures 0
residue table and plateau-start counts, failures: 0
p_min formula failures (N<=3000): 0
```

```
$ python3 skeleton_check.py
shortest-line peelings of minimizers, 3<=N<=34: 2382
  not a minimizer with g down by 1: 0
  restoration order violating exc<=2 / convexity / connectedness: 0
non-shortest peelings: 6498, landing on a minimizer: 3192
residue table sigma<=2999 mismatches: 0
N_b = M(sigma-1)+1 and boundary counts 3m^2+2m+1, 3m^2+4m+2 for m<=59: OK
```

## Status of each item

| label | meaning | items |
|---|---|---|
| `analytic` | proved analytically in the paper; the computation is a re-check | `checks.py`, `skeleton_check.py` |
| `exact` | a finite set is enumerated completely, so the finite statement is settled outright | `census.py` for N ≤ 13 |
| `check` | a census beyond the range needed by the paper | `census.py --n34` |

Two senses of "independent" are kept apart. The *code* in these scripts was written
without following the proofs it re-checks (`skeleton_check.py` even uses a different
coordinate system). The *enumeration of minimizers* is not logically independent of the
paper: `census.py` and `skeleton_check.py` both generate candidate minimizers through
Theorem 4.4(d) (minimizers are directionally convex with λ = g(N)), so every row that
speaks of "all minimizers with N ≤ 34" is a check conditional on that theorem, not a
second proof of it.

## License

The scripts in this directory are released under the MIT License; see `LICENSE` in this
directory (identical to `../LICENSES/MIT.txt`). The paper itself is licensed separately.
