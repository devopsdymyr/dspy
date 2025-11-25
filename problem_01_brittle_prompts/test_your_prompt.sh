#!/bin/bash

# Quick script to test your own prompts

cd "$(dirname "$0")"
source ../../venv/bin/activate

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║     🧪 Test Your Own Prompts - Traditional vs DSPy          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check for API key
if [ -z "$OPENAI_API_KEY" ] && [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  No API key found."
    echo "   Set OPENAI_API_KEY for real answers:"
    echo "   export OPENAI_API_KEY='your-key-here'"
    echo ""
    echo "   (Will show structure comparison without API key)"
    echo ""
fi

echo "🚀 Starting interactive comparison..."
echo ""

python compare_approaches.py

