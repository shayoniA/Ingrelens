from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(image_path):
    try:
        image = Image.open(image_path).convert("L")
        text = pytesseract.image_to_string(image)
        print(f"\n📸 Processed Image Mode: {image.mode}, Size: {image.size}")
        return text
    except Exception as e:
        print("❌ OCR Error:", e)
        return ""
