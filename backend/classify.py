from dotenv import load_dotenv
load_dotenv()
import os
import json
import re
from google import genai
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

CATEGORY_SCORES = {
    'bad': -5,
    'good': 5,
}

def classify_ingredient(ingredients):
    prompt = f"""
    You are a certified skin-care expert. Evaluate all ingredients in this list '{ingredients}' and respond in **JSON format ONLY** with two fields:
    
    1. "bad": List of all ingredients that are harmful for the skin.
    2. "good": List of all ingredients that are beneficial or good or neutral to the skin.

    ONLY return the JSON — do not include any explanation, heading, or extra text outside the JSON. The format should be this:
    {{
    "bad": [],
    "good": []
    }}

    Rules:
    - No markdown
    - No explanations
    - No text outside JSON
    """

    # try:
    #     response = client.models.generate_content(
    #         model="models/gemini-2.5-flash",
    #         contents=prompt
    #     )
    #     text = response.text.strip()
    #     if "```" in text:
    #         text = text.split("```")[1].strip()
    #     result = json.loads(text)
    #     print(f"🧠 LLM Response: {result}")
    #     return result
    
    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )
        raw_text = response.text or ""
        print("🧠 Gemini raw response:\n", raw_text)
        match = re.search(r'\{[\s\S]*\}', raw_text)
        if not match:
            raise ValueError("No valid JSON found in Gemini response")
        result = json.loads(match.group())
        return result
    
    except Exception as e:
        print(f"❌ Error during classification: {str(e)}")
        return {"bad": [], "good": []}
