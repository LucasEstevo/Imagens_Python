<h1 align="center">💻 Histograma e Equalização de Imagens - Python 💻</h1>

<br/>

## ✨Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina o
[Python 3.9.12](https://www.python.org/downloads/).
Após a instalação deste software, abra o local onde foi instalado e acesse a pasta Scripts.<br/>
Copie o diretório da pasta Scripts.<br/>
Abra o cmd do windows e digite `cd diretório_copiado`<br/>
Agora digite os seguintes comando e aguarde a finalização.<br/>
`pip install matplotlib`<br/>
`pip install opencv-python`<br/>
Após ter feito estes passos é só abrir o código no VS Code e ele estará pronto para uso

<br/>

---

## 📝 Sobre o Projeto
Este projeto tem como finalidade pegar uma imagem e gerar seu histograma.

<br/>

---

## 🐱‍💻 Sobre o Código 

<br/>

```Py
from matplotlib import pyplot as plt
import cv2

img1 = cv2.imread('Histogramas/1.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

img2 = cv2.imread('Histogramas/2.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Mostra a Imagem Original
cv2.imshow('Imagem Original',img1) 
#Mostra a Imagem Equalizada
cv2.imshow('Imagem Equalizada',img2)

## Histograma da Imagem Equalizada ##
plt.figure(figsize=[6.4, 4.8])
plt.title("Histograma Imagem 1")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img1.ravel(), 256, [0,256]) 
plt.xlim([0, 256])
plt.show(block=False)

## Histograma da Imagem Original ##
plt.figure(figsize=[6.4, 4.8])
plt.title("Histograma Imagem 2")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img2.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show(block=True)

cv2.waitKey(1)
```

