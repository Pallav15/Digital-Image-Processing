# importing the required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the Actual image present the folder
image = cv2.imread("ruler.512.tiff", 0)

# row, col = image.shape[:2]
row = 512       ## size of image
col = 512

filtered_median_image = np.zeros([row,col])            # for storing the values of the medains 

for i in range(1,row-1):              # leaving the first & last row
    for j in range(1,col-1):            # leaving the first & last col
        a1 = image[i-1][j-1]
        a2 = image[i-1,j]
        a3 = image[i-1,j+1]
        a4 = image[i,j-1]
        a5 = image[i,j]
        a6 = image[i,j+1]
        a7 = image[i+1,j-1]
        a8 = image[i+1,j]
        a9 = image[i+1,j+1]
        # print(a2)
        median = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
        # median = [image[i-1,j-1],image[i-1,j],image[i-1,j+1],image[i,j-1], image[i,j],image[i,j+1],image[i+1,j-1],image[i+1,j],image[i+1,j+1]]
        median.sort()           # sorting(asc) it for finding the middle value among all
        filtered_median_image[i][j] = median[4]               # as it contains 9 value and so middle value will be 4th


filtered5_median_image = np.zeros([row,col])            # for storing the values of the medains 
for i in range(2,row-2):              # leaving the first,sec & sec_last,last row
    for j in range(2,col-2):            # leaving the first,sec & sec_last,last col
        a1 = image[i-2][j-2]
        a2 = image[i-2][j-1]
        a3 = image[i-2][j]
        a4 = image[i-2][j+1]
        a5 = image[i-2][j+2]
        a6 = image[i-1][j-2]
        a7 = image[i-1][j-1]
        a8 = image[i-1][j]
        a9 = image[i-1][j+1]
        a10 = image[i-1][j+2]
        a11 = image[i][j-2]
        a12 = image[i][j-1]
        a13 = image[i][j]
        a14 = image[i][j+1]
        a15 = image[i][j+2]
        a16 = image[i+1][j-2]
        a17 = image[i+1][j-1]
        a18 = image[i+1][j]
        a19 = image[i+1][j+1]
        a20 = image[i+1][j+2]
        a21 = image[i+2][j-2]
        a22 = image[i+2][j-1]
        a23 = image[i+2][j]
        a24 = image[i+2][j+1]
        a25 = image[i+2][j+2]

        # print(a2)
        median1 = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25]
        # median = [image[i-1,j-1],image[i-1,j],image[i-1,j+1],image[i,j-1], image[i,j],image[i,j+1],image[i+1,j-1],image[i+1,j],image[i+1,j+1]]
        median1.sort()           # sorting(asc) it for finding the middle value among all
        filtered5_median_image[i][j] = median1[12]              # as it contains 9 value and so middle value will be 4th


cv2.imshow("Median_3X3_filter", filtered_median_image)
cv2.imshow("Median_5X5_filter", filtered5_median_image)
cv2.waitKey()
cv2.destroyAllWindows()