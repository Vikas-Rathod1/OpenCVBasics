#DRAWING OF SHAPES ON IMAGE
import cv2
import numpy as np
#image = cv2.imread("/home/vikas/Documents/mast.jpeg")
#cv2.imshow(" original image",image)
#cv2.waitKey(0)

canvs = np.zeros((300,300,3),dtype = 'uint8')
cv2.imshow("created image",canvs)

#Green line

green = (0,255,0)
#var = B,G,R not R,G,B
cv2.line(canvs,(0,0),(200,200),green,2)
#drawning of ln start point,end point,color,thikness
cv2.imshow("green_line",canvs)
#module .show,name of display,img that you want to work on


'''#Red line
red = (0,0,255)
cv2.line(canvs,(300,0),(0,300),red,3)
cv2.imshow("red_line",canvs)

#Drawing of rectangle on image
cv2.rectangle(canvs,(10,10),(50,50),red)
cv2.imshow("rectangle",canvs)

cv2.rectangle(canvs,(30,100),(100,125),(255,0,0),4)
cv2.imshow('rectangle',canvs)

cv2.rectangle(canvs,(100,20),(20,160),red,-1)
cv2.imshow("-ve_recta",canvs)
'''
#drawing a circle
(center_x,center_y)=(canvs.shape[1]//2,canvs.shape[0]//2)
white = (255,255,255)

for r in range(0,175,25):
	cv2.circle(canvs,(center_x,center_y),r,white)

cv2.imshow("canvs_circle",canvs)

#Abstract Drawing
for x in range(0,25):
	radius =np.random.randint(5,high=200)
	color = np.random.randint(0,high = 256,size = (3,)).tolist()
	pt = np.random.randint(0,high=300,size=(2,))
	cv2.circle(canvs,tuple(pt),radius,color,-1)


cv2.imshow("Abstract_crcl",canvs)
cv2.waitKey(0)
