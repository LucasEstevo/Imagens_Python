<h1 align="center">💻 Binarização de Imagens - Python 💻</h1>

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
Este projeto tem como finalidade pegar uma imagem e fazer binarização (Deixar a imagem apenas com pixels branco e pretos)

<br/>

---

## 🐱‍💻 Sobre o Código 

<br/>

```Py
import cv2
import numpy as np

img = cv2.imread('Binario/Rodovia.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255,
cv2.THRESH_BINARY_INV)
resultado = np.vstack([
np.hstack([suave, bin]),
np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
])
cv2.imshow("Binarizacao da imagem", resultado)
cv2.waitKey(0)
```

## 🤓 Resultados
*Imagem Binarizada* <br/>
|||
|--|--|
|Imagem Original com efeito blur para redução de ruídos|Imagem binarizada com escala de preto predominante |
|Imagem Binarizada com escala de rbanco predominante| Junção das Binarizações com imagem original|
|||

![Imagem 1](Resultados/Binarizacao.png)
