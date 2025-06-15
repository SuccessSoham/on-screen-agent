# agent/screen_analyzer.py
from PIL import Image
import pytesseract
import pyautogui

def capture_screen():
    # Capture the current screen
    image = pyautogui.screenshot()
    return image

def run_ocr(image):
    # Convert image to string using Tesseract
    text = pytesseract.image_to_string(image)
    return text

# (Optional) Advanced parsing could include OpenCV techniques or integration with VLM
def analyze_ui(image):
    # Placeholder for VLM or UI element detection logic
    elements = {"buttons": [], "text_fields": []}
    return elements