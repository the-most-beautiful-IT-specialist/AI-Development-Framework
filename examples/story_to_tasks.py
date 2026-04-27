import json
import time

def run_demo():
    print("=== AI Framework: Demo Mode ===")
    
    # 1. Input Data (User Story)
    user_story = "As a user, I want to reset my password via email."
    print(f"\n[INPUT] Product Manager provides User Story: \n'{user_story}'\n")
    
    # 2. Mock API call to our llm_client.py module
    print("[PROCESSING] Sending data to LLM via strict API contract...")
    time.sleep(2) # 2-second pause for realism
    
    # 3. Mock Response (simulating a perfect JSON output from AI)
    mock_json_response = {
        "tasks": [
            {"title": "Create 'Forgot Password' UI component", "hours": 2},
            {"title": "Implement reset token generation in DB", "hours": 3},
            {"title": "Configure SMTP service for email delivery", "hours": 2},
            {"title": "Create API endpoint for token validation", "hours": 4}
        ]
    }
    
    # 4. Output Result
    print("\n[OUTPUT] --- Tasks successfully generated (Strict JSON) ---")
    for task in mock_json_response['tasks']:
        print(f"[ ] {task['title']} (Estimated: {task['hours']}h)")

if __name__ == "__main__":
    run_demo()
