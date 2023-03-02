mport pyqrcode

__version__ = 1

try:
    url = "https://pixelcoblog.com"
    qr_code = pyqrcode.create(url)
    qr_code.png("pixelco.png", scale=6)
except ValueError:
    print("An error has occurred")
    
