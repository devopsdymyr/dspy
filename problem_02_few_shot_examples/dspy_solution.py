"""
Problem 2: DSPy Solution - Automatic Example Selection

DSPy automatically finds best few-shot examples through optimization.
"""

try:
    import dspy
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False
    print("⚠️  DSPy not installed. Install with: pip install dspy-ai")


def dspy_few_shot_solution():
    """Demonstrate DSPy's automatic few-shot optimization"""
    
    print("=" * 70)
    print("DSPY SOLUTION: Automatic Few-Shot Example Selection")
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

# Step 3: Prepare training examples
trainset = [
    dspy.Example(question="What is AI?", answer="AI is Artificial Intelligence"),
    dspy.Example(question="What is ML?", answer="ML is Machine Learning"),
    # ... more examples
]

# Step 4: Automatic optimization
from dspy.teleprompt import BootstrapFewShot
optimizer = BootstrapFewShot(metric=validate_answer)
optimized_qa = optimizer.compile(student=QA, trainset=trainset)

# Framework automatically:
# - Tests different example combinations
# - Selects best examples based on metric
# - Optimizes for your specific model
        """)
        return
    
    # Step 1: Define signature
    class QA(dspy.Signature):
        """Answer questions accurately."""
        question = dspy.InputField()
        answer = dspy.OutputField()
    
    print("✅ Step 1: Define signature")
    print()
    
    # Step 2: Define metric
    def validate_answer(example, pred, trace=None):
        """Metric: answer should contain expected answer"""
        expected = example.answer.lower()
        actual = pred.answer.lower()
        return expected in actual or actual in expected
    
    print("✅ Step 2: Define metric")
    print("   - Framework uses this to measure quality")
    print("   - Automatically selects examples that improve metric")
    print()
    
    # Step 3: Prepare examples
    trainset = [
        dspy.Example(question="What is AI?", answer="AI is Artificial Intelligence"),
        dspy.Example(question="What is ML?", answer="ML is Machine Learning"),
        dspy.Example(question="What is NLP?", answer="NLP is Natural Language Processing"),
        dspy.Example(question="What is DL?", answer="DL is Deep Learning"),
    ]
    
    print("✅ Step 3: Provide training examples")
    print(f"   - {len(trainset)} examples available")
    print("   - Framework will automatically select best ones")
    print()
    
    # Step 4: Automatic optimization (demo)
    print("✅ Step 4: Automatic optimization")
    print("-" * 70)
    print("With DSPy BootstrapFewShot optimizer:")
    print("  - Tests different example combinations")
    print("  - Measures performance with your metric")
    print("  - Selects best examples automatically")
    print("  - Adapts to your specific model")
    print()
    print("Example optimization process:")
    print("  1. Try examples [1, 2, 3] → score: 0.85")
    print("  2. Try examples [2, 3, 4] → score: 0.92")
    print("  3. Try examples [1, 3, 4] → score: 0.88")
    print("  → Select [2, 3, 4] (best score)")
    print()
    
    print("✅ Benefits:")
    print("  - Automatic: No manual selection needed")
    print("  - Metric-driven: Optimizes what you care about")
    print("  - Scalable: Tests many combinations efficiently")
    print("  - Model-adaptive: Adapts to different models")
    print()


if __name__ == "__main__":
    dspy_few_shot_solution()

