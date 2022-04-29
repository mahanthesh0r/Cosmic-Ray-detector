import imutils
from array import array
import numpy as np
cnts = ([array([[[639, 475]],

       [[638, 476]],

       [[638, 477]],

       [[639, 477]],

       [[638, 476]]], dtype=np.int32)], array([[[-1, -1, -1, -1]]], dtype=np.int32))
cnts = imutils.grab_contours(cnts)
for c in cnts:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	print(cX,cY)