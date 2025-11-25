"""
Problem 3: DSPy Solution - Automatic Prompt Optimization

DSPy provides systematic optimization strategies (MIPRO, COPRO, etc.)
"""

try:
    import dspy
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False
    print("⚠️  DSPy not installed. Install with: pip install dspy-ai")


def dspy_optimization_solution():
    """Demonstrate DSPy's automatic optimization"""
    
    print("=" * 70)
    print("DSPY SOLUTION: Automatic Prompt Optimization")
    print("=" * 70)
    print()
    
    if not DSPY_AVAILABLE:
        print("✅ Code structure (would work with DSPy):")
        print()
        print("""
# Step 1: Define signature
class QA(dspy.Signature):
    question = dspy.InputField()
    answer = dspy.OutputField()

# Step 2: Define metric
def validate_answer(example, pred, trace=None):
    return example.answer.lower() in pred.answer.lower()

# Step 3: Automatic optimization with MIPRO
from dspy.teleprompt import MIPRO

optimizer = MIPRO(
    metric=validate_answer,
    num_candidates=10,
    init_temperature=1.0
)

optimized_qa = optimizer.compile(
    student=QA,
    trainset=examples
)

# Framework automatically:
# - Searches prompt space systematically
# - Tests many variations efficiently
# - Finds better solutions
# - Optimizes with minimal API calls
        """)
        return
    
    print("✅ DSPy provides multiple optimization strategies:")
    print()
    
    # Strategy 1: BootstrapFewShot
    print("1. BootstrapFewShot")
    print("   - Optimizes few-shot examples")
    print("   - Good for: Improving example selection")
    print()
    
    # Strategy 2: MIPRO
    print("2. MIPRO (Multi-prompt optimization)")
    print("   - Optimizes prompt structure and examples")
    print("   - Good for: Comprehensive optimization")
    print("   - Efficient: Smart search strategies")
    print()
    
    # Strategy 3: COPRO
    print("3. COPRO (Coordinate ascent)")
    print("   - Optimizes one component at a time")
    print("   - Good for: Fine-tuning specific parts")
    print()
    
    print("✅ Example: MIPRO optimization")
    print("-" * 70)
    print("""
optimizer = MIPRO(
    metric=validate_answer,
    num_candidates=10,      # Try 10 variations
    init_temperature=1.0     # Exploration vs exploitation
)

optimized = optimizer.compile(student=QA, trainset=examples)
    """)
    print()
    
    print("What MIPRO does automatically:")
    print("  1. Generates candidate prompts")
    print("  2. Tests each with your metric")
    print("  3. Selects best candidates")
    print("  4. Refines and iterates")
    print("  5. Returns optimized module")
    print()
    
    print("✅ Benefits:")
    print("  - Automatic: No manual iteration")
    print("  - Systematic: Explores search space efficiently")
    print("  - Efficient: Smart strategies, fewer API calls")
    print("  - Better solutions: Finds global optima")
    print()


if __name__ == "__main__":
    dspy_optimization_solution()

