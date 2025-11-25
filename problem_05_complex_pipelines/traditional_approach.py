"""
Problem 5: Complex Pipelines are Hard to Build and Optimize

Traditional approach: Manual pipeline construction
"""

def traditional_pipeline_approach():
    """Demonstrate problems with manual pipeline building"""
    
    print("=" * 70)
    print("PROBLEM 5: Complex Pipelines are Hard to Build and Optimize")
    print("=" * 70)
    print()
    
    # Problem: Manual composition
    print("🔴 Problem: Manual composition")
    print("-" * 70)
    
    def traditional_rag_pipeline(question):
        """Traditional RAG pipeline - manual construction"""
        # Step 1: Retrieve
        print("Step 1: Retrieve documents")
        docs = ["Doc 1: AI is...", "Doc 2: Machine learning..."]  # Simulated
        
        # Step 2: Format prompt manually
        print("Step 2: Format prompt manually")
        context = "\n".join(docs)
        prompt = f"""Context: {context}

Question: {question}

Answer:"""
        
        # Step 3: Generate
        print("Step 3: Generate answer")
        answer = f"Answer to: {question}"  # Simulated
        
        return answer
    
    print("❌ Traditional RAG pipeline:")
    result = traditional_rag_pipeline("What is AI?")
    print(f"Result: {result}")
    print()
    print("Problems:")
    print("  - Manual step-by-step construction")
    print("  - Hard-coded prompt format")
    print("  - Tightly coupled components")
    print("  - Hard to modify or optimize")
    print()
    
    # Problem: Hard to optimize
    print("🔴 Problem: Hard to optimize")
    print("-" * 70)
    print("To optimize the pipeline, you need to:")
    print("  1. Optimize retrieval? → Try different k values")
    print("  2. Optimize prompt format? → Try different formats")
    print("  3. Optimize few-shot examples? → Try different examples")
    print("  4. Optimize model parameters? → Try different settings")
    print()
    print("  → How do you test all combinations?")
    print("  → Which component should you optimize first?")
    print("  → How do you know if improvement is from retrieval or prompt?")
    print()
    
    # Problem: No modularity
    print("🔴 Problem: No modularity")
    print("-" * 70)
    print("Components are tightly coupled:")
    print("  - Retrieval code mixed with prompt formatting")
    print("  - Prompt formatting mixed with generation")
    print("  - Hard to swap components")
    print("  - Hard to test components separately")
    print()
    
    # Problem: Testing complexity
    print("🔴 Problem: Testing complexity")
    print("-" * 70)
    print("To test the pipeline:")
    print("  - Test retrieval separately")
    print("  - Test prompt formatting separately")
    print("  - Test generation separately")
    print("  - Test entire pipeline")
    print("  - Hope components work together")
    print()


if __name__ == "__main__":
    traditional_pipeline_approach()

