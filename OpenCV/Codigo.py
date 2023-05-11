#----------------Librerías  que se usan-----------------------
import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
import imutils
#-----------------Fin librerías que se usan------------------------

#----------------Ejemplos de imágenes utilizadas------------------
# Se carga la imagen, ya sea figuras o una imagen
# dando la ruta de la imagen
img2 = cv2.imread('/home/Bellkhen/Descargas/opencv-shape-detection/shapes.png') 

#Imágenes de prueba  #Líneas comentadas
#img2=cv2.imread('/home/Bellkhen/Descargas/opencv-shape-detection/shapes.jpg') 
#img2 = cv2.imread("/home/Bellkhen/Descargas/otrost.jpg") 
#img2 = cv2.imread("/home/Bellkhen/Descargas/mona-china.jpg") 
#-----------------Fin ejemplo de imágenes utilizadas---------------

# Se renderiza la imagen a un tamaño dado (750 * 750), por si el tamaño de la 
# imagen es pequeña o muy grande 
img = cv2.resize(img2, (750,750)) 

# Se cambia el color de la imagen a grises para que la librería de opencv trabaje de 
# una forma más óptima  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Se cambia la representación de la imagen a una en forma binaria utilizando 
# THRESH_BINARY para cambiar los valores de umbralización a lo 
# máximo que es 255, eliminando las iluminaciones variables.
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  

#findContours es una función que permite buscar los n contornos de una imagen bin
contours, _ = cv2.findContours( 
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

#Crea un contador del tipo int
i = 0 
  
#Inicia un ciclo
for contour in contours:  }
    #Si i es igual a 0; i se convierte en 1
    if i == 0:  
        i = 1
        continue
        
    #Es la función que según los parámetros que tenga puede buscar los números de vértice de una forma para saber qué forma geométrica es
    approx = cv2.approxPolyDP( 
        #Se le da los parámetros para la forma geométrica
        contour, 0.01 * cv2.arcLength(contour, True), True) 
    
    #Se dibuja el contorno de la forma con el color rojo en RGB
    cv2.drawContours(img, [contour], 0,(0, 0, 255), 5) 
    
    #Calcula todos los momentos hasta el tercer orden de un polígono o forma rasterizada
    M = cv2.moments(contour) 
    
    #Si el valor de la posición m00 es diferente de 0.0 se le asigna a x y y nuevos valores de tipo entero
    if M['m00'] != 0.0: 
        #Asignación de x
        x = int(M['m10']/M['m00']) 
        #Asignación de y
        y = int(M['m01']/M['m00']) 
        
#Muestra en un frame la imagen con los dibujos en sus contornos
cv2.imshow('shapes', img)  
#Se queda en espera a una entrada 
cv2.waitKey(0) 
#Destruye el frame creado
cv2.destroyAllWindows() 
