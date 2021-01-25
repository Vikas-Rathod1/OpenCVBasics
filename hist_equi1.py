
from matplotlib import pyplot as plt 
import numpy as np 
import cv2



def plot_histogram(image, title, mask = None):

	chans = cv2.split(image)
	colors = ("b", "g", "r")
	plt.figure()
	plt.title(title)
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")
	
	for (chan, color) in zip(chans, colors):
		hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
		plt.plot(hist, color = color)
		plt.xlim([0, 256])
	image = cv2.imread("/home/vikas/DATASCIENCE/Bookpractice/img.jpg")
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")
	cv2.imshow("Original", image)
plot_histogram(image, "Histogram for Original Image")
