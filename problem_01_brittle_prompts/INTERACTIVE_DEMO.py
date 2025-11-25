"""
Interactive Demo: Understanding DSPy Step by Step

Run this to see exactly what DSPy does at each step.
"""

import os
import dspy
from dspy.clients import LM

def demo_step_by_step():
    """Interactive demonstration of DSPy concepts"""
    
    print("=" * 70)
    print("🎓 INTERACTIVE DEMO: Understanding DSPy")
    print("=" * 70)
    print()
    
    # Step 1: Show the signature
    print("📝 STEP 1: Define Signature")
    print("-" * 70)
    print("""
class QA(dspy.Signature):
    \"\"\"Answer questions accurately.\"\"\"
    question = dspy.InputField()
    answer = dspy.OutputField()
    """)
    print("💡 What this means:")
    print("   - Input: question (what you provide)")
    print("   - Output: answer (what you want back)")
    print("   - Docstring: instruction for the model")
    print()
    
    # Define it
    class QA(dspy.Signature):
        """Answer questions accurately."""
        question = dspy.InputField()
        answer = dspy.OutputField()
    
    input("Press Enter to continue...")
    print()
    
    # Step 2: Show model configuration
    print("🔧 STEP 2: Configure Model")
    print("-" * 70)
    
    has_key = os.getenv("OPENAI_API_KEY")
    if has_key:
        print("✅ API key found! Using real model.")
        lm = LM(model="openai/gpt-3.5-turbo")
        dspy.configure(lm=lm)
        print(f"   Model: openai/gpt-3.5-turbo")
    else:
        print("⚠️  No API key. Using mock mode.")
        print("   (Set OPENAI_API_KEY for real execution)")
        # Use a mock for demonstration
        class MockLM:
            def __call__(self, prompt, **kwargs):
                return "AI stands for Artificial Intelligence. It's the simulation of human intelligence by machines."
        dspy.configure(lm=MockLM())
    
    print()
    print("💡 Key point: Same code works with ANY model!")
    print("   - OpenAI: LM(model='openai/gpt-3.5-turbo')")
    print("   - Anthropic: LM(model='anthropic/claude-3-haiku-20240307')")
    print("   - Ollama: LM(model='ollama/llama3')")
    print()
    
    input("Press Enter to continue...")
    print()
    
    # Step 3: Create predictor
    print("🚀 STEP 3: Create Predictor")
    print("-" * 70)
    print("""
qa = dspy.Predict(QA)
    """)
    print("💡 What this does:")
    print("   - Takes your signature (QA)")
    print("   - Creates a callable function")
    print("   - Handles prompt generation automatically")
    print()
    
    qa = dspy.Predict(QA)
    
    input("Press Enter to continue...")
    print()
    
    # Step 4: Use it
    print("✨ STEP 4: Use It")
    print("-" * 70)
    print("""
result = qa(question="What is AI?")
print(result.answer)
    """)
    print()
    
    if has_key:
        print("🔄 Calling the model...")
        result = qa(question="What is AI?")
        print()
        print("📥 Result:")
        print(f"   Question: {result.question}")
        print(f"   Answer: {result.answer}")
    else:
        print("📥 Result (mock):")
        print("   Question: What is AI?")
        print("   Answer: AI stands for Artificial Intelligence. It's the simulation of human intelligence by machines.")
    
    print()
    print("💡 Notice:")
    print("   - Simple function call (no manual API code)")
    print("   - Structured result (result.answer, not parsing JSON)")
    print("   - Same code works with any model")
    print()
    
    input("Press Enter to continue...")
    print()
    
    # Step 5: Show what DSPy did behind the scenes
    print("🔍 STEP 5: What DSPy Did Behind the Scenes")
    print("-" * 70)
    print("""
When you called: qa(question="What is AI?")

DSPy automatically:
1. ✅ Generated a prompt from your signature
2. ✅ Formatted it for the model
3. ✅ Called the API
4. ✅ Parsed the response
5. ✅ Returned structured result

You didn't have to:
❌ Write prompt strings
❌ Handle API calls
❌ Parse responses
❌ Deal with model differences
    """)
    print()
    
    # Step 6: Compare with traditional
    print("📊 STEP 6: Comparison")
    print("-" * 70)
    print("""
Traditional Approach:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
prompt = f\"\"\"You are a helpful assistant. Answer the following question accurately.

Question: {question}

Answer:\"\"\"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
answer = response.choices[0].message.content

Problems:
❌ Hard-coded prompt
❌ Manual API handling
❌ Model-specific code
❌ Hard to maintain

DSPy Approach:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
class QA(dspy.Signature):
    question = dspy.InputField()
    answer = dspy.OutputField()

qa = dspy.Predict(QA)
result = qa(question="What is AI?")

Benefits:
✅ Declarative (define WHAT, not HOW)
✅ Model-agnostic (same code, any model)
✅ Maintainable (update signature once)
✅ Optimizable (framework can improve)
    """)
    print()
    
    print("=" * 70)
    print("✅ Demo Complete!")
    print("=" * 70)
    print()
    print("Next steps:")
    print("  1. Try modifying the signature (change docstring)")
    print("  2. Try different models (if you have API keys)")
    print("  3. Compare with traditional_approach.py")
    print("  4. Move to Problem 2: Few-Shot Examples")
    print()


if __name__ == "__main__":
    demo_step_by_step()

