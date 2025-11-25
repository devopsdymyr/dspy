"""
Problem 1: DSPy Solution - Declarative Signatures

This demonstrates how DSPy solves the brittle prompt problem:
- Declarative signatures (define WHAT, not HOW)
- Same code works across models
- Systematic optimization possible
- Centralized and maintainable
"""

try:
    import dspy
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False
    print("⚠️  DSPy not installed. Install with: pip install dspy-ai")
    print("   This example will show the structure but won't run.")


# ============================================================================
# DSPY SOLUTION - Declarative Signatures
# ============================================================================

def dspy_qa_solution():
    """
    DSPy approach: Declarative signatures
    
    BENEFITS:
    1. Declarative - define intent, not implementation
    2. Model-agnostic - same code works everywhere
    3. Optimizable - framework can improve automatically
    4. Maintainable - centralized signatures
    """
    
    if not DSPY_AVAILABLE:
        print("\n" + "=" * 70)
        print("DSPY SOLUTION: Declarative Signatures")
        print("=" * 70)
        print("\n✅ Code structure (would work with DSPy):")
        print()
        print("""
# Step 1: Define signature (WHAT you want, not HOW)
class QA(dspy.Signature):
    \"\"\"Answer questions accurately.\"\"\"
    question = dspy.InputField()
    answer = dspy.OutputField()

# Step 2: Use it (works with ANY model)
from dspy.clients import LM
lm = LM(model="openai/gpt-3.5-turbo")  # or
# lm = LM(model="anthropic/claude-3-haiku-20240307")  # or
# lm = LM(model="ollama/llama3")       # or any model

dspy.configure(lm=lm)
qa = dspy.Predict(QA)

# Step 3: Use it
result = qa(question="What is AI?")
print(result.answer)
        """)
        return
    
    print("\n" + "=" * 70)
    print("DSPY SOLUTION: Declarative Signatures")
    print("=" * 70)
    print()
    
    # Step 1: Define signature declaratively
    class QA(dspy.Signature):
        """Answer questions accurately."""
        question = dspy.InputField()
        answer = dspy.OutputField()
    
    print("✅ Step 1: Define signature (declarative)")
    print("   - Define WHAT you want (question → answer)")
    print("   - Framework handles HOW (prompt generation)")
    print()
    
    # Step 2: Configure with any model
    print("✅ Step 2: Configure with any model")
    print("   - Same code works with OpenAI, Anthropic, Ollama, etc.")
    print("   - Change model with one line: dspy.configure(lm=new_lm)")
    print()
    
    # Try to use real LM if available
    import os
    has_api_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    
    if has_api_key:
        try:
            from dspy.clients import LM
            if os.getenv("OPENAI_API_KEY"):
                lm = LM(model="openai/gpt-3.5-turbo")
            elif os.getenv("ANTHROPIC_API_KEY"):
                lm = LM(model="anthropic/claude-3-haiku-20240307")
            dspy.configure(lm=lm)
            qa = dspy.Predict(QA)
            
            # Step 3: Use it
            print("✅ Step 3: Use it (same code, any model)")
            print("-" * 70)
            result = qa(question="What is AI?")
            print(f"Question: What is AI?")
            print(f"Answer: {result.answer}")
        except Exception as e:
            print("⚠️  Error configuring LM:", str(e))
            print("   (This is expected if API keys are invalid)")
    else:
        print("⚠️  No API keys found. Skipping actual execution.")
        print("   Set OPENAI_API_KEY or ANTHROPIC_API_KEY for real testing.")
        print()
        print("✅ Step 3: Use it (same code, any model)")
        print("-" * 70)
        print("   With API keys, you would run:")
        print("   result = qa(question='What is AI?')")
        print("   print(result.answer)")
    print()
    
    print("✅ Benefits:")
    print("  - Declarative: Define intent, not implementation")
    print("  - Model-agnostic: Same code, any model")
    print("  - Maintainable: Update signature once, works everywhere")
    print("  - Optimizable: Framework can improve automatically")
    print()


if __name__ == "__main__":
    dspy_qa_solution()

