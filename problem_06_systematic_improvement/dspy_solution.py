"""
Problem 6: DSPy Solution - Systematic Performance Improvement

DSPy provides systematic optimization with metrics and automatic search.
"""

try:
    import dspy
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False
    print("⚠️  DSPy not installed. Install with: pip install dspy-ai")


def dspy_systematic_improvement_solution():
    """Demonstrate DSPy's systematic improvement approach"""
    
    print("=" * 70)
    print("DSPY SOLUTION: Systematic Performance Improvement")
    print("=" * 70)
    print()
    
    if not DSPY_AVAILABLE:
        print("✅ Code structure (would work with DSPy):")
        print()
        print("""
# Step 1: Define metric (what is "good"?)
def validate_answer(example, pred, trace=None):
    expected = example.answer.lower()
    actual = pred.answer.lower()
    return expected in actual or actual in expected

# Step 2: Systematic optimization
from dspy.teleprompt import MIPRO

optimizer = MIPRO(
    metric=validate_answer,
    num_candidates=10,
    init_temperature=1.0
)

optimized = optimizer.compile(
    student=QA,
    trainset=examples
)

# Framework automatically:
# - Searches systematically (not randomly)
# - Uses metric to guide search
# - Finds better solutions
# - Optimizes efficiently
        """)
        return
    
    print("✅ Step 1: Define metric")
    print("-" * 70)
    print("""
def validate_answer(example, pred, trace=None):
    \"\"\"Metric: answer should contain expected answer\"\"\"
    expected = example.answer.lower()
    actual = pred.answer.lower()
    return expected in actual or actual in expected
    """)
    print()
    print("  - Define what 'good' means for your task")
    print("  - Framework uses this to guide optimization")
    print("  - Can be any function (accuracy, F1, custom)")
    print()
    
    print("✅ Step 2: Systematic optimization")
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
    
    print("What the framework does:")
    print("  1. Generates candidate prompts/examples")
    print("  2. Tests each with your metric")
    print("  3. Selects best candidates")
    print("  4. Refines and iterates")
    print("  5. Returns optimized module")
    print()
    
    print("✅ Benefits:")
    print("  - Systematic: Explores search space efficiently")
    print("  - Metric-driven: Optimizes what you care about")
    print("  - Automatic: No manual testing")
    print("  - Global optimization: Finds better solutions")
    print()
    
    print("✅ Real-world impact:")
    print("-" * 70)
    print("Before DSPy:")
    print("  - Days/weeks to optimize manually")
    print("  - Hundreds of API calls")
    print("  - Local optima (not best solution)")
    print()
    print("After DSPy:")
    print("  - Hours to optimize automatically")
    print("  - Efficient optimization (fewer wasted calls)")
    print("  - Better solutions (systematic search)")
    print()


if __name__ == "__main__":
    dspy_systematic_improvement_solution()

