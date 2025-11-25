"""
Problem 7: Hard to Reproduce and Version Control Prompts

Traditional approach: Scattered prompts, no versioning
"""

def traditional_versioning_approach():
    """Demonstrate problems with prompt versioning"""
    
    print("=" * 70)
    print("PROBLEM 7: Hard to Reproduce and Version Control Prompts")
    print("=" * 70)
    print()
    
    # Problem: Scattered prompts
    print("🔴 Problem: Scattered prompts")
    print("-" * 70)
    
    # Prompts scattered across codebase
    prompts = {
        "file1.py": "Answer: {question}",
        "file2.py": "Q: {question}\nA:",
        "file3.py": "Please answer: {question}",
        "config.json": "Question: {question}\nAnswer:",
    }
    
    print("❌ Prompts scattered in codebase:")
    for file, prompt in prompts.items():
        print(f"  {file}: {prompt}")
    print()
    print("Problems:")
    print("  - Hard to find all prompts")
    print("  - Hard to update consistently")
    print("  - Hard to track changes")
    print()
    
    # Problem: No versioning
    print("🔴 Problem: No versioning")
    print("-" * 70)
    print("How do you track prompt changes?")
    print("  - Which prompt was used in production last week?")
    print("  - Which prompt gave best results?")
    print("  - What changed between version 1 and 2?")
    print()
    print("  → No versioning system")
    print("  → Can't track prompt evolution")
    print("  → Can't reproduce results")
    print()
    
    # Problem: Hard to reproduce
    print("🔴 Problem: Hard to reproduce")
    print("-" * 70)
    print("To reproduce results from last month:")
    print("  - Which prompt was used?")
    print("  - Which examples were used?")
    print("  - Which model was used?")
    print("  - What were the parameters?")
    print()
    print("  → No record of what was used")
    print("  → Can't reproduce results")
    print("  → Can't compare versions")
    print()
    
    # Problem: No rollback
    print("🔴 Problem: No rollback")
    print("-" * 70)
    print("If new prompt breaks production:")
    print("  - What was the previous prompt?")
    print("  - How do you revert?")
    print("  - Where is the backup?")
    print()
    print("  → No rollback mechanism")
    print("  → Hard to revert changes")
    print("  → Risk of breaking production")
    print()


if __name__ == "__main__":
    traditional_versioning_approach()

