# -*- coding: utf-8 -*-
"""

"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
from scipy.cluster.vq import vq, kmeans

#%%
imagen=scipy.misc.imread('../Standard test images-20190515/house.png')
(n,m)=imagen.shape # filas y columnas de la imagen
plt.figure()    
plt.imshow(imagen, cmap=plt.cm.gray)
plt.show()
#%%
def deconstruir(im,size,b):
    step=size//b
    imtmp=[[] for x in range(step*step)]
    for i in range(size):
        for j in range(size):
            ib=(i//8)*step+(j//8)
            imtmp[ib]=imtmp[ib]+[im[i][j]]
    return imtmp

def construir(vect,size,b):
    step=size//b
    res=[[] for x in range(size)]#vector de 512 posiciones que rellenaremos
    apuntadorb=0
    apuntador=0
    vtmp=vect
    for i in range(len(res)):
        for j in range(len(res)):
            
            
            if apuntador == b :
                apuntador=0
                apuntadorb+=1
            if apuntadorb == step :
                apuntador=0
                apuntadorb=0
                
            res[i].append(vtmp[apuntadorb].pop(0))
            
            if len(vtmp[apuntadorb])==0:
                vtmp[apuntadorb].pop(apuntador)
                
            apuntador+=1
                
            
def generarCodebook(im,size=512,b=8,k=512):
    imtmp=deconstruir(im,size,b)
    imrec=construir(imtmp,size,b)
    plt.figure()    
    plt.imshow(imagen, cmap=plt.cm.gray)
    plt.show()
    return imtmp        
    #print(imtmp)
    #print("MOvida len:", len(imtmp))
    #return scipy.kmeans(res,512)

generarCodebook(imagen)
#code(im):
    

#decode(imd):           
"""
Usando K-means http://docs.scipy.org/doc/scipy/reference/cluster.vq.html
crear un diccionario cuyas palabras sean bloques 8x8 con 512 entradas 
para la imagen house.png.

Dibujar el resultado de codificar house.png con dicho diccionario.

Calcular el error, la ratio de compresión y el número de bits por píxel
"""

"""
Hacer lo mismo con la imagen cameraman.png

https://atenea.upc.edu/mod/folder/view.php?id=1833385
http://www.imageprocessingplace.com/downloads_V3/root_downloads/image_databases/standard_test_images.zip
"""


"""
Dibujar el resultado de codificar cameraman.png con el diccionarios obtenido
con la imagen house.png

Calcular el error.
"""



