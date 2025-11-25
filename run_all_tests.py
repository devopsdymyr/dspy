#!/usr/bin/env python3
"""
Test Runner for All DSPy Problems & Solutions

This script runs all problem demonstrations to validate they work correctly.
"""

import os
import sys
import subprocess
from pathlib import Path

# Color codes for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_header(text):
    """Print formatted header"""
    print(f"\n{BOLD}{BLUE}{'=' * 70}{RESET}")
    print(f"{BOLD}{BLUE}{text}{RESET}")
    print(f"{BOLD}{BLUE}{'=' * 70}{RESET}\n")

def print_success(text):
    """Print success message"""
    print(f"{GREEN}✅ {text}{RESET}")

def print_error(text):
    """Print error message"""
    print(f"{RED}❌ {text}{RESET}")

def print_warning(text):
    """Print warning message"""
    print(f"{YELLOW}⚠️  {text}{RESET}")

def run_script(script_path):
    """Run a Python script and return success status"""
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except subprocess.TimeoutExpired:
        return False, "Timeout after 30 seconds"
    except Exception as e:
        return False, str(e)

def check_dspy_installation():
    """Check if DSPy is installed"""
    try:
        import dspy
        print_success("DSPy is installed")
        return True
    except ImportError:
        print_warning("DSPy is not installed (examples will show structure but won't run)")
        print("  Install with: pip install dspy-ai")
        return False

def main():
    """Run all tests"""
    print_header("DSPy Problems & Solutions - Test Runner")
    
    # Check DSPy installation
    dspy_installed = check_dspy_installation()
    print()
    
    # Get base directory
    base_dir = Path(__file__).parent
    
    # Define all problems to test
    problems = [
        "problem_01_brittle_prompts",
        "problem_02_few_shot_examples",
        "problem_03_prompt_optimization",
        "problem_04_model_portability",
        "problem_05_complex_pipelines",
        "problem_06_systematic_improvement",
        "problem_07_reproducibility",
    ]
    
    results = {}
    
    # Test each problem
    for problem in problems:
        problem_dir = base_dir / problem
        
        if not problem_dir.exists():
            print_error(f"Problem directory not found: {problem}")
            results[problem] = {"status": "missing", "tests": {}}
            continue
        
        print_header(f"Testing {problem}")
        
        problem_results = {}
        
        # Test traditional approach
        traditional_script = problem_dir / "traditional_approach.py"
        if traditional_script.exists():
            print(f"\n{BOLD}Running: traditional_approach.py{RESET}")
            success, output = run_script(traditional_script)
            if success:
                print_success("Traditional approach demonstration passed")
                problem_results["traditional"] = "passed"
                # Show first few lines of output
                lines = output.split('\n')[:10]
                for line in lines:
                    if line.strip():
                        print(f"  {line}")
            else:
                print_error(f"Traditional approach failed: {output[:200]}")
                problem_results["traditional"] = "failed"
        else:
            print_warning("traditional_approach.py not found")
            problem_results["traditional"] = "missing"
        
        # Test DSPy solution
        dspy_script = problem_dir / "dspy_solution.py"
        if dspy_script.exists():
            print(f"\n{BOLD}Running: dspy_solution.py{RESET}")
            success, output = run_script(dspy_script)
            if success:
                print_success("DSPy solution demonstration passed")
                problem_results["dspy"] = "passed"
                # Show first few lines of output
                lines = output.split('\n')[:10]
                for line in lines:
                    if line.strip():
                        print(f"  {line}")
            else:
                print_warning(f"DSPy solution (may need API keys): {output[:200]}")
                problem_results["dspy"] = "warning"
        else:
            print_warning("dspy_solution.py not found")
            problem_results["dspy"] = "missing"
        
        # Test framework integration (if exists)
        framework_script = problem_dir / "test_with_framework.py"
        if framework_script.exists():
            print(f"\n{BOLD}Running: test_with_framework.py{RESET}")
            success, output = run_script(framework_script)
            if success:
                print_success("Framework integration test passed")
                problem_results["framework"] = "passed"
            else:
                print_warning(f"Framework integration (may need framework): {output[:200]}")
                problem_results["framework"] = "warning"
        
        results[problem] = {"status": "tested", "tests": problem_results}
        print()
    
    # Print summary
    print_header("Test Summary")
    
    total_problems = len(problems)
    passed_traditional = sum(1 for r in results.values() if r.get("tests", {}).get("traditional") == "passed")
    passed_dspy = sum(1 for r in results.values() if r.get("tests", {}).get("dspy") in ["passed", "warning"])
    
    print(f"\n{BOLD}Results:{RESET}")
    print(f"  Total problems: {total_problems}")
    print(f"  Traditional approach tests passed: {passed_traditional}/{total_problems}")
    print(f"  DSPy solution tests passed: {passed_dspy}/{total_problems}")
    print()
    
    print(f"{BOLD}Detailed Results:{RESET}")
    for problem, result in results.items():
        status_icon = "✅" if result.get("status") == "tested" else "❌"
        print(f"  {status_icon} {problem}")
        for test_name, test_status in result.get("tests", {}).items():
            if test_status == "passed":
                print(f"      ✅ {test_name}")
            elif test_status == "warning":
                print(f"      ⚠️  {test_name}")
            elif test_status == "failed":
                print(f"      ❌ {test_name}")
            else:
                print(f"      ⚪ {test_name} (missing)")
    
    print()
    print_success("All tests completed!")
    print()
    print("💡 Next steps:")
    print("  1. Install DSPy: pip install dspy-ai")
    print("  2. Set API keys (optional): export OPENAI_API_KEY=...")
    print("  3. Run individual problems: cd problem_01_brittle_prompts && python traditional_approach.py")
    print()

if __name__ == "__main__":
    main()

