import math
import numpy as np
import cv2
import matplotlib.pyplot as plt




def bilinear(Image, nrow, ncol,row, col):
    
    # Creating an Array of all zeros
    nImage = np.zeros((nrow, ncol), dtype = 'uint8')

    ## calculating the factor by which the size is to be reduced
    x_factor = row/nrow        # as 512/128
    y_factor = col/ncol        # as 512/128

    val = []

    for i in range(nrow):           #3 new image looping
        for j in range(ncol):
            x_coord = i*x_factor
            y_coord = j*y_factor

            ## as we know in bilinear we have to fine 4 surronding coordinates
            x1 = math.floor(x_coord)                    ## taking floor
            x2 = min(math.ceil(x_coord), row-1)         ## so that it can't go beyound the limit    
            y1 = math.floor(y_coord)                    
            y2 = min(math.ceil(y_coord),col-1)          ## so that it can't go beyound the limit

            #conditions checked
            val = bicond(Image, x1,x2,y1,y2,x_coord,y_coord)            ## verifying the conditions as taught in the classs
            ## how puttingthe value of c3 in new image pixel
            nImage[i,j] = val[0]
    
    return nImage

def bilinearArea(Image, nrow, ncol,row,col):
    # Creating an Array of all zeros
    nImage = np.zeros((nrow, ncol), dtype = 'uint8')

    ## calculating the factor by which the size is to be reduced
    x_factor = row/nrow        # as 512/128
    y_factor = col/ncol        # as 512/128

    val = []

    for i in range(nrow):           #3 new image looping
        for j in range(ncol):
            x_coord = i*x_factor            ## here i am finding the coordinate in the super resolved image
            y_coord = j*y_factor

            ## as we know in bilinear we have to fine 4 surronding coordinates
            x1 = math.floor(x_coord)            ## taking floor value 
            x2 = min(math.ceil(x_coord), row-1)         ## so that it can't go beyound the limit
            y1 = math.floor(y_coord)
            y2 = min(math.ceil(y_coord),col-1)          ## so that it can't go beyound the limit

            #conditions checked
            val = bicond_area(Image, x1,x2,y1,y2,x_coord,y_coord)                ## verifying the conditions as taught in the classs
            ## how puttingthe value of c3 in new image pixel
            nImage[i,j] = val[0]
    
    return nImage

def NN(Image, nrow, ncol,row,col):

    nnImage = np.zeros((nrow, ncol), dtype = 'uint8')

    factor = int(row/nrow)

    p=0
    k=0
    for i in range(nrow):
        for j in range(ncol):
            nnImage[i,j] = Image[p,k]
            k+=factor
        k=0
        p+=factor

    return nnImage

def NN_back(image, size2,n):
    new_image = np.zeros([size2,size2],dtype='uint8')             ## initialised the new imge woth all 0 in starting 
    p=0             # these are the variable to access the actual image
    k=0
    for i in range(0,size2,n):              # this loop is used to data in the new image matrix alternatively as size of new image is large
        for j in range(0,size2,n):          # . for alternating row as well as alternating column
            new_image[i][j] = image[p][k]
            # j+=2
            k+=1                            
        k=0
        # i+=2
        p+=1

    for i in range(0,size2,n):              # this loop is for filling the gap row vise that we left in above loop
        for j in range(1,size2,n):          # this is actually in this i ma replicating the values of left cell 
            new_image[i][j] = new_image[i][j-1]   ## vertically
            # j+=2
        # i+=2

    for i in range(0,size2,n):              ## this loop is for filling the gaps that we left in between the rows when we putting values in new inmage
        for j in range(1,size2,n):           #even after this in odd row and odd colum cells are left
            new_image[j][i] = new_image[j-1][i]
            # j+=2
        # i+=2

    for i in range(1,size2,n):                 ## . here just filling those gap left behind in above row and cell
        for j in range(1, size2,n):
            new_image[i][j] = new_image[i][j-1]
            # j+=2
        # i+=2

    return new_image

# def Linear(Image, nrow, ncol, row, col):

#     lImage = np.zeros((nrow, ncol),dtype = 'uint8')

#     for i in range(nrow):
#         for j in range(ncol):
def bilnearArea(Image, nrow, ncol):
    return cv2.resize(Image, dsize= (nrow, ncol), interpolation=cv2.INTER_AREA)
#     return lImage

def bell__(Image,nrow, ncol, row, col):
    nImage = np.zeros((nrow, ncol), dtype = 'uint8')

    ## calculating the factor by which the size is to be reduced
    x_factor = row/nrow        # as 512/128
    y_factor = col/ncol        # as 512/128

    val = []

    for i in range(nrow):           #3 new image looping
        for j in range(ncol):
            x_coord = i*x_factor
            y_coord = j*y_factor

            ## as we know in bilinear we have to fine 4 surronding coordinates
            x1 = math.floor(kernelBell(x_coord))                    ## taking floor
            x2 = min(math.ceil(kernelBell(x_coord)), row-1)         ## so that it can't go beyound the limit    
            y1 = math.floor((y_coord))                    
            y2 = min(math.ceil((y_coord)),col-1)          ## so that it can't go beyound the limit

            #conditions checked
            val = bicond(Image, x1,x2,y1,y2,x_coord,y_coord)            ## verifying the conditions as taught in the classs
            ## how puttingthe value of c3 in new image pixel
            nImage[i,j] = val[0]
    
    return nImage


def kernelBell(x):
    if(abs(x)<0.5):
        return 0.75 - abs(x)*abs(x)
    elif(abs(x)>0.5 and abs(x)<1.5):
        return 0.5*(abs(x)-1.5)*(abs(x)-1.5)
    else:
        return 0

Image = cv2.imread('cameraman.png',0)

r,c = Image.shape

# sImage = bell(nImage, row,col,nrow,ncol)
# print(sImage)
# print(Image)
def bell_(Image, nrow, ncol):
    return cv2.resize(Image, dsize= (nrow, ncol), interpolation=cv2.INTER_LANCZOS4)
def hermiite(Image, nrow, ncol):
    return cv2.resize(Image, dsize= (nrow, ncol), interpolation=cv2.INTER_CUBIC)
# print(r)
# print(c)
# print(k)

row = 513       #size of old Image approx
col = 513
nrow = 128       # size of new image
ncol = 128

def bicond(Image,x1,x2,y1,y2,x_coord,y_coord):
    val = []
    if((x2==x1) and (y2==y1)):              ## if both are same then it means theat the point is same
        z1 = int(x_coord)
        z2 = int(y_coord)

        c3 = Image[z1,z2]
    elif(x2==x1):                           ## it means the xcoordinate of new image is same as old only differenc is in y 
        c1 = Image[int(x_coord),int(y1)]
        c2 = Image[int(x_coord),int(y2)]
        c3 = c1*(y2-y_coord) + c2*(y_coord-y1)
    elif(y2==y1):                           ## it means the ycoordinate of new image is same as old only difference is in x
        c1 = Image[int(x1),int(y_coord)]
        c2 = Image[int(x2),int(y_coord)]
        c3 = c1*(x2-x_coord) + c2*(x_coord-x1)
    else:                                       # if both x, y are different then we have multiply the pixels woth opp distances same for y and x axis
        ## the 4 vertices are:  
        v1 = Image[x1,y1]
        v2 = Image[x1, y2]
        v3 = Image[x2,y1]
        v4 = Image[x2,y2]
        c1 = v1*(x2-x_coord) + v3*(x_coord-x1)
        c2 = v2*(x2-x_coord) + v4*(x_coord-x1)
        c3 = c1*(y2-y_coord) + c2*(y_coord-y1)          ## multiply to get the relative average of vertical coordinate

    val.append(c3)
    # val.append(x_coord)         ## For testing
    # val.append(y_coord)             
    return val
def hermite(Image, nrow, ncol, row, col):
    nImage = np.zeros((nrow, ncol), dtype = 'uint8')

    ## calculating the factor by which the size is to be reduced
    x_factor = row/nrow        # as 512/128
    y_factor = col/ncol        # as 512/128

    val = []

    for i in range(nrow):           #3 new image looping
        for j in range(ncol):
            x_coord = i*x_factor
            y_coord = j*y_factor

            ## as we know in bilinear we have to fine 4 surronding coordinates
            x1 = math.floor(hermitekernel(x_coord))                    ## taking floor
            x2 = min(math.ceil(hermitekernel(x_coord)), row-1)         ## so that it can't go beyound the limit    
            y1 = math.floor(hermitekernel(y_coord))                    
            y2 = min(math.ceil(hermitekernel(y_coord)),col-1)          ## so that it can't go beyound the limit

            #conditions checked
            val = bicond(Image, x1,x2,y1,y2,x_coord,y_coord)            ## verifying the conditions as taught in the classs
            ## how puttingthe value of c3 in new image pixel
            nImage[i,j] = val[0]
    
    return nImage

def hermitekernel(x):
    if(abs(x)<=1):
        return 2*abs(x)*abs(x)*abs(x) - 3* abs(x)*abs(x) + 1
    else:
        return 0

def bicond_area(Image,x1,x2,y1,y2,x_coord,y_coord):
    val = []
    if((x2==x1) and (y2==y1)):              ## if both are same then it means theat the point is same
        z1 = int(x_coord)
        z2 = int(y_coord)

        c3 = Image[z1,z2]
    elif(x2==x1):                           ## it means the xcoordinate of new image is same as old only differenc is in y 
        c1 = Image[int(x_coord),int(y1)]
        c2 = Image[int(x_coord),int(y2)]
        c3 = c1*(y2-y_coord) + c2*(y_coord-y1)
    elif(y2==y1):                           ## it means the ycoordinate of new image is same as old only difference is in x
        c1 = Image[int(x1),int(y_coord)]
        c2 = Image[int(x2),int(y_coord)]
        c3 = c1*(x2-x_coord) + c2*(x_coord-x1)
    else:                                       # if both x, y are different then we have multiply the pixels woth opp distances same for y and x axis
        ## the 4 vertices are:  
        yr1 = (y2-y_coord)
        yr2 = (y1 - y_coord)
        v1 = Image[x1,y1]
        v2 = Image[x1, y2]
        v3 = Image[x2,y1]
        v4 = Image[x2,y2]

        A1 = (x2-x_coord)*(y2-y_coord)                  #3 this is the area technique in this we are finding the area to different block then finding what all they are contributing
        A2 = (x_coord - x1)*(y2-y_coord)
        A3 = (x2-x_coord)*(y1 - y_coord)
        A4 = (x_coord-x2)*(y1-y_coord)

        c1 = v1*(A1/yr1) + v3*(A2/yr1)
        c2 = v2*(A3/yr1) + v4*(A4/yr1)
        c3 = c1 + c2          ## multiply to get the relative average of vertical coordinate

    val.append(c3)
    # val.append(x_coord)         ## For testing
    # val.append(y_coord)             
    return val


def b(Image, nrow, ncol, row, col):
    cImage = Image.copy()
    for i in range(row):
        for j in range(col):
            cImage[i,j] = 1000*kernelBell(cImage[i,j]/1000)
    return cImage
    

## Bilinear 2 techniques
nImage = bilinear(Image,nrow, ncol,row, col)               ##3 shrinking the image, downsampling
cv2.imshow('small Image', nImage)
## super resolving the image
sImage = bilinear(nImage,row, col,nrow,ncol)
# sImage = bell(nImage, row,col,nrow,ncol)
# print(sImage)
# print(Image)
aImage = bilnearArea(nImage, row, col)
cv2.imshow('super-resolved Image_bilinear',sImage)
cv2.imshow('super-resolved Image_bilinear_area',aImage)

## Nearest Neighbour technique
nnImage = NN(Image, nrow, ncol, row, col)
# cv2.imshow('original Image', Image)
s2Image = NN_back(nnImage, 256,2)
s4Image =  bell_(nImage,row, col)
# cv2.imshow('Bell Image',s4Image)
s3Image = NN_back(s2Image,row-1,2)
# cv2.imshow('nearest neighbour Image', nnImage)
# cv2.imshow('super-resolved_NN',s3Image)
#3 hermite
s5Image = hermiite(nImage, row, col)
# cv2.imshow('Hermite-technique',s5Image)

# bImage = b(Image,row, col, row,col)
# cv2.imshow('hi',bImage)

print(Image)
print(bImage)
# lImage = Linear(Image, nrow, ncol, row,col)
# cv2.imshow('original Image', Image)
# cv2.imshow('bilinear Interpolated Image', nImage)

print(cv2.PSNR(Image,sImage))
print(cv2.PSNR(Image,aImage))
print(cv2.PSNR(Image,s4Image))
print(cv2.PSNR(Image,s5Image))
# cv2.imshow('linear Image', lImage)
cv2.waitKey()
cv2.destroyAllWindows()

