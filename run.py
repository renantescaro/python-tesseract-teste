import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

image = cv2.imread('assets/1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plate_text = pytesseract.image_to_string(gray)

print(f'plate_text:{plate_text}')
