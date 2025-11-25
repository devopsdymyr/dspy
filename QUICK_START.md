# Quick Start Guide

## ✅ Setup Complete!

Virtual environment created and all dependencies installed.

## 🚀 Run Tests

### Option 1: Test All Problems
```bash
cd /mnt/sdb1/dspy_problems_solutions
source venv/bin/activate
python run_all_tests.py
```

### Option 2: Test Individual Problem
```bash
cd /mnt/sdb1/dspy_problems_solutions
source venv/bin/activate

# Example: Problem 1
cd problem_01_brittle_prompts
python traditional_approach.py  # See the problem
python dspy_solution.py          # See the solution
```

## 📁 Structure

Each problem folder contains:
- `README.md` - Problem explanation
- `traditional_approach.py` - Shows the problem
- `dspy_solution.py` - Shows the solution
- `test_with_framework.py` - Integration example (Problem 1 only)

## 🎯 All 7 Problems

1. **problem_01_brittle_prompts** - Manual prompt engineering
2. **problem_02_few_shot_examples** - Finding good examples
3. **problem_03_prompt_optimization** - Manual optimization
4. **problem_04_model_portability** - Model-specific code
5. **problem_05_complex_pipelines** - Building pipelines
6. **problem_06_systematic_improvement** - Performance improvement
7. **problem_07_reproducibility** - Version control

## 💡 Next Steps

1. **Explore each problem**: Run both traditional and DSPy versions
2. **Set API keys** (optional): For full DSPy execution
   ```bash
   export OPENAI_API_KEY="your-key"
   # or
   export ANTHROPIC_API_KEY="your-key"
   ```
3. **Integrate with your framework**: See `problem_01_brittle_prompts/test_with_framework.py`

## 📊 Test Results

All problems tested successfully! See `TEST_RESULTS.md` for details.

