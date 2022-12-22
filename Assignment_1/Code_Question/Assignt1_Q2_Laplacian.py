# importing the required libraries
from pickletools import uint8
import cv2
import numpy as np
import matplotlib.pyplot as plt

## reading the image using library
image = cv2.imread("7.1.03.tiff",0)

## for giving padding to the image so that it can look more sharpen
row1 = np.array([0 for i in range(512)],dtype="uint8")  ## here converted integer to image datatype 
col1 = np.array([0 for i in range(514)],dtype="uint8")  ## to increase the sharpness
col1=np.reshape(col1,(514,1))

image=np.row_stack((row1,image))   ## adding padded row above image
image=np.row_stack((image,row1))  ## adding padded row below image
image=np.column_stack((col1,image)) ## adding padded col left side image
image=np.column_stack((image,col1)) ## adding padded col right side image

## Laplacian Mask
Mask5 = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
## Enhance Laplacian Mask to increase the sharpness
Mask9 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

## sharped image with different laplacian mask
Sharpen_image5 = cv2.filter2D(image,-1,Mask5)

Sharpen_image9 = cv2.filter2D(image,-1,Mask9)

## displaying the sharpen images
cv2.imshow("Actual Image",image)
cv2.imshow("Sharpen Image5", Sharpen_image5)
cv2.imshow("Sharpen Image9", Sharpen_image9)
cv2.waitKey()
cv2.destroyAllWindows()