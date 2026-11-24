#!/usr/bin/env bash
set -euo pipefail

usage() {
    cat <<EOF
Usage: $0 [-x]

Run pytest for all year directories (matching yearYYYY/ pattern).

Options:
    -x    Stop at first test failure (passes -x to pytest and exits script)

Examples:
    $0        Run all tests, continue on failures
    $0 -x     Stop at first failure
EOF
    exit 1
}

exit_first=false

while getopts "xh" opt; do
    case $opt in
        x) exit_first=true ;;
        h) usage ;;
        *) usage ;;
    esac
done

for year in */; do
    if [[ $year =~ ^year[0-9]{4}/$ ]]; then
        year_num="${year#year}"
        year_num="${year_num%/}"
        pytest_args=(--json-report --json-report-file="results_${year_num}.json")
        [[ $exit_first == true ]] && pytest_args+=(-x)

        if ! uv run --all-groups pytest "${year%/}" "${pytest_args[@]}"; then
            if [[ $exit_first == true ]]; then
                total=$(jq -r '.summary.total // 0' "results_${year_num}.json")
                [[ $total -gt 0 ]] && exit 1
            fi
        fi
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
