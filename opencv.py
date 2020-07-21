
import cv2
import numpy as np
import os as os

print(os.getcwd())


path='/Users/piyushjain/Desktop/pics vids/My hero/mypic.jpeg'

## For  Reading and showing Image in Grayscale
    # img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    # #cv2.imshow('image',img)
    # #cv2.waitKey(0)
    # #cv2.destroyAllWindows()

##For Saving Image in other location
    # path2='/Users/piyushjain/Desktop/OCR'
    # print(os.listdir(path2))
    # os.chdir(path2)
    # cv2.imwrite("NewByCV2.jpeg",img)
    # print(os.listdir(path2))


##RGB color presentation
    # img=cv2.imread(path)
    # B,G,R=cv2.split(img)
    # cv2.imshow('Original',img)
    # cv2.waitKey(0)
    # cv2.imshow('Blue',B)
    # cv2.waitKey(0)
    # cv2.imshow('Green',G)
    # cv2.waitKey(0)
    # cv2.imshow('Red',R)
    # cv2.waitKey(0)
    #cv2.destroyAllWindows()


##Addng  & Subtracting Two Images  Two Images
# path2='/Users/piyushjain/Desktop/pics vids/My hero/MS-Dhoni.jpg'
# img=cv2.imread(path)
# img=cv2.resize(img,(500,400))
# img2=cv2.imread(path2)
# img2=cv2.resize(img2,(500,400))

# weightedsum=cv2.addWeighted(img,0.5,img2,1,0)
#cv2.imshow('Weighted Image',weightedsum)
# os.chdir('/Users/piyushjain/Desktop/OCR')
# cv2.imwrite("Dhoni.jpeg",weightedsum)
# weightedsub=cv2.subtract(img,img2)
# os.chdir('/Users/piyushjain/Desktop/OCR')
# cv2.imwrite("Dhonibhaipiyush.jpeg",weightedsub)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# Image Erosion
# img=cv2.imread(path)
# kernel = np.ones((10, 10), np.uint8)
#
# #img2=cv2.erode(img,kernel)
# img2=cv2.erode(img,kernel,cv2.BORDER_REFLECT)
#
# os.chdir('/Users/piyushjain/Desktop/OCR')
# cv2.imwrite("erodedBorderReflect.jpeg",img2)
#

#Blurr Image   Remove Noise

# img=cv2.imread(path)
# GaussianBlurr=cv2.GaussianBlur(img,(7,7),0)
# path2='/Users/piyushjain/Desktop/OCR'
# os.chdir(path2)
# cv2.imwrite("GaussianBlurrImage.jpeg",GaussianBlurr)



# img=cv2.imread(path)
# MedianBlurr=cv2.medianBlur(img,5)
# path2='/Users/piyushjain/Desktop/OCR'
# os.chdir(path2)
# cv2.imwrite("MedianBlurrImage.jpeg",MedianBlurr)


# img=cv2.imread(path)
# bilateralFilterBlurr=cv2.bilateralFilter(img,9,75,75)
# path2='/Users/piyushjain/Desktop/OCR'
# os.chdir(path2)
# cv2.imwrite("bilateralFilter.jpeg",bilateralFilterBlurr)



# img=cv2.imread(path)
# img2=cv2.Canny(img,100,200)
# path2='/Users/piyushjain/Desktop/OCR'
# os.chdir(path2)
# cv2.imwrite("CannyEdgeDetection2.jpeg",img2)




