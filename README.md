# DSPy: Problems & Solutions - Testable Examples

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains practical examples demonstrating the problems DSPy solves and how it solves them. Perfect for learning DSPy through hands-on examples.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📁 Structure

```
dspy_problems_solutions/
├── README.md                          # This file
├── requirements.txt                   # Dependencies
├── problem_01_brittle_prompts/        # Problem 1: Manual prompt engineering
├── problem_02_few_shot_examples/      # Problem 2: Finding good examples
├── problem_03_prompt_optimization/    # Problem 3: Manual optimization
├── problem_04_model_portability/      # Problem 4: Model-specific code
├── problem_05_complex_pipelines/       # Problem 5: Building pipelines
├── problem_06_systematic_improvement/  # Problem 6: Performance improvement
└── problem_07_reproducibility/        # Problem 7: Version control
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys (Optional - for real LLM testing)
```bash
export OPENAI_API_KEY="your-key-here"
# or
export ANTHROPIC_API_KEY="your-key-here"
```

### 3. Run Examples
Each problem folder contains:
- `traditional_approach.py` - Shows the problem
- `dspy_solution.py` - Shows the solution
- `README.md` - Explanation

Run any example:
```bash
cd problem_01_brittle_prompts
python traditional_approach.py
python dspy_solution.py
```

## 📊 Problem Overview

| Problem | Folder | Key Issue | DSPy Solution |
|---------|--------|-----------|---------------|
| 1. Brittle Prompts | `problem_01_brittle_prompts/` | Manual prompt crafting | Declarative signatures |
| 2. Few-Shot Examples | `problem_02_few_shot_examples/` | Manual example selection | Automatic optimization |
| 3. Prompt Optimization | `problem_03_prompt_optimization/` | Manual iteration | Systematic search |
| 4. Model Portability | `problem_04_model_portability/` | Model-specific code | Model-agnostic framework |
| 5. Complex Pipelines | `problem_05_complex_pipelines/` | Manual composition | Modular building blocks |
| 6. Systematic Improvement | `problem_06_systematic_improvement/` | Manual A/B testing | Automatic optimization |
| 7. Reproducibility | `problem_07_reproducibility/` | Scattered prompts | Version-controlled modules |

## 🎯 Learning Path

1. **Start with Problem 1** - Understand the basic issue with manual prompts
2. **Progress sequentially** - Each problem builds on previous concepts
3. **Compare approaches** - Run both traditional and DSPy versions
4. **Experiment** - Modify examples to see how DSPy adapts

## 💡 Key Concepts

- **Signatures**: Declarative way to define input/output
- **Modules**: Composable building blocks
- **Optimizers**: Automatic prompt/example optimization
- **Metrics**: Define what "good" means for your task

## 🔧 Requirements

- Python 3.8+
- DSPy library
- (Optional) LLM API keys for real testing

## 📝 Notes

- Examples use mock responses when API keys aren't available
- All examples are runnable and testable
- Each example includes clear comments explaining the problem

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add more problem examples
- Improve existing examples
- Fix bugs or typos
- Enhance documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Learning!** 🚀

