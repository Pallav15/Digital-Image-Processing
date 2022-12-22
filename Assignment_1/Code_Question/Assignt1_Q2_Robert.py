# importing the required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

## reading the image using library
image = cv2.imread("7.1.03.tiff",0)

# for giving padding to the image so that it can look more sharpen
row1 = np.array([0 for i in range(512)],dtype="uint8")  ## here converted integer to image datatype 
col1 = np.array([0 for i in range(514)],dtype="uint8")  ## to increase the sharpness
col1=np.reshape(col1,(514,1))

image=np.row_stack((row1,image))   ## adding padded row above image
image=np.row_stack((image,row1))  ## adding padded row below image
image=np.column_stack((col1,image)) ## adding padded col left side image
image=np.column_stack((image,col1)) ## adding padded col right side image

## Mask for finding Gx
robert1 = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])     

## Mask/ kernel for finding Gy
robert2 = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

## applying filter to the image with the mask1
Gx = cv2.filter2D(image,-1,robert1)

## applying filter to the image with the mask2
Gy = cv2.filter2D(image,-1, robert2)
## by this i got the edges almost 
Edges_Mask = abs(Gx)+abs(Gy)

## here the edges i got i added them to the actual image to get sharpen image
Sharpened_Image = image + (Edges_Mask//3)  # here i divided by to reduce the noice basically 
## first order mask are used for edge detection 

## for display of the images
cv2.imshow("Actual Image", image)

cv2.imshow("Only Edges",Edges_Mask)

cv2.imshow("Final sharpen Image using Robert", Sharpened_Image)
cv2.waitKey()
cv2.destroyAllWindows()