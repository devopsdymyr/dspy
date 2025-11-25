"""
Problem 4: Code Doesn't Work Across Different Models

Traditional approach: Model-specific code
"""

def traditional_model_specific_approach():
    """Demonstrate problems with model-specific code"""
    
    print("=" * 70)
    print("PROBLEM 4: Code Doesn't Work Across Different Models")
    print("=" * 70)
    print()
    
    # Problem: Model-specific prompts
    print("🔴 Problem: Model-specific prompts")
    print("-" * 70)
    
    def get_prompt_for_model(question, model):
        """Different prompts for different models"""
        if model == "gpt-3.5":
            return f"Answer: {question}"
        elif model == "gpt-4":
            return f"Please provide an answer: {question}"
        elif model == "claude":
            return f"Question: {question}\nAnswer:"
        elif model == "llama":
            return f"Q: {question}\nA:"
        else:
            return f"{question}"
    
    models = ["gpt-3.5", "gpt-4", "claude", "llama"]
    question = "What is AI?"
    
    print("❌ Model-specific code:")
    for model in models:
        prompt = get_prompt_for_model(question, model)
        print(f"  {model}: {prompt}")
    print()
    print("Problems:")
    print("  - Different code for each model")
    print("  - Hard to maintain (update each one)")
    print("  - Can't reuse code")
    print()
    
    # Problem: Model-specific API calls
    print("🔴 Problem: Model-specific API calls")
    print("-" * 70)
    
    def call_model_api(prompt, model):
        """Different API calls for different models"""
        if model == "gpt-3.5" or model == "gpt-4":
            # OpenAI format
            return {
                "model": model,
                "messages": [{"role": "user", "content": prompt}]
            }
        elif model == "claude":
            # Anthropic format
            return {
                "model": model,
                "messages": [{"role": "user", "content": prompt}]
            }
        elif model == "llama":
            # Ollama format
            return {
                "model": model,
                "prompt": prompt
            }
    
    print("❌ Different API formats:")
    for model in models:
        api_call = call_model_api(question, model)
        print(f"  {model}: {api_call}")
    print()
    print("Problems:")
    print("  - Different API formats")
    print("  - Different response parsing")
    print("  - Code duplication")
    print()
    
    # Problem: Maintenance nightmare
    print("🔴 Problem: Maintenance nightmare")
    print("-" * 70)
    print("To add a new model:")
    print("  1. Write new prompt format")
    print("  2. Write new API call code")
    print("  3. Write new response parser")
    print("  4. Test everything")
    print("  5. Update all existing code")
    print()
    print("To improve prompts:")
    print("  - Update for GPT-3.5")
    print("  - Update for GPT-4")
    print("  - Update for Claude")
    print("  - Update for Llama")
    print("  - Test each one separately")
    print()


if __name__ == "__main__":
    traditional_model_specific_approach()

