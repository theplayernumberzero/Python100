import pyqrcode

url = input("Enter url which you want to convert qr code: ")

qr_code = pyqrcode.create(url)
qr_code.svg("./QR_codes/qrcode.svg", scale=5)