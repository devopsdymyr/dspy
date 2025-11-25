"""
Problem 2: Finding Good Few-Shot Examples is Hard

Traditional approach: Manual example selection
"""

def traditional_few_shot_approach():
    """Demonstrate problems with manual few-shot selection"""
    
    print("=" * 70)
    print("PROBLEM 2: Finding Good Few-Shot Examples is Hard")
    print("=" * 70)
    print()
    
    # Problem: Manual selection
    print("🔴 Problem: Manual example selection")
    print("-" * 70)
    
    # You have many potential examples
    all_examples = [
        ("What is AI?", "AI is Artificial Intelligence"),
        ("What is ML?", "ML is Machine Learning"),
        ("What is NLP?", "NLP is Natural Language Processing"),
        ("What is DL?", "DL is Deep Learning"),
        ("What is RL?", "RL is Reinforcement Learning"),
        ("What is CV?", "CV is Computer Vision"),
        ("What is GAN?", "GAN is Generative Adversarial Network"),
        ("What is BERT?", "BERT is Bidirectional Encoder Representations"),
    ]
    
    print(f"You have {len(all_examples)} potential examples.")
    print("Which ones should you use?")
    print()
    
    # Manual selection - guesswork
    selected_examples = all_examples[:3]  # Just pick first 3?
    print("❌ Manual selection (guesswork):")
    for q, a in selected_examples:
        print(f"  Q: {q}")
        print(f"  A: {a}")
    print()
    print("Problems:")
    print("  - Why these 3? No clear reason")
    print("  - How do you know they're best?")
    print("  - What if different examples work better?")
    print("  - Need to test manually")
    print()
    
    # Problem: No metrics
    print("🔴 Problem: No metrics")
    print("-" * 70)
    print("How do you measure if examples help?")
    print("  - Try with examples → get response")
    print("  - Try without examples → get response")
    print("  - Compare manually")
    print("  - No systematic way to measure improvement")
    print()
    
    # Problem: Not scalable
    print("🔴 Problem: Not scalable")
    print("-" * 70)
    print("To find best examples:")
    print("  - Try all combinations? → 2^8 = 256 combinations")
    print("  - Try 3 examples at a time? → C(8,3) = 56 combinations")
    print("  - Each test = API call = time + money")
    print("  - Can't test all combinations manually")
    print()
    
    # Problem: Model-specific
    print("🔴 Problem: Model-specific")
    print("-" * 70)
    print("Examples that work for GPT-3.5:")
    print("  - Might not work for GPT-4")
    print("  - Might not work for Claude")
    print("  - Might not work for Llama")
    print("  - Need to find examples for each model")
    print()


if __name__ == "__main__":
    traditional_few_shot_approach()

