from src.llm_client import AIClientFramework

def run_example():
    framework = AIClientFramework()
    
    # Input
    user_story = "As a user, I want to reset my password via email."
    
    system_instruction = """
    Extract development tasks from User Story. 
    Output JSON strictly in this schema: {"tasks": [{"title": "string", "hours": "int"}]}
    """
    
    # Processing
    try:
        result = framework.get_strict_json(user_story, system_instruction)
        
        # Output
        print("--- Successful task generation ---")
        for task in result.get('tasks', []):
            print(f"[ ] {task['title']} ({task['hours']}h)")
            
    except Exception as e:
        print(f"Guardrails error: {e}")

if __name__ == "__main__":
    run_example()
