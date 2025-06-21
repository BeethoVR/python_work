import cv2 
import time
from os import system
#import sys

system('clear')
print("\n\n")

frames_seg  = 20 # 24 FPS pon el video como en camara rápida
videoSize   = (1280, 720) #(640,480)

video       = cv2.VideoCapture(0) # Con '0' le dices que lo capture de la video camara

t           = time.localtime()
ini_time    = time.strftime("%M:%S", t)
ft_min      = int(time.strftime('%M', t)) + 1
ft_seg      = time.strftime('%S', t)
fin_time    = str(ft_min) + ':' + ft_seg
#print(ini_time, ' - ', fin_time)

try:
    """FourCC is a 4-byte code used to specify the video codec. The list of available codes can be found in fourcc.org. It is platform dependent. The following codecs work fine for me.

        In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
        In Windows: DIVX (More to be tested and added)
        In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).

        FourCC code is passed as ‘cv.VideoWriter_fourcc('M’,'J','P','G') or 
                                cv.VideoWriter_fourcc(*'MJPG')` for MJPG.
    """
    fourcc = cv2.VideoWriter_fourcc(*'MJPG') # Solo éste (MJPG) funcionó para mí, y en teoría funcionaría para TODOS
    video_out   = cv2.VideoWriter(f"./cap_video/videoSalida{ini_time}.mp4", fourcc, frames_seg , videoSize, False)
except:
    print('Error al generar archivo de salida')
    exit()

check = True
while check:
    check, frame    = video.read()

    #print(check)
    #print(frame)

    #time.sleep(3) # Sleep for 3 seconds

    #cv2.imshow('Capturing...', frame)    
    #cv2.waitKey(0)

    frame = cv2.resize(frame , videoSize)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing...', gray)
    video_out.write(gray)
    key = cv2.waitKey(int(1000/frames_seg))

    if (key != -1):
        break
    
    # Mi forma de medir 1 minuto de video
    if check == True:
        t        = time.localtime()
        ini_time = time.strftime("%M:%S", t)
        check = (ini_time != fin_time)
        #print(ini_time, '-', fin_time, '-->' , check)

video.release()
video_out.release()
cv2.destroyAllWindows()
