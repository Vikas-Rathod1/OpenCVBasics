from __future__ import print_function
import argparse
import cv2

image = cv2.imread("/home/vikas/Documents/mast.jpeg")
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))
cv2.imshow("Original Image", image)

#accessing and manipulating pixels
(b,g,r)= image[0,0]
print("Pixel at (0,0) - Red:{},Green:{},Blue:{}".format(r,g,b))
image[0,0]=(0,0,255)
(b,g,r)=image[0,0]
print("Pixel at (0,0) - Red:{},Green:{},Blue:{}".format(r,g,b))

corner = image[10:100,10:100]
cv2.imshow("corner",corner)

#image[100:300,100:300]=(0 ,0,0) #black rectangle on image
#cv2.imshow("Update Image",image)

#Accessing and manipulating pixels
#Indexes



#cv2.imwrite("newimage.jpg",image)
cv2.waitKey(0)