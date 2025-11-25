"""
Integration test: DSPy with AI Red Teaming Framework

This shows how DSPy can work with the existing framework's API call patterns.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../.AIRedTeaming'))

try:
    from backend.attack_strategies.utils import format_api_request, parse_api_response
    FRAMEWORK_AVAILABLE = True
except ImportError:
    FRAMEWORK_AVAILABLE = False
    print("⚠️  Framework not found. This is a demo of integration pattern.")


def demonstrate_integration():
    """Show how DSPy concepts can integrate with the framework"""
    
    print("=" * 70)
    print("INTEGRATION: DSPy Concepts with AI Red Teaming Framework")
    print("=" * 70)
    print()
    
    print("💡 Key Insight: DSPy's declarative approach can work with")
    print("   your framework's API call patterns.")
    print()
    
    if FRAMEWORK_AVAILABLE:
        print("✅ Framework utilities available")
        print()
        
        # Show how DSPy signature could map to framework format
        print("Example: DSPy signature → Framework API call")
        print("-" * 70)
        
        # Simulate DSPy signature
        class QA:
            question = "What is AI?"
            answer = None  # Will be filled
        
        # Use framework's format_api_request
        target_url = "http://localhost:11434/v1/chat/completions"
        target_model = "llama3:8b"
        payload = f"Question: {QA.question}\nAnswer:"
        
        request_data = format_api_request(target_url, target_model, payload)
        print("DSPy signature → Framework API format:")
        print(f"  Request: {request_data}")
        print()
        
        print("✅ Benefits of integration:")
        print("  - Use DSPy for prompt optimization")
        print("  - Use framework for API calls and testing")
        print("  - Best of both worlds")
    else:
        print("📝 Integration pattern:")
        print("""
# 1. Define DSPy signature
class AttackSignature(dspy.Signature):
    prompt = dspy.InputField()
    response = dspy.OutputField()

# 2. Use framework's API utilities
from backend.attack_strategies.utils import format_api_request

# 3. Combine: DSPy optimizes, framework executes
optimized_prompt = dspy_optimizer.optimize(signature)
request = format_api_request(url, model, optimized_prompt)
response = make_api_call(request)
        """)
    
    print()


if __name__ == "__main__":
    demonstrate_integration()

