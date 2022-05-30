#pip install numpy
import cv2
import numpy as np

img = cv2.imread('Blur/leao.png')
rows,cols=img.shape[:2]

kernel_25 = np.ones((25,25),np.float32)/625.0
output_kernel=cv2.filter2D(img,-1,kernel_25)

img_blur = cv2.blur(img,(10,10)) #Define o valor do efeito blur nas coordenadas (x,y)

cv2.imshow('Original',img)
cv2.imshow('Blur',img_blur)

cv2.waitKey(0)