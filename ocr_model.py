import sys
import pytesseract
import cv2

def image_to_text(filename):
    img_cv = cv2.imread(filename)
    arabic_text = pytesseract.image_to_string(img_cv, lang='ara', config=".")
    return arabic_text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ocr_model.py <image_path>")
    else:
        image_path = sys.argv[1]
        ahmed = image_to_text(image_path)
        print(ahmed)
