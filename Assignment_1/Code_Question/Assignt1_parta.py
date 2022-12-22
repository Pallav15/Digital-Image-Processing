# importing the required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the Actual image present the folder
image = cv2.imread("ruler.512.tiff",0)

#created the mean filter kernal of size 3X3 and 5X5
###
##########       MEAN_filters
MeanK_3X3 = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

MeanK_5X5 = np.array([[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25],[1/25,1/25,1/25,1/25,1/25]])

## Using the filter2D function i have multiplied the kernal and the actual image 
MeanK_3X3_image = cv2.filter2D(image, -1, MeanK_3X3)

MeanK_5X5_image = cv2.filter2D(image,-1,MeanK_5X5)


##########       MEADIAN_filters
## for displaying the image after filtering
cv2.imshow("Actual Image", image)
cv2.imshow("Mean filtered 3X3", MeanK_3X3_image)
cv2.imshow("Mean filtered 5X5", MeanK_5X5_image)
cv2.waitKey()
cv2.destroyAllWindows()

