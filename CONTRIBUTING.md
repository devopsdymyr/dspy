# Contributing to DSPy Problems & Solutions

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🎯 How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:
1. Check if the issue already exists
2. Create a new issue with:
   - Clear description
   - Steps to reproduce (if applicable)
   - Expected vs actual behavior

### Adding New Examples

1. **Fork the repository**
2. **Create a new problem folder** following the naming convention:
   - `problem_XX_description/`
   - Include: `README.md`, `traditional_approach.py`, `dspy_solution.py`

3. **Follow the structure:**
   ```
   problem_XX_description/
   ├── README.md                  # Problem explanation
   ├── traditional_approach.py    # Shows the problem
   └── dspy_solution.py           # Shows the solution
   ```

4. **Ensure code quality:**
   - Clear comments
   - Runnable examples
   - Works without API keys (use mocks)

5. **Update main README.md** with your new problem

6. **Submit a pull request**

### Improving Existing Examples

- Fix bugs
- Improve documentation
- Add more comments
- Enhance examples

## 📝 Code Style

- Follow PEP 8 for Python code
- Use clear, descriptive variable names
- Add docstrings to functions
- Include comments explaining key concepts

## ✅ Checklist

Before submitting:
- [ ] Code runs without errors
- [ ] Works without API keys (uses mocks)
- [ ] README updated (if adding new problem)
- [ ] Code is well-commented
- [ ] Follows existing structure

## 🚀 Getting Started

1. Fork the repository
2. Clone your fork
3. Create a virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Make your changes
6. Test your changes
7. Submit a pull request

Thank you for contributing! 🎉

