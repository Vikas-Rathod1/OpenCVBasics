import numpy as np 
import cv2

image = cv2.imread("/home/vikas/Desktop/1.jpg")
cv2.imshow("origianl_image",image)

image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("Image",image)

(T,Thresh) = cv2.threshold(blurred,155,255,cv2.THRESH_BINARY)
cv2.imshow("tHRESOLD_bINARY",Thresh)

(T, threshInv) = cv2.threshold(blurred, 100, 200, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

cv2.imshow("Rose", cv2.bitwise_and(image, image, mask =threshInv))
cv2.waitKey(0)
'''
#Adaptive threasholding
#it is use to calc te smaller region of the img 

Thresh = cv2.adaptiveThreshold(iamge, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 150, 3)
cv2.imshow("Mean Thresh", thresh)

thresh = cv2.adaptiveThreshold(iamge, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 200, 5)
cv2.imshow("Gaussian Thresh", thresh)
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  
'''



