import cv2

import os

detect = cv2.imread('detect.png',0)
edges = cv2.Canny(detect,100,200)

outputname = 'output.png' #This is the name of the output detected file.

cv2.imwrite(outputname, edges)
cv2.imshow(outputname, edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
