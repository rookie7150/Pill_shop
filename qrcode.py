import pyqrcode
data = 'pill_2,pill_3'
qr = pyqrcode.create(data)
qr.png("qr_code.png", scale=6)