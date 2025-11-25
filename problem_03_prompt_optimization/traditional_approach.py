"""
Problem 3: Prompt Optimization is Manual and Slow

Traditional approach: Manual iteration through prompt variations
"""

def traditional_optimization_approach():
    """Demonstrate problems with manual prompt optimization"""
    
    print("=" * 70)
    print("PROBLEM 3: Prompt Optimization is Manual and Slow")
    print("=" * 70)
    print()
    
    # Problem: Manual iteration
    print("🔴 Problem: Manual iteration")
    print("-" * 70)
    
    # You try different prompt variations manually
    prompt_variations = [
        "Answer: {question}",
        "Please answer: {question}",
        "Question: {question}\nAnswer:",
        "Answer the following question: {question}",
        "Q: {question}\nA:",
        "Please provide an answer to: {question}",
        # ... 100 more variations
    ]
    
    print(f"You have {len(prompt_variations)} prompt variations to try.")
    print("How do you find the best one?")
    print()
    
    print("❌ Manual process:")
    print("  1. Try prompt 1 → test → score: 0.75")
    print("  2. Try prompt 2 → test → score: 0.82")
    print("  3. Try prompt 3 → test → score: 0.79")
    print("  ...")
    print(f"  {len(prompt_variations)}. Try prompt {len(prompt_variations)} → test → score: ?")
    print()
    print("Problems:")
    print("  - Try each one manually")
    print("  - Each test = API call = time + money")
    print("  - No systematic search")
    print("  - Might miss better combinations")
    print()
    
    # Problem: No systematic search
    print("🔴 Problem: No systematic search")
    print("-" * 70)
    print("Search space:")
    print("  - Different prompt structures")
    print("  - Different wordings")
    print("  - Different formats")
    print("  - Different few-shot examples")
    print("  - Different reasoning steps")
    print()
    print("  → Exponential combinations!")
    print("  → Can't test all manually")
    print("  → Might find local optima, miss global best")
    print()
    
    # Problem: Slow and expensive
    print("🔴 Problem: Slow and expensive")
    print("-" * 70)
    print("To test 100 prompt variations:")
    print("  - 100 API calls")
    print("  - ~$1-10 per 100 calls (depending on model)")
    print("  - Hours of manual work")
    print("  - Still might not find best")
    print()
    
    # Problem: Local optima
    print("🔴 Problem: Local optima")
    print("-" * 70)
    print("You might find:")
    print("  - Prompt A: score 0.85 (good)")
    print("  - Stop searching (think it's good enough)")
    print("  - But prompt B: score 0.95 exists (you never tried)")
    print()
    print("  → Manual search often finds local optima")
    print("  → Misses better global solutions")
    print()


if __name__ == "__main__":
    traditional_optimization_approach()

