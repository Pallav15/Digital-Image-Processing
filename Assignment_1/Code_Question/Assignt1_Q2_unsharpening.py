# importing the required libraries
from typing import final
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the Actual image present the folder
image = cv2.imread("7.1.03.tiff",0)

# for giving padding to the image so that it can look more sharpen
row1 = np.array([0 for i in range(512)],dtype="uint8")  ## here converted integer to image datatype 
col1 = np.array([0 for i in range(514)],dtype="uint8")  ## to increase the sharpness
col1=np.reshape(col1,(514,1))

image=np.row_stack((row1,image))   ## adding padded row above image
image=np.row_stack((image,row1))  ## adding padded row below image
image=np.column_stack((col1,image)) ## adding padded col left side image
image=np.column_stack((image,col1)) ## adding padded col right side image

#created the mean filter kernal of size 3X3 and 5X5
###
##########       MEAN_filters
MeanK_3X3 = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

MeanK_5X5 = np.array([[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25]])

## Using the filter2D function i have multiplied the kernal and the actual image 
MeanK_3X3_image = cv2.filter2D(image, -1, MeanK_3X3)

MeanK_5X5_image = cv2.filter2D(image,-1,MeanK_5X5)

sharp_edgesk_3X3 = image - MeanK_3X3_image

sharp_edgesk_5X5 = image - MeanK_5X5_image

final_image_3X3_blur = image + sharp_edgesk_3X3

final_image_5X5_blur = image + sharp_edgesk_5X5

cv2.imshow("Actual Image", image)

cv2.imshow("sharpened image3X3", final_image_3X3_blur)

cv2.imshow("sharpened image5X5", final_image_5X5_blur)

cv2.waitKey()
cv2.destroyAllWindows()
