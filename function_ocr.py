# By Julio Daniel 12 November 2020
try:
    from PIL import Image
except ImportError:
    from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

# print(ocr_core('tess_image1.png'))