from os import system
import cv2
import glob

system('clear')
print("\n\n")

# Mi solución fue con una LISTA
#lImgs = ['galaxy', 'kangaroos-rain-australia_71370_990x742', 'Lighthouse', 'Moon sinking, sun rising']
# y le puse la extensión y el subdirectorio en el programa (siguientes lineas)

lImgs   = glob.glob('*.jpg')
print(lImgs)

for sImg in lImgs:
    if (sImg.startswith('resize_')):
        continue
    img = cv2.imread(sImg, 1) # 0 - Escala GRISES, -1 - Con Transparencia, 1 - Normal???
    nAncho  = 100
    nLargo  = 100
    resize_img = cv2.resize(img , (nAncho,nLargo))   #
    cv2.imshow(sImg, resize_img)
    if (cv2.imwrite('./resultados/resize_' + sImg, resize_img) == False):
        print(sImg, 'No se pudo guardar')    
    cv2.waitKey(0)              # 2000 - 2 segundos, 0 - Espera a key stroke
    cv2.destroyAllWindows()