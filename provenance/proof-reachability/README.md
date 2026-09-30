# Proof-reachability experiment archive

This directory preserves prompts and, when available, run records for the proof-reachability experiments associated with the polyhex growth project.

These materials document research process and reproducibility. They are **not** part of the mathematical proof and are not used as mathematical evidence for the results in the paper.

## Current prompt

- File: `proof-reachable_prompt_v1.0.txt`
- Internal prompt identifier: `B1-v1.1`
- SHA-256: `654ae47632a2af03f72dc45f5d5d157bf79cd23146310ca2a2b816b7d53e16d7`
- Source: prompt supplied by the author and archived verbatim.

The prompt asks an AI system to work on the polyhex growth problem independently, with public web search permitted but direct searching for solutions to Tasks A/B prohibited. It requires a logged exploration process, allows at most 18 rounds, imposes a 20-minute total computation budget, and requires explicit GAP marking and a final self-audit.

Future run transcripts or summaries can be added under this directory without changing the archived prompt.


## AI opinion records on the Note B proof route

The `opinions/` directory preserves two AI-generated responses to the author's question
about why independent AI proof searches did not naturally move toward the one-cell-deletion
route recorded in companion Note B.

These documents are **provenance records only**. They are not mathematical evidence, are not
used in any proof, and should not be read as claims about the intrinsic capabilities or
limitations of language models. They record the models' own contemporaneous interpretations
of the observed proof-search behavior.

- GPT-5.6 Sol
  - `opinions/GPT_Opinion_NoteB_ProofReachability_ja.tex` / `.pdf`: Japanese response
    record, preserving the immediately preceding GPT answer in substance without editorial
    re-analysis.
  - `opinions/GPT_Opinion_NoteB_ProofReachability_en.tex` / `.pdf`: faithful English
    translation of the Japanese GPT response.
- Claude (Anthropic)
  - `opinions/Claude_Opinion_NoteB_ProofReachability_ja.tex` / `.pdf`: Japanese response
    transcribed verbatim as supplied by the author.
  - `opinions/Claude_Opinion_NoteB_ProofReachability_en.tex` / `.pdf`: Claude's English
    rendering supplied with the Japanese record.

The two responses were generated independently and should be compared as model opinions,
not merged into a single retrospective human analysis.
