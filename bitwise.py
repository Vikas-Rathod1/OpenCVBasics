import numpy as np 
import cv2


'''
rectangle = np.zeros((300,300),dtype = "uint8")
cv2.rectangle(rectangle,(25,25),(275,275),255,-1)
cv2.imshow("Rectangle",rectangle)

circle = np.zeros((300,300),dtype = "uint8")
cv2.circle(circle,(150,150),150,255,1)
cv2.imshow("Circle",circle)
cv2.waitKey(0)



bitwiseAnd = cv2.bitwise_and(rectangle,circle)
cv2.imshow("AND",bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle,circle)
cv2.imshow("OR",bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow("XOR",bitwiseXor)
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(rectangle,circle)
cv2.imshow("bitwiseNot",bitwiseNot)
cv2.waitKey(0)
'''

# MASKING  ON THE IMAGE

image = cv2.imread("/home/vikas/Documents/mast.jpeg")

'''mask = np.zeros(image.shape[:2],dtype= "uint8")
(cx,cy)= (image.shape[1]//2,image.shape[0]//2)
cv2.rectangle(mask,(cx-75,cy-75),(cx+75,cy+75),255,-1)
cv2.imshow("Mask",mask)

masked = cv2.bitwise_and(image,image,mask = mask)
cv2.imshow("Mask applied to the Image",masked)
'''

(cx,cy)= (image.shape[1]//2,image.shape[0]//2)
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (cx, cy), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)