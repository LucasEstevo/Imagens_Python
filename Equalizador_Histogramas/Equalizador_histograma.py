from matplotlib import pyplot as plt
import cv2

img = cv2.imread('Equalizador_Histogramas/mulher.png') #fusca.png | mulher.png
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_eq = cv2.equalizeHist(img) #Faz a equalização da imagem

#Mostra a Imagem Original
cv2.imshow('Imagem Original',img) 
#Mostra a Imagem Equalizada
cv2.imshow('Imagem Equalizada',img_eq)

## Histograma da Imagem Equalizada ##
plt.figure(figsize=[6.4, 4.8])
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img_eq.ravel(), 256, [0,256]) 
plt.xlim([0, 256])
plt.show(block=False)

## Histograma da Imagem Original ##
plt.figure(figsize=[6.4, 4.8])
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show(block=True)

cv2.waitKey(0)