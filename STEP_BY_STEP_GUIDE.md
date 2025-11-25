# Step-by-Step Testing Guide

## 🎯 Goal
Test each DSPy problem one by one with your OPENAI_API_KEY.

## 📋 Prerequisites

1. **Set your API key:**
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

2. **Activate virtual environment:**
   ```bash
   cd /mnt/sdb1/dspy_test
   source venv/bin/activate
   ```

## 🚀 Method 1: Interactive Script (Recommended)

Run the interactive script that guides you through each problem:

```bash
./test_one_by_one.sh
```

This script will:
- ✅ Check if API key is set
- ✅ Test each problem one by one
- ✅ Wait for your confirmation between problems
- ✅ Show results for each test

## 🚀 Method 2: Manual Testing

Test each problem manually:

### Problem 1: Brittle Prompts
```bash
cd problem_01_brittle_prompts

# See the problem
python traditional_approach.py

# See the solution
python dspy_solution.py

# Optional: Test with framework
python test_with_framework.py

cd ..
```

### Problem 2: Few-Shot Examples
```bash
cd problem_02_few_shot_examples
python traditional_approach.py
python dspy_solution.py
cd ..
```

### Problem 3: Prompt Optimization
```bash
cd problem_03_prompt_optimization
python traditional_approach.py
python dspy_solution.py
cd ..
```

### Problem 4: Model Portability
```bash
cd problem_04_model_portability
python traditional_approach.py
python dspy_solution.py
cd ..
```

### Problem 5: Complex Pipelines
```bash
cd problem_05_complex_pipelines
python traditional_approach.py
python dspy_solution.py
cd ..
```

### Problem 6: Systematic Improvement
```bash
cd problem_06_systematic_improvement
python traditional_approach.py
python dspy_solution.py
cd ..
```

### Problem 7: Reproducibility
```bash
cd problem_07_reproducibility
python traditional_approach.py
python dspy_solution.py
cd ..
```

## 📊 What to Look For

For each problem, observe:

1. **Traditional Approach:**
   - Shows the problem/challenge
   - Manual, brittle code
   - Model-specific implementations

2. **DSPy Solution:**
   - Declarative, clean code
   - Model-agnostic
   - Systematic optimization

3. **Comparison:**
   - How DSPy simplifies the code
   - How DSPy makes it more maintainable
   - How DSPy enables optimization

## 🔍 Detailed Analysis

### Problem 1: Brittle Prompts
- **Traditional**: String manipulation, hard to maintain
- **DSPy**: Declarative signatures, easy to modify
- **Key Learning**: Define WHAT, not HOW

### Problem 2: Few-Shot Examples
- **Traditional**: Manual example selection
- **DSPy**: Automatic optimization finds best examples
- **Key Learning**: Let the framework optimize

### Problem 3: Prompt Optimization
- **Traditional**: Manual iteration, slow
- **DSPy**: Systematic search (MIPRO, COPRO)
- **Key Learning**: Systematic > Manual

### Problem 4: Model Portability
- **Traditional**: Model-specific code
- **DSPy**: Same code, any model
- **Key Learning**: Model-agnostic design

### Problem 5: Complex Pipelines
- **Traditional**: Manual composition
- **DSPy**: Modular, composable building blocks
- **Key Learning**: Composition over construction

### Problem 6: Systematic Improvement
- **Traditional**: Manual A/B testing
- **DSPy**: Automatic optimization with metrics
- **Key Learning**: Metrics-driven improvement

### Problem 7: Reproducibility
- **Traditional**: No versioning
- **DSPy**: Version-controlled modules
- **Key Learning**: Reproducibility matters

## 💡 Tips

1. **Read the README** in each problem folder first
2. **Compare outputs** side by side
3. **Modify examples** to see how DSPy adapts
4. **Take notes** on what you learn
5. **Experiment** with different inputs

## 🐛 Troubleshooting

### API Key Not Working
```bash
# Verify it's set
echo $OPENAI_API_KEY

# Re-export if needed
export OPENAI_API_KEY='your-key-here'
```

### Import Errors
```bash
# Ensure venv is activated
source venv/bin/activate

# Reinstall if needed
pip install -r requirements.txt
```

### Script Permission Denied
```bash
chmod +x test_one_by_one.sh
```

## 📝 Notes

- **API Costs**: Real LLM calls will incur costs
- **Rate Limits**: Be aware of API rate limits
- **Testing**: Start with one problem to verify setup
- **Learning**: Take your time to understand each concept

---

**Happy Testing!** 🎉

