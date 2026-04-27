import os
import json
from openai import OpenAI
import anthropic

class AIClientFramework:
    """A universal framework for securely calling LLM"""
    
    def __init__(self):
        # Safe initialization of keys from the environment
        self.openai_key = os.environ.get("OPENAI_API_KEY")
        self.anthropic_key = os.environ.get("ANTHROPIC_API_KEY")

    def get_strict_json(self, user_text: str, schema_prompt: str) -> dict:
        """API contract for strict JSON (OpenAI)"""
        client = OpenAI(api_key=self.openai_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            temperature=0.0, # 0 is required for accurate data
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": schema_prompt},
                {"role": "user", "content": user_text}
            ]
        )
        return json.loads(response.choices[0].message.content)

    def analyze_code_safe(self, code_snippet: str, rules: str) -> str:
        """API contract for code review (Anthropic Claude)"""
        client = anthropic.Anthropic(api_key=self.anthropic_key)
        message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=2000,
            temperature=0.2,
            messages=[
                {"role": "user", "content": f"{rules}\n\n<code_block>\n{code_snippet}\n</code_block>"}
            ]
        )
        return message.content[0].text
