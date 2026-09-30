#!/bin/sh
# 日本語版のビルド。XeLaTeX が必要。
set -e
xelatex -interaction=nonstopmode main_ja.tex
bibtex  main_ja
xelatex -interaction=nonstopmode main_ja.tex
xelatex -interaction=nonstopmode main_ja.tex
echo "done: main_ja.pdf"
