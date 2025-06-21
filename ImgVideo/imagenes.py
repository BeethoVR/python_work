from os import system
import cv2

system('clear')
print("\n\n")

img = cv2.imread('galaxy.jpg', 0) # 0 - Escala GRISES, -1 - Con Transparencia, 1 - ???

print(type(img))
print(img)          # Data, como números qiue indican la intencidad del color, en éste caso GRISES
print(img.shape)    # Size
print(img.ndim)     # Dimensiones/Capas

nAncho  = (img.shape[1]//4)
nLargo  = (img.shape[0]//4)
#resize_img = cv2.resize(img, (300,500))        # tupla(Ancho , Largo)
resize_img = cv2.resize(img , (nAncho,nLargo))   # Para hacerla a la mitad
cv2.imshow('Galaxy Risize', resize_img)
cv2.imwrite('./resultados/galaxy_resize.jpg', resize_img)
#cv2.imshow('Galaxy', img)
cv2.waitKey(0) # 2000 - 2 segundos, 0 - Espera a key stroke
cv2.destroyAllWindows()

print('Todo Ok...')