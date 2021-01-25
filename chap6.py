import numpy as np
import argparse
import imutils
import cv2

#Tranxlation
'''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
'''
image = cv2.imread("/home/vikas/Documents/mast.jpeg")
'''
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
'''

def translate(image,x,y):
	M= np.float32([1,0,x],[0,1,y])
	shifte = cv2.warpAffine(image,M,image.shape[1],image.shape[0])
	return shifte
shifted1 = imutils.translate(image,40,100)
cv2.imshow("shifted Down",shifted1)



#Rotation of image
(h,w) = image.shape[:2]
center = (w//2, h//2)

A = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image,A,(w,h))
cv2.imshow("Rotated by 45 Degree",rotated)

A = cv2.getRotationMatrix2D(center,-90,1.0)
rotated = cv2.warpAffine(image,A,(w,h))
cv2.imshow("ratated bye -90 degrees",rotated)

rot = imutils.rotate(image,180)
cv2.imshow("rotated by 180 degree",rot)

cv2.waitKey(0)



