#resizing the image
import numpy as np
import imutils
import cv2

image = cv2.imread("/home/vikas/Documents/mast.jpeg")
cv2.imshow("Original image",image)

r = 150.0/image.shape[1]
dim = (150,int(image.shape[0]*r))

resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
cv2.imshow("resized WIDTH",resized)
cv2.waitKey(0)