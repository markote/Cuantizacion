# -*- coding: utf-8 -*-

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt


import scipy.ndimage
import math
from scipy.cluster.vq import vq, kmeans

#%%
imagen = misc.ascent()#Leo la imagen
(n,m)=imagen.shape # filas y columnas de la imagen
plt.imshow(imagen, cmap=plt.cm.gray) 
plt.xticks([])
plt.yticks([])
plt.show() 

def generarCodigos(k, lista):
    
    if len(lista)==k :
        print("result")
        print([lista])
        return [lista]
    else:
        lista+="0"
        print("antes"+str(lista))
        l1=generarCodigos(k,lista)
        print("despues"+ str(lista))
        lista=lista[:len(lista)-1]
        print("Ponmgo 1 quito 0")
        lista+="1"
        print("antes"+str(lista))
        l2=generarCodigos(k,lista)
        print("despues"+ str(lista))
       
        return l1+l2

print(generarCodigos(2,[]))

def cuantificar(imagen, k=8):
    #c1 = generarCodigos(k,[])
    #c2 = [for i in range(0,1)]
    step = 256/(2**k)
    #imagenComp = ""
    imagenCuantizada = []
    for fil in imagen:
        filaImagenCuantizada = []
        for p in fil:
            #imagenComp += codigos[math.floor(p/step)]
            filaImagenCuantizada.append(math.floor(p/step)*step+math.floor(step/2))
        imagenCuantizada.append(filaImagenCuantizada)
    return imagenCuantizada

for i in range(1,9):
    imagenCuantizada = cuantificar(imagen,i)
    plt.imshow(imagenCuantizada, cmap=plt.cm.gray) 
    plt.xticks([])
    plt.yticks([])
    plt.show()
    Sigma=np.sqrt(sum(sum((imagen-imagenCuantizada)**2)))/(n*m)
    print("Sigma:", str(Sigma))
    ratio = 8/i
    print("Ratio comp:",str(ratio))

"""
Mostrar la imagen habiendo cuantizado los valores de los píxeles en
2**k niveles, k=1..8

Para cada cuantización dar la ratio de compresión y Sigma
"""




#%%
"""
Mostrar la imagen cuantizando los valores de los pixeles de cada bloque
n_bloque x n_bloque en 2^k niveles, siendo n_bloque=8 y k=2

Calcular Sigma y la ratio de compresión (para cada bloque 
es necesario guardar 16 bits extra para los valores máximos 
y mínimos del bloque, esto supone 16/n_bloque**2 bits más por pixel).
"""





           
