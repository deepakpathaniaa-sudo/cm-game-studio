#!/usr/bin/env bash
# Build, verify and QA every Sprint 0 artifact. Exit non-zero on any failure.
set -euo pipefail
cd "$(dirname "$0")"
python3 modules/m01/verify.py
python3 modules/m02/verify.py
python3 drills/integer_pv.py | head -1
python3 modules/m01/build_m01.py
python3 modules/m02/build_m02.py
python3 scripts/figure_audit.py "${TMPDIR:-/tmp}/cm_fig_audit"
cd output
Q=../scripts/qa_pdf.py
for f in CM_G7_Math_GaussM02*.pdf; do c=""; [[ $f == *Combined* ]] && c="--combined"
  python3 $Q "$f" --topic "Integers, Place Value and Arithmetic" $c --companion CM_G7_Math_GaussDrillIntegerPlaceValue_v1_2026-09.pdf >/dev/null && echo "QA PASS $f"; done
python3 $Q CM_G7_Math_GaussDrillIntegerPlaceValue_v1_2026-09.pdf --topic "Integer and Place-Value Fluency" \
  --companion CM_G7_Math_GaussM02IntegersSheetStudent_v1_2026-09.pdf CM_G7_Math_GaussM02IntegersHomework_v1_2026-09.pdf >/dev/null && echo "QA PASS drill"
for f in CM_G7_Math_GaussM01*.pdf; do c=""; [[ $f == *Combined* ]] && c="--combined"
  python3 $Q "$f" --topic "Contest Mindset and Diagnostic" $c >/dev/null && echo "QA PASS $f"; done
