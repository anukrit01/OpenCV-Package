import cv2

#Loading images
img = cv2.imread('C:/Users/Admin/Desktop/Billing Trip/DSC0125.jpg', 1)        #read the image in RGB/ coloured format
img_1 = cv2.imread('C:/Users/Admin/Desktop/Billing Trip/DSC0125.jpg', 0)      #read the image in gray scale/ black & white format
'''
print(type(img))
print(img)
print(img.shape)        #dimension of image
print(img_1.shape)

cv2.imshow('Image one', img)        #to show the image
cv2.waitKey(0)                      #to hold the popup of image for infinite time(0)
cv2.destroyAllWindows()
'''

#Resizing Image
resized_img = cv2.resize(img, (int(img.shape[1]/5), int(img.shape[0]/5)))
cv2.imshow('image resized', resized_img)
cv2.waitKey(0)                      #to hold the popup of image for infinite time(0)
cv2.destroyAllWindows()

cv2.imwrite('image resize.jpg', resized_img)