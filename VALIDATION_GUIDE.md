# Validation Guide - Testing Each Functionality

## ✅ Setup Complete

Repository cloned and environment ready at: `/mnt/sdb1/dspy_test`

## 🧪 Testing Each Problem

### Prerequisites
```bash
cd /mnt/sdb1/dspy_test
source venv/bin/activate
```

### Problem 1: Brittle Prompts
**What to test:** Manual prompt engineering vs declarative signatures

```bash
cd problem_01_brittle_prompts

# See the problem (traditional approach)
python traditional_approach.py

# See the solution (DSPy)
python dspy_solution.py

# Test with framework integration
python test_with_framework.py
```

**Expected:** DSPy solution should show structured, maintainable code vs brittle string manipulation.

---

### Problem 2: Few-Shot Examples
**What to test:** Manual example selection vs automatic optimization

```bash
cd problem_02_few_shot_examples

# Traditional: Manual example selection
python traditional_approach.py

# DSPy: Automatic example selection
python dspy_solution.py
```

**Expected:** DSPy automatically finds best examples using optimization.

---

### Problem 3: Prompt Optimization
**What to test:** Manual iteration vs systematic optimization

```bash
cd problem_03_prompt_optimization

# Traditional: Manual optimization loop
python traditional_approach.py

# DSPy: Automatic optimization (MIPRO, COPRO)
python dspy_solution.py
```

**Expected:** DSPy systematically searches for better prompts.

---

### Problem 4: Model Portability
**What to test:** Model-specific code vs model-agnostic framework

```bash
cd problem_04_model_portability

# Traditional: Different code for each model
python traditional_approach.py

# DSPy: Same code, any model
python dspy_solution.py
```

**Expected:** DSPy solution works with any model by changing one line.

---

### Problem 5: Complex Pipelines
**What to test:** Manual pipeline construction vs modular building blocks

```bash
cd problem_05_complex_pipelines

# Traditional: Manual composition
python traditional_approach.py

# DSPy: Declarative, composable modules
python dspy_solution.py
```

**Expected:** DSPy provides modular, optimizable pipeline components.

---

### Problem 6: Systematic Improvement
**What to test:** Manual A/B testing vs automatic optimization

```bash
cd problem_06_systematic_improvement

# Traditional: Manual testing
python traditional_approach.py

# DSPy: Systematic optimization with metrics
python dspy_solution.py
```

**Expected:** DSPy systematically improves performance based on metrics.

---

### Problem 7: Reproducibility
**What to test:** Scattered prompts vs version-controlled modules

```bash
cd problem_07_reproducibility

# Traditional: No versioning
python traditional_approach.py

# DSPy: Version-controlled, reproducible
python dspy_solution.py
```

**Expected:** DSPy enables saving/loading optimized modules for reproducibility.

---

## 🚀 Run All Tests

```bash
cd /mnt/sdb1/dspy_test
source venv/bin/activate
python run_all_tests.py
```

This will test all 7 problems sequentially.

---

## 🔍 Validation Checklist

For each problem, verify:

- [ ] **Traditional approach runs** - Shows the problem
- [ ] **DSPy solution runs** - Shows the solution
- [ ] **Code is readable** - Clear comments and structure
- [ ] **Examples are runnable** - No syntax errors
- [ ] **DSPy benefits are clear** - Easy to see improvements

---

## 📊 Expected Results

### Problem 1: Brittle Prompts
- ✅ Traditional: String manipulation, hard to maintain
- ✅ DSPy: Declarative signatures, easy to modify

### Problem 2: Few-Shot Examples
- ✅ Traditional: Manual example selection
- ✅ DSPy: Automatic optimization finds best examples

### Problem 3: Prompt Optimization
- ✅ Traditional: Manual iteration, slow
- ✅ DSPy: Systematic search, efficient

### Problem 4: Model Portability
- ✅ Traditional: Model-specific code
- ✅ DSPy: Same code, any model

### Problem 5: Complex Pipelines
- ✅ Traditional: Manual composition
- ✅ DSPy: Modular, composable building blocks

### Problem 6: Systematic Improvement
- ✅ Traditional: Manual A/B testing
- ✅ DSPy: Automatic optimization with metrics

### Problem 7: Reproducibility
- ✅ Traditional: No versioning
- ✅ DSPy: Version-controlled modules

---

## 💡 Tips for Testing

1. **Start with Problem 1** - It introduces core concepts
2. **Compare side-by-side** - Run traditional then DSPy
3. **Read the README** - Each problem folder has detailed explanation
4. **Modify examples** - Try changing inputs to see how DSPy adapts
5. **Check test results** - See `TEST_RESULTS.md` for expected outputs

---

## 🐛 Troubleshooting

### Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### API Key Issues
- Examples work without API keys (use mocks)
- For real LLM testing, set environment variables:
  ```bash
  export OPENAI_API_KEY="your-key"
  export ANTHROPIC_API_KEY="your-key"
  ```

### DSPy Version
```bash
python -c "import dspy; print(dspy.__version__)"
# Should show: 3.0.4
```

---

## 📝 Notes

- All examples are **runnable** without API keys (use mocks)
- Each problem demonstrates a **real-world scenario**
- Code is **well-commented** for learning
- Examples can be **integrated** into your framework

---

**Happy Testing!** 🎉

