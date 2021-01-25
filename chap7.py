#calcHist(images,channels,mask,histsize,ranges)

import numpy as np
import cv2
import matplotlib.pyplot as plt

image= cv2.imread("/home/vikas/DATASCIENCE/Bookpractice/img.jpg")
'''
#img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("original image",image)
cv2.waitKey(0)
'''

'''
#histogram for img
hist = cv2.calcHist([img],[0],None,[256],[0,256])
#[0] is bcz our gray scale has only oone channel, 
#no mask nd have 256 bins, and the range is 0-256
plt.figure()
plt.title("Grayscal_Histigram")
plt.xlabel("Bins")
plt.ylabel("#  no of pixel")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)
'''
#histogram of each channels of image
chans = cv2.split(image)
'''colors = ("b","g","r")
plt.figure()
plt.title("Flatten_color_Histogram")

for (chan,color) in zip(chans,colors):
	hist = cv2.calcHist([chan],[0],None,[256],[0,256])
	plt.plot(hist,color = color)
	plt.xlim([0,256])
plt.xlabel("Bins")
plt.ylabel("# no of Pixels")
plt.show()
'''

'''
fig = plt.figure()

ax = fig.add_subplot(131)
hist=cv2.calcHist([chans[1],chans[0]],[0,1],None,[32,32],[0,256,0,256])
'''



fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None,
[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None,
[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None,
[32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))