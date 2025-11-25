"""
Problem 4: DSPy Solution - Model-Agnostic Code

DSPy provides model-agnostic interface - same code works with any model.
"""

try:
    import dspy
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False
    print("⚠️  DSPy not installed. Install with: pip install dspy-ai")


def dspy_model_agnostic_solution():
    """Demonstrate DSPy's model-agnostic approach"""
    
    print("=" * 70)
    print("DSPY SOLUTION: Model-Agnostic Code")
    print("=" * 70)
    print()
    
    if not DSPY_AVAILABLE:
        print("✅ Code structure (would work with DSPy):")
        print()
        print("""
# Step 1: Define signature (model-agnostic)
class QA(dspy.Signature):
    question = dspy.InputField()
    answer = dspy.OutputField()

# Step 2: Use with ANY model (same code!)
from dspy.clients import LM

# Option 1: OpenAI
lm = LM(model="openai/gpt-3.5-turbo")
dspy.configure(lm=lm)
qa = dspy.Predict(QA)

# Option 2: Anthropic
lm = LM(model="anthropic/claude-3-haiku-20240307")
dspy.configure(lm=lm)
qa = dspy.Predict(QA)  # Same code!

# Option 3: Ollama
lm = LM(model="ollama/llama3")
dspy.configure(lm=lm)
qa = dspy.Predict(QA)  # Same code!

# Option 4: Any other model
lm = LM(model="any-provider/any-model")
dspy.configure(lm=lm)
qa = dspy.Predict(QA)  # Same code!
        """)
        return
    
    # Step 1: Define signature (model-agnostic)
    class QA(dspy.Signature):
        """Answer questions accurately."""
        question = dspy.InputField()
        answer = dspy.OutputField()
    
    print("✅ Step 1: Define signature (model-agnostic)")
    print("   - Same signature works with any model")
    print()
    
    # Step 2: Show how to switch models
    print("✅ Step 2: Switch models with one line")
    print("-" * 70)
    
    models_config = [
        ("OpenAI", "LM(model='openai/gpt-3.5-turbo')"),
        ("Anthropic", "LM(model='anthropic/claude-3-haiku-20240307')"),
        ("Ollama", "LM(model='ollama/llama3')"),
        ("Any model", "LM(model='any-provider/any-model')"),
    ]
    
    for provider, config in models_config:
        print(f"  {provider}:")
        print(f"    from dspy.clients import LM")
        print(f"    lm = {config}")
        print(f"    dspy.configure(lm=lm)")
        print(f"    qa = dspy.Predict(QA)  # Same code!")
        print()
    
    print("✅ Benefits:")
    print("  - Model-agnostic: Same code, any model")
    print("  - Easy switching: Change model with one line")
    print("  - Maintainable: One codebase for all models")
    print("  - Testable: Test once, works everywhere")
    print()
    
    print("✅ Real-world example:")
    print("-" * 70)
    print("""
# Development: Use cheap model
from dspy.clients import LM
lm = LM(model="openai/gpt-3.5-turbo")
dspy.configure(lm=lm)

# Production: Use better model
lm = LM(model="openai/gpt-4")
dspy.configure(lm=lm)

# Testing: Use local model
lm = LM(model="ollama/llama3")
dspy.configure(lm=lm)

# Same code works everywhere!
    """)


if __name__ == "__main__":
    dspy_model_agnostic_solution()

