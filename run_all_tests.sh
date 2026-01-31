#!/usr/bin/env bash
for year in */; do
    if [[ $year =~ ^[0-9]{4}/$ ]]; then
        uv run --all-groups pytest "${year%/}" --json-report --json-report-file="results_${year%/}.json"
    fi
done

echo ""
echo "=========================================="
echo "OVERALL SUMMARY"
echo "=========================================="
jq -s '
  (map(.summary) | {
    total: map(.total // 0) | add,
    passed: map(.passed // 0) | add,
    failed: map(.failed // 0) | add,
    skipped: map(.skipped // 0) | add
  }) as $summary |
  (map([.collectors[]? | select(.outcome == "failed")]) | flatten | length) as $collection_errors |
  $summary | .collection_errors = $collection_errors
' results_*.json

rm -f results_*.json
