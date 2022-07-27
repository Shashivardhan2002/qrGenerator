import qrcode
import cv2

# Converting into Qrcode
data = input('Enter what do you want to convert to qrcode')
img = qrcode.make(data)
img.save('MyQrcode1.png')

# Reading an Qrcode
img = cv2.imread('MyQrcode1.png')
detector = cv2.QRCodeDetector()
bbox = detector.detectAndDecode(img)
if bbox is not None:
    print("Qr Code data: ",data)
