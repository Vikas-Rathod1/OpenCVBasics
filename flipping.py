import cv2
import numpy as np 


image = cv2.imread("/home/vikas/Documents/mast.jpeg")
cv2.imshow("original image",image)


flip = cv2.flip(image,1)
cv2.imshow("Flipping Horizontal",flip)


fllip = cv2.flip(image,0)
cv2.imshow("flip vertically",fllip)

flipp = cv2.flip(image,-1)
cv2.imshow("Flipping v and h",flipp)
cv2.waitKey(0)




#Cropping image 


cropped = image[30:120,240:335]
cv2.imshow("T-Rex Face",cropped)
cv2.waitKey(0)

# Aritmatic operation on image
print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8
([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8
([100]))))

print("wrap around: {}".format(np.uint8([200]) + np.uint8([100]))
)
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

M = np.ones(image.shape,dtype = "uint8")*100
added = cv2.add(image,M)
cv2.imshow("Added",added) 

M = np.ones(image.shape,dtype = "uint8")*50
subtracted = cv2.subtract(image,M)
cv2.imshow("subtract",subtracted)
cv2.waitKey(0)