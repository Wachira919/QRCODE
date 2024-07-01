import qrcode

yourQr = input("Enter anything you want to become a qrcode: ")

image = qrcode.make(yourQr)
image.save("Image.png")