import numpy as np
import cv2
 
image  =  cv2.imread("/home/vikas/DATASCIENCE/Bookpractice/img.jpg")
cv2.imshow("original image",image)
cv2.waitKey(0)

(B,G,R)= cv2.split(image)
'''
cv2.imshow("Red",R)
cv2.imshow("Green",G)
cv2.imshow("Blue",B)
cv2.waitKey(0)


merged = cv2.merge([B,G,R])
cv2.imshow("Merged",merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


'''#MERGING CHANNELS
zeros = np.zeros(image.shape[:2],dtype = "uint8")
cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.waitKey(0)'''

# COLOR SPACE
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY",gray)

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)

lab = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
cv2.imshow("LAB",lab)
cv2.waitKey(0)