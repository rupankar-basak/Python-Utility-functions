import qrcode
import random

def generate_QR(URL):
    qr_img = qrcode.make(URL)
    fileNum = str(random.randint(0, 999999))
    qr_img.save("QR_" + fileNum + ".jpg")
    print('QR Code for your link has been generated and saved successfully.')

link = input("Please enter a text or URL: ")
generate_QR(link)
