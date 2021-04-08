from cv2 import cv2
import pytesseract
import docx
from app import app
from flask import abort

pytesseract.pytesseract.tesseract_cmd = "D:\\OpenCV\\Helper.uz\\Tesseract-OCR\\tesseract.exe"

@app.route('/check/<string:imagename>')
def check(imagename):
    try:
        image_path = "uploads/"  + imagename
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        data = str(pytesseract.image_to_string(img))
        data = data[:-1]
        return data
    except :
        abort(404)
