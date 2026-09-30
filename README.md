# Shortest-side skeletons of edge-perimeter-minimizing polyhexes

H. Utsunomiya — English paper (canonical), Japanese edition, companion notes, verification
scripts, and provenance records.

**Canonical version:** `paper/en/main.tex` (23 pages). arXiv: `<to be filled in after submission>`.

## Result

A polyhex is a finite connected set of cells of the hexagonal tiling; its edge perimeter is
the number of unit edges separating it from its complement. The paper proves:

> Deleting any shortest extreme line from an edge-perimeter minimizer with at least three
> cells leaves a minimizer whose threshold has dropped by exactly one, and the deleted line
> can be restored one cell at a time with edge-perimeter excess at most two.

Hence every minimizer lies on a chain of minimizers linked by such deletions, and every
minimizer can be grown from a single cell one adjacent cell at a time with excess never
above two. The constant two cannot be lowered.

## Layout

```
paper/en/       main.tex, main.bbl, refs.bib, main.pdf        — canonical English paper
paper/ja/       main_ja.tex, main_ja.bbl, fig1_body.tex, …    — Japanese edition
notes/          note_A  Growth chains for near-extremal directionally convex polyhexes
                note_B  A one-cell deletion proof for bounded-excess growth of minimizing polyhexes
                note_C  Extreme endpoints of low-excess polyhexes are never articulation cells
anc/            verification scripts (Python 3.8+, standard library only) — see anc/README.md
provenance/     research-history records, proof-reachability materials, and the audited standalone note behind Section 6
```

The three notes are self-contained (each reproduces the common framework of the paper).
They record, respectively, the wider-class extension mentioned in Remark 8.2, the one-cell
proof mentioned in Remark 8.3, and a structural theorem on extreme-line endpoints. They are
not part of the arXiv submission.

## Correspondence between the two editions

The English and Japanese editions both incorporate the pre-submission review corrections
of 2026-09-28 and have matching mathematical content, labels, and cited sources. The English
edition is the canonical arXiv text; the Japanese edition is provided as a synchronized
translation.

## Building

English: `pdflatex main.tex; bibtex main; pdflatex main.tex; pdflatex main.tex` (a
pre-generated `main.bbl` is included). Japanese: `cd paper/ja && ./build.sh` (XeLaTeX with
Noto Serif CJK JP / Noto Sans CJK JP). Notes: in `notes/`, for each `X` in `A B C`:
`pdflatex note_X.tex; bibtex note_X; pdflatex note_X.tex; pdflatex note_X.tex`
(`refs.bib` is shared and pre-generated `note_X.bbl` files are included, so the notes also
build without BibTeX).

## Licenses

- Paper texts (English and Japanese), notes, provenance documents, and figures: **CC BY 4.0** — `LICENSES/CC-BY-4.0.txt`.
- Code and scripts, including `anc/`, build scripts, and GitHub Actions workflows: **MIT** — `LICENSES/MIT.txt`.

The full license texts are kept in the top-level `LICENSES/` directory.

## AI-assisted tools

AI-assisted tools were used during the research and preparation of this work. See the
statement at the end of the paper.

