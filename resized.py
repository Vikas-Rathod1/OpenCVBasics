#resizing the image
import numpy as np
import imutils
import cv2

image = cv2.imread("/home/vikas/Documents/mast.jpeg")
cv2.imshow("Original image",image)

#r = 500.0/image.shape[1]
r = 150.0/image.shape[0]
dim = (int(image.shape[0]*r),50)

resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
cv2.imshow("resized width",resized)

resized = imutils.resize(image,width = 1000)
cv2.imshow("Resized via function",resized)

resized  = imutils.resize(image,height  = 50)
cv2.imshow("resized height",resized)
cv2.waitKey(0) 


#USING FUNCTION

def resize(image,width = None,height = None,inter = cv2.INTER_AREA):
	dim = None
	(h,w) = image.shape[:2]
	print("h is",h)
	print("w is ",w)
	if width is None  and height is None:
		return image
	if width is None:
		r = height/float(h)
		dim = (int(w*r),height)
	else:
		r = width/float(w)
		dim = (width,int(h*r))
	resized = cv2.resize(image,dim,interpolation =inter)
	return resized
cv2.imshow("function",)