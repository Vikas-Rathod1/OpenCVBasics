import numpy as np
import cv2
class CoverDes:
	def __init__(self,useSIFT=False):
		self.useSIFT=useSIFT
	def describe(self,image):
		descriptor = cv2.BRISK_create()

		if self.useSHIFT:
			descriptor = cv2.xfeatures2d.SHIFT_create()
		(kps,descs) = descriptor.detectAndCompute(image,None)
		kps = np.float32([kp.pt for kp in kps])

		return (kps,descs)