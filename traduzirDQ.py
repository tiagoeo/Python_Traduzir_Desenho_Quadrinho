import pytesseract
import cv2
from googletrans import Translator

tr = Translator()
caminho_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Carregar um quadrinho para traduzir
imagem = cv2.imread("quadrinho.png")

# Extrair o texto original do balão de quadrinho
pytesseract.pytesseract.tesseract_cmd = caminho_tesseract

texto_original_capturado = pytesseract.image_to_string(imagem, lang="eng")

# Processar texto detectado para português
google_translator = tr.translate(texto_original_capturado, dest="pt")

texto_traduzido = google_translator.text

# Saída
print(f"\n ------------- \n O texto original do quadrinho foi: \n ------------- \n {texto_original_capturado} \n ------------- \n Sua tradução em português é: \n ------------- \n {texto_traduzido}")