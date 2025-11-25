"""
Problem 6: No Systematic Way to Improve Performance

Traditional approach: Manual A/B testing
"""

def traditional_improvement_approach():
    """Demonstrate problems with manual performance improvement"""
    
    print("=" * 70)
    print("PROBLEM 6: No Systematic Way to Improve Performance")
    print("=" * 70)
    print()
    
    # Problem: Exponential search space
    print("🔴 Problem: Exponential search space")
    print("-" * 70)
    
    print("To improve performance, you can try:")
    print("  - Different prompts: 10 variations")
    print("  - Different examples: 20 example sets")
    print("  - Different models: 5 models")
    print("  - Different retrieval: 3 strategies")
    print()
    print("Search space: 10 × 20 × 5 × 3 = 3,000 combinations!")
    print()
    print("❌ Manual testing:")
    print("  - Try combination 1 → test → score: 0.75")
    print("  - Try combination 2 → test → score: 0.82")
    print("  - Try combination 3 → test → score: 0.79")
    print("  ...")
    print("  - Try combination 3000 → test → score: ?")
    print()
    print("  → Can't test all combinations manually")
    print("  → Might miss best combination")
    print()
    
    # Problem: No metrics
    print("🔴 Problem: No metrics")
    print("-" * 70)
    print("How do you measure improvement?")
    print("  - Try prompt A → get response")
    print("  - Try prompt B → get response")
    print("  - Compare manually")
    print("  - Which is better? Hard to tell")
    print()
    print("  → No clear metric")
    print("  → Subjective evaluation")
    print("  → Hard to automate")
    print()
    
    # Problem: Manual testing
    print("🔴 Problem: Manual testing")
    print("-" * 70)
    print("To test 100 combinations:")
    print("  - Write test code for each")
    print("  - Run each test")
    print("  - Collect results")
    print("  - Compare manually")
    print()
    print("  → Hours of manual work")
    print("  → Error-prone")
    print("  → Not scalable")
    print()
    
    # Problem: Local optima
    print("🔴 Problem: Local optima")
    print("-" * 70)
    print("You might find:")
    print("  - Combination A: score 0.85 (good)")
    print("  - Stop searching (think it's good enough)")
    print("  - But combination B: score 0.95 exists")
    print()
    print("  → Manual search finds local optima")
    print("  → Misses better global solutions")
    print()


if __name__ == "__main__":
    traditional_improvement_approach()

