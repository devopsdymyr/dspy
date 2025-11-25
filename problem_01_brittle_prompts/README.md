# Problem 1: Manual Prompt Engineering is Brittle

## ❌ The Problem

Traditional prompt engineering requires:
- Manual crafting of prompt strings
- Trial and error to find what works
- Different prompts for different models
- Hard to maintain and update
- No systematic way to improve

## ✅ DSPy Solution

DSPy uses **declarative signatures**:
- Define WHAT you want, not HOW
- Framework handles prompt generation
- Same code works across models
- Systematic optimization possible
- Centralized and maintainable

## 🧪 Test It

```bash
# See the problem
python traditional_approach.py

# See the solution
python dspy_solution.py
```

## 📊 Comparison

| Aspect | Traditional | DSPy |
|--------|------------|------|
| **Code** | String manipulation | Declarative signatures |
| **Maintenance** | Update strings everywhere | Update signature once |
| **Model Support** | Different code per model | Same code, any model |
| **Optimization** | Manual trial & error | Automatic optimization |

