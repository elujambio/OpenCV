import numpy as numpy
import cv2
from matplotlib import pyplot as plt 

bgr_img = cv2.imread("input/pablo.jpg", 1)

# This line shows the image in matplotlib in grayscale 
# 
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# 
# OpenCV loads images in BGR (Blue, Green, Red), instead
# of RGB. So we need to fix it by splitting and  
# rearranging the image

b,g,r = cv2.split(bgr_img)
rgb_img = cv2.merge([r,g,b])

plt.imshow(rgb_img)
plt.xticks([]), plt.yticks([])
plt.show()