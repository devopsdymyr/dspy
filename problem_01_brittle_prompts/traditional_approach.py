"""
Problem 1: Manual Prompt Engineering is Brittle

This demonstrates the traditional approach with its problems:
- Brittle prompts that break easily
- Hard to maintain
- Model-specific code
- No systematic improvement
"""

# ============================================================================
# TRADITIONAL APPROACH - The Problems
# ============================================================================

def traditional_qa_approach(question, model="gpt-3.5"):
    """
    Traditional approach: Manual prompt crafting
    
    PROBLEMS:
    1. Hard-coded prompt strings
    2. Different prompts for different models
    3. Brittle - small changes break everything
    4. No way to systematically improve
    5. Prompts scattered in code
    """
    
    # Problem 1: Hard-coded prompt strings
    if model == "gpt-3.5":
        prompt = f"""You are a helpful assistant. Answer the following question accurately.

Question: {question}

Answer:"""
    elif model == "gpt-4":
        prompt = f"""Please provide an accurate answer to the following question.

Question: {question}

Your answer:"""
    elif model == "claude":
        prompt = f"""Question: {question}

Answer:"""
    else:
        prompt = f"Answer: {question}"
    
    # Problem 2: Manual API calls
    # (In real code, you'd call the API here)
    print(f"📝 Using prompt for {model}:")
    print(prompt)
    print("\n❌ Problems:")
    print("  - Different prompt for each model")
    print("  - Hard to maintain (update in multiple places)")
    print("  - No systematic way to improve")
    print("  - Brittle (small changes break everything)\n")
    
    return prompt


def demonstrate_problems():
    """Show all the problems with traditional approach"""
    
    print("=" * 70)
    print("PROBLEM 1: Manual Prompt Engineering is Brittle")
    print("=" * 70)
    print()
    
    # Problem: Different prompts for different models
    print("🔴 Problem: Model-specific prompts")
    print("-" * 70)
    traditional_qa_approach("What is AI?", model="gpt-3.5")
    print()
    traditional_qa_approach("What is AI?", model="gpt-4")
    print()
    traditional_qa_approach("What is AI?", model="claude")
    print()
    
    # Problem: Hard to update
    print("🔴 Problem: Hard to maintain")
    print("-" * 70)
    print("If you want to improve the prompt, you need to:")
    print("  1. Find all places where prompt is used")
    print("  2. Update each one manually")
    print("  3. Test each model separately")
    print("  4. Hope you didn't break anything")
    print()
    
    # Problem: No systematic improvement
    print("🔴 Problem: No systematic improvement")
    print("-" * 70)
    print("How do you know if a prompt is good?")
    print("  - Try different variations manually")
    print("  - Test each one")
    print("  - Hope you find something better")
    print("  - No guarantee you found the best")
    print()
    
    # Problem: Brittle
    print("🔴 Problem: Brittle prompts")
    print("-" * 70)
    print("Small changes can break everything:")
    print("  - Change 'Answer:' to 'Response:' → might break")
    print("  - Add/remove newline → might break")
    print("  - Change wording slightly → might break")
    print("  - No way to test systematically")
    print()


if __name__ == "__main__":
    demonstrate_problems()

