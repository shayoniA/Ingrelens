**Ingrelens** <br>
A web app that analyzes cosmetic product ingredients directly from images and explains their impact on skin health. It categorizes ingredients as good or bad, and gives an overall health score to the product, enabling easy comparison between products (the greater the better).
**Deployed Website**: [https://ingrelens1.onrender.com] <br>
**Demo Video**: [https://<your-demo-video-link-here>](https://drive.google.com/file/d/1cjAATwds1UuHmvSKC2Dn4ooxX58_pds4/view) <br>
<br>
<br>
**How to Run**: <br>
Create & activate a Virtual Environment:  *python -m venv venv*  -->  *venv\Scripts\activate*
Install Dependencies:  *pip install -r requirements.txt*
Install Tesseract OCR:  Download and install Tesseract, and add installation path to your system PATH.
Set Up Environment Variables:  Create an *.env* file containing *GOOGLE_API_KEY* and *MONGO_URI* (Make sure your Gemini API key has access to gemini-2.5-flash model).
Run the App:  *python run.py*

**Key Features**:
1. **Image-based ingredient extraction** - Upload a product image and automatically extract ingredient text using OCR.
2. **AI-powered ingredient classification** - Ingredients are classified as good and bad, using LLMs instead of a static rule-based system.
3. **Dynamic health scoring** - A health score is generated based on ingredient composition.
4. **Click-to-explain ingredients** - Click on any ingredient to get streamed explanations, including their positive and negative impacts, rendered in markdown.
5. **Cached explanations** - Previously explained ingredients are stored to reduce latency and API calls.
6. **Clean and responsive UI** - Smooth animations, loaders, and intuitive interface for better UX.

**Tech Stack**:
1. Frontend - HTML, CSS, JavaScript (React.js, Marked.js)
2. Backend - Python, Flask
3. AI & ML - Google Gemini API (LLM-powered), OCR (computer vision) for text extraction from images.
4. Database - MongoDB (ingredient explanation caching)
5. Deployment - Render

**Why I Built Ingrelens**:  Most ingredient-checking apps Rely on static databases, and Don’t adapt to context/combinations of ingredients.
Being interested in AI, LLMs, and real-world applications, I wanted to build something that:
- Uses AI reasoning, not just DB-lookups
- Explains ingredients on demand
- Enables comparison between products for better decision making

**Future Improvement**:  Ingredient sensitivity personalization based on user profile & history.


Author
**Sayani Adhikary**
(B.Tech CSE, IIIT Guwahati)
