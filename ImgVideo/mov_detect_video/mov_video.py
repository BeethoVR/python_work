import cv2, time, pandas
from datetime import datetime
from os import system
#import sys
system('clear')
print("\n\n")

def setTime(move_list, time_list):
    status = 'OUT - '
    if (move_list[-1] == True):
        status = 'IN - '
    time_list.append((status, datetime.now().strftime("%H:%M:%S")))

frames_seg  = 20 # 24 FPS pone el video como en camara rápida
videoSize   = (640, 480) #(1280, 720) #(640,480)

first_frame = None
video       = cv2.VideoCapture(0) # Con '0' le dices que lo capture de la video camara

t           = time.localtime()
ini_time    = time.strftime("%M:%S", t)
ft_min      = int(time.strftime('%M', t)) + 1
ft_seg      = time.strftime('%S', t)
fin_time    = str(ft_min) + ':' + ft_seg

status_list = []
time_list   = []

check = True
while check:
    check, frame    = video.read()

    isMov = False

    frame = cv2.resize(frame , videoSize)       # Lo hice más peque, para poder 
                                                # ver los 2 videos al mismo tiempo

    #frame = cv2.resize(frame , videoSize)
    gray     = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayWork = cv2.GaussianBlur(gray, (21,21), 0)       # Suaviza la imagen y elimina el ruido, 
                                                        # y eso potencia/aumenta la precisión en
                                                        # el cálculo
    if (first_frame is None):
        first_frame = grayWork  # Imagen base/REFEFERENCIA para comparar el movimiento
        continue                # como guardo la REFEFERENCIA, se va al inicio del loop 

    delta_frame = cv2.absdiff(first_frame, grayWork)  

    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] # OJO: Debe ser el segundo parametro, pues 
                                                                             # ésta función regresa una tupla, donde el #
                                                                             # segundo dato ([1]) es el frame
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cnts         = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    #(cnts, _)    = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Estas 2 líneas son lo mismo
    for countour in cnts:
        # Aquí checa si hay alguna diferncia en la imagen, de que se detecta algo
        if (cv2.contourArea(countour) < 1600): # Si el área en menor de 1600px
            continue
        isMov = True
        (x, y, w, h) = cv2.boundingRect(countour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 3) # COLOR (B,G,R)
      
    status_list.append(isMov)
    if (len(status_list) > 1):
        if (status_list[-1] != status_list[-2]) : 
            #t        = time.localtime()
            #movTime  = time.strftime("%M:%S", t)
            setTime(status_list, time_list)
            #status = 'OUT - '
            #if (status_list[-1] == True):
            #    status = 'IN - '
            #time_list.append((status, datetime.now().strftime("%H:%M:%S")))
    
    cv2.imshow('Capturing...' , frame)
    #cv2.imshow('Original Frame...'  , first_frame)
    #cv2.imshow('Capturing Frame...' , gray)
    #cv2.imshow('Delta Frame...'     , delta_frame)
    #cv2.imshow('Threshhold Frame...', thresh_frame)  

    key = cv2.waitKey(int(1000/frames_seg))
    if (key != -1):
        status_list.append(isMov)
        setTime(status_list, time_list)    
        break
    
    # Mi forma de medir 1 minuto de video
    #if check == True:
    #    t        = time.localtime()
    #    ini_time = time.strftime("%M:%S", t)
    #    #check = (ini_time != fin_time)
    #    #print(ini_time, '-', fin_time, '-->' , check)

    #if (isMov):
    #    print('Hay movimiento')   
    #else:
    #    print('---')
video.release()
#video_out.release()
cv2.destroyAllWindows()

#print(status_list)
print(time_list)

#df          = pandas.DataFrame(columns=['Ini', 'Fin'])
listIni     = []
listFin     = []
for mtime in range(0,len(time_list),2):
    if (mtime+1) >= len(time_list):
        break
    print('Ini:' + time_list[mtime][1] + ' Fin:' + time_list[mtime+1][1])
    listIni.append(time_list[mtime][1])
    listFin.append(time_list[mtime+1][1])
    # pandas.df.append en PANDAS 2.0 ya está deprecado/obsoleto, busque otra forma
    #df1 = pandas.DataFrame({'Ini':time_list[mtime][1],'Fin':time_list[mtime+1][1]})
    #df = df.append({'Ini':time_list[mtime][1],'Fin':time_list[mtime+1][1]}, ignore_index=True)
    #df = pandas.concat([df, df1], ignore_index=True)
df          = pandas.DataFrame({'Ini': listIni, 'Fin': listFin})    
df.to_csv('./mov_detect_video/Times.csv')
