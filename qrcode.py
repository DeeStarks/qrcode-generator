import os
import pyqrcode
import datetime

class QR_Gen:
    def __init__(self, link):
        self.qr_image = self.qr_generator(link)

    @staticmethod
    def qr_generator(text):
        qr_code = pyqrcode.create(text)
        now = datetime.datetime.now()
        filename = ''
        url = text.replace('/', '_')
        url_text = url.split(".")
        if "https://www" in text or "www" in text:
            for keyword in url_text:
                if keyword != "https:__www" and keyword != "www":
                    filename += keyword + "_"
        else:
            filename = "qr_img"
        name = f"qrcode_images/{filename}{now.strftime('%d%m%Y%H%M%S')}.png"
        qr_code.png(name, scale=20)
        os.system(f"start {name}")

if __name__ == "__main__":
    QR_Gen(input("Enter URL to generate QR Code (Powered by DeeStarks): "))