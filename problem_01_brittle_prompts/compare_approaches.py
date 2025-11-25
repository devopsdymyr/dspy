"""
Compare Traditional vs DSPy Approaches
Test with your own prompts and see the difference!
"""

import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import dspy
    from dspy.clients import LM
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False
    print("⚠️  DSPy not installed. Install with: pip install dspy-ai")


def traditional_approach(question, model="gpt-3.5"):
    """
    Traditional approach: Manual prompt crafting
    """
    # Hard-coded prompt strings
    if model == "gpt-3.5":
        prompt = f"""You are a helpful assistant. Answer the following question accurately.

Question: {question}

Answer:"""
    elif model == "gpt-4":
        prompt = f"""Please provide an accurate answer to the following question.

Question: {question}

Your answer:"""
    elif model == "claude":
        prompt = f"""Question: {question}

Answer:"""
    else:
        prompt = f"Answer: {question}"
    
    # In real scenario, you'd call the API here
    # For comparison, we'll show what would be sent
    return {
        "prompt": prompt,
        "model": model,
        "method": "traditional"
    }


def dspy_approach(question):
    """
    DSPy approach: Declarative signatures
    """
    if not DSPY_AVAILABLE:
        return {
            "error": "DSPy not available",
            "method": "dspy"
        }
    
    # Define signature
    class QA(dspy.Signature):
        """Answer questions accurately."""
        question = dspy.InputField()
        answer = dspy.OutputField()
    
    # Configure model
    has_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    
    if has_key:
        try:
            if os.getenv("OPENAI_API_KEY"):
                lm = LM(model="openai/gpt-3.5-turbo")
            elif os.getenv("ANTHROPIC_API_KEY"):
                lm = LM(model="anthropic/claude-3-haiku-20240307")
            
            dspy.configure(lm=lm)
            qa = dspy.Predict(QA)
            
            # Get result
            result = qa(question=question)
            
            return {
                "answer": result.answer,
                "question": result.question,
                "method": "dspy",
                "model": "configured"
            }
        except Exception as e:
            return {
                "error": str(e),
                "method": "dspy"
            }
    else:
        return {
            "error": "No API key found. Set OPENAI_API_KEY or ANTHROPIC_API_KEY",
            "method": "dspy",
            "note": "Would work with API key"
        }


def compare_approaches(question, test_traditional=True, test_dspy=True):
    """
    Compare traditional and DSPy approaches side by side
    """
    print("=" * 80)
    print("🔬 COMPARISON: Traditional vs DSPy")
    print("=" * 80)
    print()
    print(f"📝 Your Question: {question}")
    print()
    
    results = {}
    
    # Test Traditional Approach
    if test_traditional:
        print("━" * 80)
        print("1️⃣  TRADITIONAL APPROACH")
        print("━" * 80)
        print()
        
        traditional_result = traditional_approach(question)
        results["traditional"] = traditional_result
        
        print("📋 Prompt Generated:")
        print("-" * 80)
        print(traditional_result["prompt"])
        print()
        print("❌ Problems:")
        print("  - Hard-coded prompt string")
        print("  - Model-specific (different for each model)")
        print("  - Brittle (small changes break it)")
        print("  - No systematic improvement")
        print()
        
        # Show what would be sent to API
        print("🔧 What gets sent to API:")
        print("-" * 80)
        print(f"Model: {traditional_result['model']}")
        print(f"Prompt: {traditional_result['prompt'][:100]}...")
        print()
    
    # Test DSPy Approach
    if test_dspy:
        print("━" * 80)
        print("2️⃣  DSPY APPROACH")
        print("━" * 80)
        print()
        
        dspy_result = dspy_approach(question)
        results["dspy"] = dspy_result
        
        if "error" in dspy_result:
            print(f"⚠️  {dspy_result['error']}")
            if "note" in dspy_result:
                print(f"   {dspy_result['note']}")
            print()
            print("📋 Code Structure:")
            print("-" * 80)
            print("""
class QA(dspy.Signature):
    \"\"\"Answer questions accurately.\"\"\"
    question = dspy.InputField()
    answer = dspy.OutputField()

qa = dspy.Predict(QA)
result = qa(question="Your question here")
            """)
        else:
            print("✅ Answer Generated:")
            print("-" * 80)
            print(f"Question: {dspy_result['question']}")
            print(f"Answer: {dspy_result['answer']}")
            print()
        
        print("✅ Benefits:")
        print("  - Declarative (define WHAT, not HOW)")
        print("  - Model-agnostic (same code, any model)")
        print("  - Maintainable (update signature once)")
        print("  - Optimizable (framework can improve)")
        print()
    
    # Side-by-Side Comparison
    print("━" * 80)
    print("📊 SIDE-BY-SIDE COMPARISON")
    print("━" * 80)
    print()
    
    print(f"{'Traditional Approach':<40} | {'DSPy Approach':<40}")
    print("-" * 40 + "-+-" + "-" * 40)
    
    comparison_points = [
        ("Code Style", "Imperative (HOW)", "Declarative (WHAT)"),
        ("Prompt", "Hard-coded string", "Auto-generated from signature"),
        ("Model Support", "Different code per model", "Same code, any model"),
        ("Maintainability", "Update in multiple places", "Update signature once"),
        ("Optimization", "Manual trial & error", "Automatic optimization"),
        ("Structure", "String manipulation", "Structured fields"),
    ]
    
    for point, traditional, dspy in comparison_points:
        print(f"{point:<20} {traditional:<18} | {dspy:<40}")
    
    print()
    print("=" * 80)
    print("✅ Comparison Complete!")
    print("=" * 80)
    print()
    
    return results


def interactive_mode():
    """
    Interactive mode: Ask for questions and compare
    """
    print("=" * 80)
    print("🎯 INTERACTIVE COMPARISON MODE")
    print("=" * 80)
    print()
    print("Enter your questions to compare Traditional vs DSPy approaches.")
    print("Type 'quit' or 'exit' to stop.")
    print()
    
    # Check API key
    has_key = os.getenv("OPENAI_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
    if not has_key:
        print("⚠️  No API key found. DSPy will show structure only.")
        print("   Set OPENAI_API_KEY for real answers.")
        print()
    
    while True:
        print("-" * 80)
        question = input("Enter your question (or 'quit' to exit): ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if not question:
            print("⚠️  Please enter a question.")
            continue
        
        print()
        compare_approaches(question)
        
        print()
        another = input("Test another question? (y/n): ").strip().lower()
        if another != 'y':
            print("\n👋 Goodbye!")
            break
        print()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Command line mode: test specific question
        question = " ".join(sys.argv[1:])
        compare_approaches(question)
    else:
        # Interactive mode
        interactive_mode()

