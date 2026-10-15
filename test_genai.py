import os
from google import genai

print("Script started")

# Read API key
api_key = os.getenv("GEMINI_API_KEY")
print("API key found:", bool(api_key))

if not api_key:
    print("ERROR: API key not found")
    exit()

# Create Gemini client
client = genai.Client(api_key=api_key)
print("Client created")

# Test prompt
prompt = """
Classify the following payload:

<script>alert(1)</script>

Is this:
- XSS
- SQL Injection
- Command Injection
- Normal

Answer in one sentence.
"""

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=prompt
)

print("\nGemini response:")
print(response.text)


