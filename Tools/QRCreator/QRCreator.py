import qrcode
from PIL import Image

def QRCreator(url):
    img = qrcode.make(url)
    img.show()

url = input("Introduce la URL: ")
QRCreator(url)
