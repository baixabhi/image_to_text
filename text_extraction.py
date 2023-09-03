from PIL import Image
import pytesseract  # Import the pytesseract module

class ImageReader:
    def __init__(self, tesseract_path):
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    def extract_text(self, image_path):
        return pytesseract.image_to_string(Image.open(image_path))

if __name__ == '__main__':
    tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image_path = r'C:\Users\abhij\OneDrive\Desktop\Image_extract\newpoem.png'
    extracted_text = ImageReader(tesseract_path).extract_text(image_path)
    print(extracted_text)
