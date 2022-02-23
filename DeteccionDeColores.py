import numpy as np
import cv2


# Activamos la camara
camara = cv2.VideoCapture(0)

redBajo1 = np.array([0,100,20],np.uint8)
redAlto1 = np.array([8,255,255],np.uint8)

redBajo2 = np.array([175,100,20],np.uint8)
redAlto2 = np.array([179,255,255],np.uint8)

#"Frame" obtendrá el siguiente fotograma en la cámara (a través de "camara").
# "Ret" obtendrá el valor de retorno al obtener el marco de la cámara,
#  ya sea verdadero o falso.
while True:
    ret,frame = camara.read()
    if ret == True:
      frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
      maskRed1 = cv2.inRange(frameHSV,redBajo1,redAlto1)
      maskRed2 = cv2.inRange(frameHSV,redBajo2,redAlto2)
      #Unimos las 2 mascaras
      maskRed = cv2.add(maskRed1,maskRed2)
      #Mostramos el color 
      maskRedis = cv2.bitwise_and(frame,frame,mask=maskRed)
      cv2.imshow('Camara',frame)
      cv2.imshow('Deteccion de color',maskRed)
      #El 0xFF en este escenario representa el binario 11111111, un binario de 8 bits,
       #Al preionar la tecla 'x' finalizamos la ejecucion
      if cv2.waitKey(1) & 0xFF == ord('x'):
          break



camara.release()
cv2.destroyAllWindows()