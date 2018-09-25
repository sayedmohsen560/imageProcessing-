from PIL import Image
import pytesseract



def extract_text_from_image (image_file):
    image_to_text = Image.open(image_file)
    text = pytesseract.image_to_string(image=image_to_text, lang='eng')
    return text


