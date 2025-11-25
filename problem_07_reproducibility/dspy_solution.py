"""
Problem 7: DSPy Solution - Version-Controlled, Reproducible Modules

DSPy provides version control and reproducibility for prompts.
"""

try:
    import dspy
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False
    print("⚠️  DSPy not installed. Install with: pip install dspy-ai")


def dspy_versioning_solution():
    """Demonstrate DSPy's versioning and reproducibility"""
    
    print("=" * 70)
    print("DSPY SOLUTION: Version-Controlled, Reproducible Modules")
    print("=" * 70)
    print()
    
    if not DSPY_AVAILABLE:
        print("✅ Code structure (would work with DSPy):")
        print()
        print("""
# Step 1: Define signature (version-controlled)
class QA(dspy.Signature):
    \"\"\"Version 1.0 - Basic QA\"\"\"
    question = dspy.InputField()
    answer = dspy.OutputField()

# Step 2: Optimize
optimizer = BootstrapFewShot(metric=validate_answer)
optimized_qa = optimizer.compile(student=QA, trainset=examples)

# Step 3: Save version
dspy.settings.save(optimized_qa, "qa_v1.0.json")

# Step 4: Load version (reproducible)
qa_v1 = dspy.settings.load("qa_v1.0.json")

# Step 5: Version control with Git
# - Signatures in code (version-controlled)
# - Optimized modules saved as JSON
# - Can track changes, rollback, compare
        """)
        return
    
    print("✅ Step 1: Version-controlled signatures")
    print("-" * 70)
    print("""
class QA(dspy.Signature):
    \"\"\"Version 1.0 - Basic QA\"\"\"
    question = dspy.InputField()
    answer = dspy.OutputField()
    """)
    print()
    print("  - Signatures in code (Git version control)")
    print("  - Can track changes over time")
    print("  - Can see evolution of prompts")
    print()
    
    print("✅ Step 2: Save optimized modules")
    print("-" * 70)
    print("""
optimizer = BootstrapFewShot(metric=validate_answer)
optimized_qa = optimizer.compile(student=QA, trainset=examples)

# Save version
dspy.settings.save(optimized_qa, "qa_v1.0.json")
    """)
    print()
    print("  - Save optimized modules as JSON")
    print("  - Can load exact same version later")
    print("  - Reproducible results")
    print()
    
    print("✅ Step 3: Load and use versions")
    print("-" * 70)
    print("""
# Load specific version
qa_v1 = dspy.settings.load("qa_v1.0.json")

# Use it
result = qa_v1(question="What is AI?")
    """)
    print()
    print("  - Load exact version used before")
    print("  - Reproduce results")
    print("  - Compare versions")
    print()
    
    print("✅ Step 4: Version control workflow")
    print("-" * 70)
    print("""
# Git workflow
git add qa_v1.0.json
git commit -m "QA module v1.0 - optimized with BootstrapFewShot"

# Later: Create new version
class QA_v2(dspy.Signature):
    \"\"\"Version 2.0 - Enhanced QA\"\"\"
    question = dspy.InputField()
    answer = dspy.OutputField()
    reasoning = dspy.OutputField()

# Optimize and save
optimized_qa_v2 = optimizer.compile(student=QA_v2, trainset=examples)
dspy.settings.save(optimized_qa_v2, "qa_v2.0.json")

# Can rollback if needed
qa_v1 = dspy.settings.load("qa_v1.0.json")
    """)
    print()
    
    print("✅ Benefits:")
    print("  - Version control: Track prompt evolution")
    print("  - Reproducible: Load exact versions")
    print("  - Centralized: Signatures in one place")
    print("  - Rollback: Revert to previous versions")
    print()


if __name__ == "__main__":
    dspy_versioning_solution()

