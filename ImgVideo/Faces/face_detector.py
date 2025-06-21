from os import system
import cv2

system('clear')
print("\n\n")

oFaceCascade    = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

oImg            = cv2.imread('FamVM.jpg')
oGreyImg        = cv2.cvtColor(oImg, cv2.COLOR_BGR2GRAY)
oFaces          = oFaceCascade.detectMultiScale(oGreyImg, scaleFactor   =1.25
                                                        , minNeighbors  =5)
print(type(oFaces))
print(oFaces)

for x , y, w, h in oFaces:
    oImg    = cv2.rectangle(oImg, (x, y), ((x+w),(y+h)), (0,255,0), 3)

oImgResize  = cv2.resize(oImg, (oImg.shape[1]//3, oImg.shape[0]//3))
cv2.imshow('Grey', oImgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('Todo Listo')

