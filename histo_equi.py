import numpy as np 
import cv2

image = cv2.imread("/home/vikas/DATASCIENCE/Bookpractice/img.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

cv2.imshow(" Hist equalization",np.hstack([image,eq]))
cv2.waitKey(0)