import numpy as np
import cv2
import matplotlib.pyplot as plt
import random

# image = cv2.imread("barbara_gray.bmp") # reading as gray scale

# row, col = image.shape[:2]
# print(row, col)


def impulse(image,n):
    s = size
    pixel = int((n/100)*512*512)            ##   n% noise in the Image
    for i in range(pixel):                      #3 taking the total of percentage mentioned in the question given 
        x = random.randint(0,s-1)               ## putting random pixel to white
        y = random.randint(0,s-1)
        image[x,y] = 255        #3 white
    
    for i in range(pixel):                  ## n% noise in the image
        x = random.randint(0,s-1)
        y = random.randint(0, s-1)          #3 putting random pixel to black
        image[x,y] = 0          ## dark

    return image

def median_filter(image, size):
    filtered_median_image = np.zeros([size,size],dtype='uint8')            # for storing the values of the medains 

    for i in range(1,size-1):              # leaving the first & last row
        for j in range(1,size-1):            # leaving the first & last col
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
    
    return filtered_median_image

def median_filter_5(image,size):
    filtered5_median_image = np.zeros([size,size],dtype='uint8')            # for storing the values of the medains 
    for i in range(2,size-2):              # leaving the first,sec & sec_last,last row
        for j in range(2,size-2):            # leaving the first,sec & sec_last,last col
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
            filtered5_median_image[i][j] = median1[12]              # as it contains 25 value and so middle value will be 12th
    
    return filtered5_median_image

def median_filter_7(image, size):
    filtered7_median_image = np.zeros([size,size],dtype='uint8')            # for storing the values of the medains 
    for i in range(3,size-3):              # leaving the first,sec,third & third_last,sec_last,last row
        for j in range(3,size-3):            # leaving the first,sec, third & third_last,sec_last,last col
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
            a26 = image[i-3][j-3]
            a27 = image[i-3][j-2]
            a28 = image[i-3][j-1]
            a29 = image[i-3][j]
            a30 = image[i-3][j+1]
            a31 = image[i-3][j+2]
            a32 = image[i-3][j+3]
            a33 = image[i+3][j-3]
            a34 = image[i+3][j-2]
            a35 = image[i+3][j-1]
            a36 = image[i+3][j]
            a37 = image[i+3][j+1]
            a38 = image[i+3][j+2]
            a39 = image[i+3][j+3]

            a40 = image[i-2][j-3]
            a41 = image[i-2][j+3]

            a42 = image[i-1][j-3]
            a43 = image[i-1][j+3]

            a44 = image[i][j-3]
            a45 = image[i][j+3]

            a46 = image[i+1][j-3]
            a47 = image[i+1][j+3]

            a48 = image[i+2][j-3]
            a49 = image[i+2][j+3]


            # print(a2)
            median1 = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34,a35,a36,a37,a38,a39,a40,a41,a42,a43,a44,a45,a46,a47,a48,a49]
            # median = [image[i-1,j-1],image[i-1,j],image[i-1,j+1],image[i,j-1], image[i,j],image[i,j+1],image[i+1,j-1],image[i+1,j],image[i+1,j+1]]
            median1.sort()           # sorting(asc) it for finding the middle value among all
            filtered7_median_image[i][j] = median1[24]             # as it contains 25 value and so middle value will be 12th
    
    return filtered7_median_image

image1 = cv2.imread("barbara_gray.bmp",0) # reading as gray scale
size = 512
# cv2.imwrite("noise1.bmp",impulse(image1, 5))
# cv2.imwrite("noise2.bmp",impulse(image1, 15))
# cv2.imwrite("noise3.bmp",impulse(image1, 20))
# cv2.imwrite("noise4.bmp",impulse(image1, 25))

image1 = cv2.imread("noise1.bmp",0)
image2 = cv2.imread("noise2.bmp",0)
image3 = cv2.imread("noise3.bmp",0)
image4 = cv2.imread("noise4.bmp",0)

filtered1_median_image = median_filter(impulse(image1.copy(),5), size)
filtered2_median_image = median_filter_5(impulse(image1.copy(),15), size)
filtered3_median_image = median_filter_5(impulse(image1.copy(),20), size)
filtered4_median_image = median_filter_7(impulse(image1.copy(),25), size)
# filtered4_median_image = cv2.medianBlur(image4,7)

psnr1  = cv2.PSNR(image1,filtered1_median_image)
psnr2  = cv2.PSNR(image1,filtered2_median_image)
psnr3  = cv2.PSNR(image1,filtered3_median_image)
psnr4  = cv2.PSNR(image1,filtered4_median_image)

print(psnr1)
print(psnr2)
print(psnr3)
print(psnr4)

cv2.imshow("Median1_filter", filtered1_median_image)
cv2.imshow("Median2_filter", filtered2_median_image)
cv2.imshow("Median3_filter", filtered3_median_image)
cv2.imshow("Median4_filter", filtered4_median_image)
cv2.waitKey()
cv2.destroyAllWindows()