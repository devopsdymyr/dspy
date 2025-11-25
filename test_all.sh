#!/bin/bash

# Test All DSPy Problems & Solutions
# This script validates each problem one by one

set -e

echo "=========================================="
echo "🧪 DSPy Problems & Solutions - Validation"
echo "=========================================="
echo ""

cd "$(dirname "$0")"
source venv/bin/activate

PROBLEMS=(
    "problem_01_brittle_prompts"
    "problem_02_few_shot_examples"
    "problem_03_prompt_optimization"
    "problem_04_model_portability"
    "problem_05_complex_pipelines"
    "problem_06_systematic_improvement"
    "problem_07_reproducibility"
)

PASSED=0
FAILED=0

for problem in "${PROBLEMS[@]}"; do
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "Testing: $problem"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    cd "$problem"
    
    # Test traditional approach
    echo "📝 Testing traditional approach..."
    if python traditional_approach.py > /dev/null 2>&1; then
        echo "  ✅ Traditional approach: PASSED"
    else
        echo "  ❌ Traditional approach: FAILED"
        ((FAILED++))
        cd ..
        continue
    fi
    
    # Test DSPy solution
    echo "🚀 Testing DSPy solution..."
    if python dspy_solution.py > /dev/null 2>&1; then
        echo "  ✅ DSPy solution: PASSED"
        ((PASSED++))
    else
        echo "  ❌ DSPy solution: FAILED"
        ((FAILED++))
    fi
    
    cd ..
    echo ""
done

echo "=========================================="
echo "📊 Test Summary"
echo "=========================================="
echo "✅ Passed: $PASSED"
echo "❌ Failed: $FAILED"
echo "Total: $((PASSED + FAILED))"
echo ""

if [ $FAILED -eq 0 ]; then
    echo "🎉 All tests passed!"
    exit 0
else
    echo "⚠️  Some tests failed. Check output above."
    exit 1
fi

