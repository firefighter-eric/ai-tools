import os

import pytesseract
from PIL import Image


class OCR:
    def __init__(self):
        tesseract_path = r"C:\Program Files\Tesseract-OCR"
        if tesseract_path not in os.environ['PATH']:
            os.environ['PATH'] += os.pathsep + tesseract_path
        print(os.environ['PATH'])

    def __call__(self, img_path) -> str:
        string = pytesseract.image_to_string(Image.open(img_path), lang='chi_sim')
        return string


# tesseract_path = r"C:\Program Files\Tesseract-OCR"
# if tesseract_path not in os.environ['PATH']:
#     os.environ['PATH'] += os.pathsep + tesseract_path
# languages = pytesseract.get_languages()

if __name__ == '__main__':
    ocr = OCR()
    print(ocr('data/screenshot.png'))