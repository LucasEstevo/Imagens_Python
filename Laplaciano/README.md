<h1 align="center">💻 Laplaciano de Imagens - Python 💻</h1>

<br/>

## ✨Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina o
[Python 3.9.12](https://www.python.org/downloads/).
Após a instalação deste software, abra o local onde foi instalado e acesse a pasta Scripts.<br/>
Copie o diretório da pasta Scripts.<br/>
Abra o cmd do windows e digite `cd diretório_copiado`<br/>
Agora digite os seguintes comando e aguarde a finalização.<br/>
`pip install numpy`<br/>
`pip install opencv-python`<br/>
Após ter feito estes passos é só abrir o código no VS Code e ele estará pronto para uso

<br/>

---

## 📝 Sobre o Projeto
Este projeto tem como finalidade pegar uma imagem e aplicar o filtro laplaciano, nos eixos x e y depois monta-los em uma única imagem

<br/>

---

## 🐱‍💻 Sobre o Código 

<br/>

```Py
import numpy as np
import cv2
img = cv2.imread('Laplaciano/bingo.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobel = cv2.bitwise_or(sobelX, sobelY)
resultado = np.vstack([
np.hstack([img, sobelX]),
np.hstack([sobelY, sobel])
])
cv2.imshow("Laplaciano", resultado)
cv2.waitKey(0)
```

## 🤓 Resultados
*Imagem Laplaciana* <br/>
![Imagem 1](Resultados/bingo_laplaciano.png)
