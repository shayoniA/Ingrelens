from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from backend.db import get_info, save_info
import os
import re
import requests
from backend.ocr import extract_text
from backend.classify import classify_ingredient

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/mainpage')
def mainpage():
    return render_template("mainpage.html")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(path)

    # OCR extract
    raw_text = extract_text(path)
    raw_text = re.sub(r'\bingredients?\b', '', raw_text, flags=re.IGNORECASE)  # Removing starting word 'Ingredients' or similar
    raw_text = re.sub(r"[^\w\s,.\-]", '', raw_text)  # Removing all punctuations except ,.-
    print("\n📄 OCR Raw Text:\n", raw_text)

    # Ingredient list
    ingredients = [i.strip() for i in raw_text.replace("\n", " ").split(",") if i.strip()]
    print("\n🧪 Extracted Ingredients List:\n", ingredients)

    result = {
        # "ingredients": [],
        "categories": {
            "bad": [],
            "good": []
        },
        "total_score": 0
    }

    resultjson = classify_ingredient(ingredients)
    bad_key, bad_items = list(resultjson.items())[0]
    good_key, good_items = list(resultjson.items())[1]
    for bading in bad_items:
        result["categories"]["bad"].append(bading)
    for gooding in good_items:
        result["categories"]["good"].append(gooding)
    result["total_score"] = (len(good_items)*5)-(len(bad_items)*5)

    return jsonify(result)
    

@app.route('/explain_ingredient', methods=['POST'])
def explain_ingredient():
    # from ollama import chat
    import time
    data = request.json
    ingredient = data.get('ingredient', '').strip()

    if not ingredient:
        return jsonify({"error": "No ingredient provided"}), 400

    cached_info = get_info(ingredient)
    if cached_info:
        def stream_cached():
            for line in cached_info.splitlines(keepends=True):
                yield line
                time.sleep(0.02)
        return Response(stream_with_context(stream_cached()), content_type='text/plain')

    # If not cached — generate with Ollama
    prompt = f"""
    You are a certified skin-health expert. Provide the **positive and negative impacts** of the ingredient '{ingredient}' on **skin and overall health**, written in well-structured **Markdown**.
    Use this format:

    ### 🔬 Ingredient: <name>

    #### ✅ Positive Impacts: (maximum of 2 points)
    - Point 1
    - Point 2

    #### ⚠️ Negative Impacts: (maximum of 2 points)
    - Point 1
    - Point 2
    """

    OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434")

    def generate_and_store():
        full_text = ""
        try:
            with requests.post(
                f"{OLLAMA_API_URL}/api/chat",
                json={"model": "mistral", "messages": [{"role": "user", "content": prompt}], "stream": True},
                stream=True,
            ) as response:
                for line in response.iter_lines():
                    if line:
                        text = line.decode('utf-8')
                        full_text += text
                        yield text
                        time.sleep(0.02)
        finally:
            if full_text.strip():
                save_info(ingredient, full_text)

    return Response(stream_with_context(generate_and_store()), content_type='text/plain')
