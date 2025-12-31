# Ingrelens

Ingrelens is a web app that analyzes cosmetic product ingredients directly from images and explains their impact on skin health. It categorizes ingredients as good or bad and generates an overall health score for the product, enabling easy comparison between products (higher score indicates better suitability).

**Deployed Website:** https://ingrelens1.onrender.com  
**Demo Video:** https://drive.google.com/file/d/1cjAATwds1UuHmvSKC2Dn4ooxX58_pds4/view  

---

## How to Run

### Create and activate a virtual environment
```
python -m venv venv
venv\Scripts\activate
```

### Install dependencies
```
pip install -r requirements.txt
```

### Install Tesseract OCR
Download and install Tesseract OCR and add its installation path to your system PATH.

### Environment variables
Create a `.env` file containing:
```
GOOGLE_API_KEY=your_api_key
MONGO_URI=your_mongo_uri
```
Make sure your Gemini API key has access to the `gemini-2.5-flash` model.

### Run the application
```
python run.py
```

---

## Key Features

1. **Image-based ingredient extraction**  
   Upload a cosmetic product image and automatically extract ingredient text using OCR.

2. **AI-powered ingredient classification**  
   Ingredients are classified as good or bad using LLMs instead of static rule-based systems.

3. **Dynamic health scoring**  
   A health score is generated based on the overall ingredient composition.

4. **Click-to-explain ingredients**  
   Click on any ingredient to receive streamed explanations describing both positive and negative effects, rendered in Markdown.

5. **Cached explanations**  
   Previously explained ingredients are stored to reduce latency and minimize API calls.

6. **Clean and responsive UI**  
   Smooth animations, loaders, and an intuitive interface for better user experience.

---

## Tech Stack

1. **Frontend** – HTML, CSS, JavaScript (React.js, Marked.js)
2. **Backend** – Python, Flask
3. **AI & ML** – Google Gemini API (LLM-powered), OCR for image-based text extraction
4. **Database** – MongoDB (ingredient explanation caching)
5. **Deployment** – Render

---

## Why I Built Ingrelens

Most ingredient-checking applications rely on static databases and do not adapt to context or combinations of ingredients. Being interested in AI, LLMs, and real-world problem solving, I wanted to build a system that:

- Uses AI reasoning instead of simple database lookups  
- Explains ingredients dynamically on demand  
- Enables meaningful comparison between cosmetic products  

---

## Future Improvements

Ingredient sensitivity personalization based on user profile and usage history

---

## Author

**Sayani Adhikary**  
