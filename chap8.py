import numpy as np 
import cv2

image = cv2.imread("/home/vikas/Documents/mast.jpg")
cv2.imshow("original_image",image)
#cv2.waitKey(0)
'''
#average blured image
blurred = np.hstack([
cv2.blur(image, (3, 3)),cv2.blur(image, (7, 7)),cv2.blur(image, (10, 10))])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

#gaussian blured image
G_blurred = np.hstack([
cv2.GaussianBlur(image, (3, 3),0),cv2.GaussianBlur(image, (7, 7),0),cv2.GaussianBlur(image, (9, 9),0)])
cv2.imshow("Gaussian", G_blurred)
cv2.waitKey(0)


#Median blured
blurred = np.hstack([
cv2.medianBlur(image, 3),
cv2.medianBlur(image, 5),
cv2.medianBlur(image, 7)])
cv2.imshow("Median", blurred)
cv2.waitKey(0)
'''

blurred = np.hstack([
cv2.bilateralFilter(image, 5, 21, 21),
cv2.bilateralFilter(image, 7, 31, 31),
cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)