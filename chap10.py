import numpy as np 
import cv2

image = cv2.imread("/home/vikas/Documents/IMG1.jpg")
cv2.imshow("origianl_image",image)

img  = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image",image)

#Laplacian method
lap =cv2.Laplacian(img ,cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)
