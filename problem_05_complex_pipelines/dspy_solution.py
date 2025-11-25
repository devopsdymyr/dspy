"""
Problem 5: DSPy Solution - Modular, Composable Pipelines

DSPy provides modular building blocks that can be composed and optimized.
"""

try:
    import dspy
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False
    print("⚠️  DSPy not installed. Install with: pip install dspy-ai")


def dspy_pipeline_solution():
    """Demonstrate DSPy's modular pipeline approach"""
    
    print("=" * 70)
    print("DSPY SOLUTION: Modular, Composable Pipelines")
    print("=" * 70)
    print()
    
    if not DSPY_AVAILABLE:
        print("✅ Code structure (would work with DSPy):")
        print()
        print("""
# Step 1: Define modular components
class RAGPipeline(dspy.Module):
    def __init__(self):
        # Modular building blocks
        self.retrieve = dspy.Retrieve(k=3)
        self.generate = dspy.ChainOfThought("context, question -> answer")
    
    def forward(self, question):
        # Compose components
        context = self.retrieve(question).passages
        return self.generate(context=context, question=question)

# Step 2: Use it
pipeline = RAGPipeline()
result = pipeline("What is AI?")

# Step 3: Optimize entire pipeline
from dspy.teleprompt import BootstrapFewShot
optimizer = BootstrapFewShot(metric=validate_answer)
optimized_pipeline = optimizer.compile(
    student=RAGPipeline(),
    trainset=examples
)

# Framework automatically optimizes:
# - Retrieval strategy
# - Prompt format
# - Few-shot examples
# - All components together
        """)
        return
    
    print("✅ Step 1: Define modular components")
    print("-" * 70)
    print("""
class RAGPipeline(dspy.Module):
    def __init__(self):
        # Modular building blocks
        self.retrieve = dspy.Retrieve(k=3)
        self.generate = dspy.ChainOfThought("context, question -> answer")
    
    def forward(self, question):
        # Compose components
        context = self.retrieve(question).passages
        return self.generate(context=context, question=question)
    """)
    print()
    
    print("✅ Benefits of modular design:")
    print("  - Composable: Mix and match building blocks")
    print("  - Swappable: Easy to replace components")
    print("  - Testable: Test components separately")
    print("  - Optimizable: Optimize entire pipeline")
    print()
    
    print("✅ Step 2: Optimize entire pipeline")
    print("-" * 70)
    print("""
optimizer = BootstrapFewShot(metric=validate_answer)
optimized_pipeline = optimizer.compile(
    student=RAGPipeline(),
    trainset=examples
)
    """)
    print()
    print("Framework automatically optimizes:")
    print("  - Retrieval: Best k value, retrieval strategy")
    print("  - Prompt: Best format, structure")
    print("  - Examples: Best few-shot examples")
    print("  - All together: End-to-end optimization")
    print()
    
    print("✅ Benefits:")
    print("  - Modular: Compose building blocks")
    print("  - Optimizable: Optimize entire pipeline")
    print("  - Declarative: Define structure, not implementation")
    print("  - Testable: Test as a unit")
    print()


if __name__ == "__main__":
    dspy_pipeline_solution()

