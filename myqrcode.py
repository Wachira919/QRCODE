import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


myQrCode = qrcode.make('https://jacobnarayan.com/blogs/create-a-qr-code-with-7-lines-of-python')
myQrCode.save("Image.jpg")

b = decode(Image.open('myQrCode'))
print(b[0].data.decode("ascii"))