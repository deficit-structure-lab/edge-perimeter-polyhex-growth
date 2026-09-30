# FREEZE RECORD — Shortest-side skeleton theorem

**Date:** 2026-09-27
**Artifact:** `skeleton_note.tex` rev 2 — sha256 見出しの値を参照
**Status:** 独立監査 CONDITIONAL（GAP 0）→ 局所 patch 3 件反映 → **PROVED / FROZEN 候補**（PI 確定待ち）

## 監査鎖
1. GPT-ASTRA clean run が補題 6 として到達（2026-09-27）
2. Claude が現行記号で単独文書化、別実装（cube 座標）で機械検証：最短端列 2,382 / 破れ 0、復元順序 破れ 0
3. 独立監査（GPT）：Q1–Q9 のうち Q5・Q8 が CONDITIONAL、他 PROVED、GAP 0。監査側でも axial 座標の別実装で `3 ≤ N ≤ 10` を再検査、破れ 0
4. patch 3 件反映（本 rev 2）

## 反映した patch
| # | 箇所 | 内容 |
|---|---|---|
| 1 | Step 4 | `σ ≥ 6` の根拠を `g(1), g(2)` から **`g(3) = 6` と単調性**へ。あわせて `σ − 1 ∈ range(g)` を `M(σ−1) − M(σ−2) = m ≥ 1` から明示し、`N_b(σ−1)` の定義域を閉じた |
| 2 | Step 3 "In words" | 三条件が**同時に**成り立つときにのみ厳密不等式が失敗しうる、と読める文に修正（従来文は「`s ∉ {3,5}` なら plateau 先頭」と誤読可能だった） |
| 3 | §1 (P8) の依存 | Lemma 3.4(iv)（hull のセル数）と threshold jump `j(N) ∈ {0,1}` を追加。後者は本文書では `M` の差の正値性で代替済み |

## 使用する既存命題（Option D で移植が要るもの）
(P8) = Prop 11.1 とその証明が依存する Lemma 3.4(iv)、Lemma 11.2、Lemma 11.3、`j(N) ∈ {0,1}`（または `M` の差の正値性）。

## 本文書が確定した場合の帰結
- 現行論文 §5 "peeling a minimizer need not produce a minimizer"、Remark 7.3、序論の `X₃₁` の位置づけは修正必須（内容変更）。
- Option D（一証明稿への再構成）に進める前提が揃う。
