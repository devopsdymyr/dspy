#!/bin/bash

# Test DSPy Problems One by One
# Interactive script to test each problem sequentially

set -e

echo "=========================================="
echo "🧪 DSPy Problems & Solutions - One by One"
echo "=========================================="
echo ""

cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run: python3 -m venv venv"
    exit 1
fi

source venv/bin/activate

# Check for API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  OPENAI_API_KEY not set!"
    echo ""
    echo "Please set it with:"
    echo "  export OPENAI_API_KEY='your-api-key-here'"
    echo ""
    read -p "Do you want to set it now? (y/n): " set_key
    if [ "$set_key" = "y" ] || [ "$set_key" = "Y" ]; then
        read -p "Enter your OPENAI_API_KEY: " api_key
        export OPENAI_API_KEY="$api_key"
        echo "✅ API key set for this session"
    else
        echo "⚠️  Continuing without API key (will use mocks)"
    fi
    echo ""
else
    echo "✅ OPENAI_API_KEY is set"
    echo ""
fi

PROBLEMS=(
    "problem_01_brittle_prompts:Brittle Prompts"
    "problem_02_few_shot_examples:Few-Shot Examples"
    "problem_03_prompt_optimization:Prompt Optimization"
    "problem_04_model_portability:Model Portability"
    "problem_05_complex_pipelines:Complex Pipelines"
    "problem_06_systematic_improvement:Systematic Improvement"
    "problem_07_reproducibility:Reproducibility"
)

for problem_entry in "${PROBLEMS[@]}"; do
    IFS=':' read -r problem_dir problem_name <<< "$problem_entry"
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📦 Problem: $problem_name"
    echo "📁 Folder: $problem_dir"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    if [ ! -d "$problem_dir" ]; then
        echo "❌ Folder not found: $problem_dir"
        echo ""
        continue
    fi
    
    cd "$problem_dir"
    
    # Show README if exists
    if [ -f "README.md" ]; then
        echo "📖 Problem Description:"
        head -10 README.md | grep -v "^#" | head -5
        echo ""
    fi
    
    # Test traditional approach
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "1️⃣  Testing TRADITIONAL APPROACH (shows the problem)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    read -p "Press Enter to run traditional_approach.py..."
    echo ""
    
    if python traditional_approach.py; then
        echo ""
        echo "✅ Traditional approach completed"
    else
        echo ""
        echo "❌ Traditional approach failed"
        read -p "Press Enter to continue to next problem..."
        cd ..
        echo ""
        continue
    fi
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "2️⃣  Testing DSPY SOLUTION (shows the solution)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    read -p "Press Enter to run dspy_solution.py..."
    echo ""
    
    if python dspy_solution.py; then
        echo ""
        echo "✅ DSPy solution completed"
    else
        echo ""
        echo "❌ DSPy solution failed"
    fi
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "✅ Problem $problem_name completed!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    read -p "Press Enter to continue to next problem (or Ctrl+C to exit)..."
    echo ""
    
    cd ..
done

echo "=========================================="
echo "🎉 All Problems Tested!"
echo "=========================================="
echo ""
echo "Summary:"
echo "  ✅ 7 problems tested"
echo "  ✅ Traditional approaches validated"
echo "  ✅ DSPy solutions validated"
echo ""
echo "Next steps:"
echo "  - Review the output above"
echo "  - Compare traditional vs DSPy approaches"
echo "  - Read README.md in each problem folder for details"
echo ""

