import ollama
import json

CATEGORY_SCORES = {
    'bad': -5,
    'good': 5,
}

def classify_ingredient(ingredients):
    prompt = f"""
    You are a certified skin-care expert. Evaluate all ingredients in this list '{ingredients}' and respond in **JSON format only** with two fields:
    
    1. "bad": List of all ingredients that are harmful for the skin.
    2. "good": List of all ingredients that are beneficial or good or neutral to the skin.

    Only return the JSON — do not include any explanation, heading, or extra text outside the JSON.
    """

    try:
        response = ollama.chat(model='mistral', messages=[{"role": "user", "content": prompt}])
        answer = response['message']['content'].strip()
        result = json.loads(answer)
        print(f"🧠 LLM Response: {result}")
        return result
    
    except Exception as e:
        print(f"❌ Error during classification: {str(e)}")
        return {"bad": [], "good": []}