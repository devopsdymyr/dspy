# Quick Test: Compare Traditional vs DSPy with Your Own Prompts

## 🚀 Quick Start

### Option 1: Interactive Mode (Recommended)
```bash
cd /mnt/sdb1/dspy_test/problem_01_brittle_prompts
source ../../venv/bin/activate

# Set your API key (optional, but recommended)
export OPENAI_API_KEY='your-api-key-here'

# Run the comparison tool
python compare_approaches.py
```

Or use the quick script:
```bash
./test_your_prompt.sh
```

### Option 2: Command Line Mode
```bash
cd /mnt/sdb1/dspy_test/problem_01_brittle_prompts
source ../../venv/bin/activate
export OPENAI_API_KEY='your-api-key-here'

# Test a specific question
python compare_approaches.py "What is machine learning?"
python compare_approaches.py "Explain quantum computing in simple terms"
python compare_approaches.py "How does a neural network work?"
```

## 📊 What You'll See

The comparison tool shows:

1. **Traditional Approach:**
   - The hard-coded prompt that would be used
   - Model-specific code
   - Problems with this approach

2. **DSPy Approach:**
   - The declarative signature
   - Auto-generated prompt (behind the scenes)
   - Actual answer (if API key is set)
   - Benefits of this approach

3. **Side-by-Side Comparison:**
   - Code style comparison
   - Prompt generation comparison
   - Model support comparison
   - Maintainability comparison
   - Optimization comparison

## 🎯 Example Questions to Try

### Technical Questions
- "What is machine learning?"
- "Explain how transformers work in NLP"
- "What's the difference between supervised and unsupervised learning?"

### Simple Questions
- "What is AI?"
- "How does a computer work?"
- "What is Python programming?"

### Complex Questions
- "Explain quantum computing in simple terms"
- "How do neural networks learn?"
- "What is the difference between AI and ML?"

## 💡 What to Observe

### Traditional Approach
Notice:
- ❌ Hard-coded prompt strings
- ❌ Different code for different models
- ❌ Brittle (small changes break it)
- ❌ No way to systematically improve

### DSPy Approach
Notice:
- ✅ Declarative signature (define WHAT, not HOW)
- ✅ Same code works with any model
- ✅ Clean, maintainable code
- ✅ Can be optimized automatically

## 🔍 Understanding the Output

### Without API Key
You'll see:
- Traditional: The prompt that would be used
- DSPy: The code structure (signature)
- Comparison table

### With API Key
You'll see:
- Traditional: The prompt + what would be sent
- DSPy: The actual answer from the model
- Comparison table

## 🧪 Experiment Ideas

1. **Try different question types:**
   - Technical vs Simple
   - Short vs Long
   - Specific vs General

2. **Compare answers:**
   - Are they similar?
   - Which approach is easier to modify?
   - Which is more maintainable?

3. **Modify the signature:**
   - Change the docstring in `compare_approaches.py`
   - See how it affects the answer

## 📝 Notes

- **API Costs**: Real API calls will incur costs
- **Rate Limits**: Be aware of API rate limits
- **Without API Key**: Still useful for seeing the structure
- **Learning**: Focus on understanding the differences

## 🐛 Troubleshooting

### Import Errors
```bash
# Ensure venv is activated
source ../../venv/bin/activate

# Reinstall if needed
pip install -r ../../requirements.txt
```

### API Key Not Working
```bash
# Verify it's set
echo $OPENAI_API_KEY

# Re-export if needed
export OPENAI_API_KEY='your-key-here'
```

### Permission Denied
```bash
chmod +x test_your_prompt.sh
```

---

**Happy Testing!** 🎉

