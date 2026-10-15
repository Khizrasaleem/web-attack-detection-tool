import os
import json
import re
from google import genai

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def detect_attack(payload: str) -> dict:
    prompt = f"""
You are a web security expert.

Analyze the input and classify it strictly as one of:
XSS, SQL Injection, Command Injection, LFI, RFI, Normal

Respond ONLY with valid JSON.
Do NOT use markdown or backticks.

Format:
{{
  "attack_type": "",
  "confidence": "",
  "reason": ""
}}

Input:
{payload}
"""

    response = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    text = response.text.strip()

    # Remove markdown if Gemini still adds it
    text = re.sub(r"```json|```", "", text).strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
            "attack_type": "Unknown",
            "confidence": "Low",
            "reason": "Invalid model response"
        }

