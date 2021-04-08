from qrcode import *
img = qrcode.make ("Baby jpg1 ate 20 biscuits today")
img.save ("jpg1.jpg")
import cv2
d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode (cv2.imread ("jpg1.jpg"))
print(val)