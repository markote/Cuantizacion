# -*- coding: utf-8 -*-
"""

"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
import math
from scipy.cluster.vq import vq, kmeans

#%%
imagenHome=scipy.misc.imread('../Standard test images-20190515/house.png')
(n,m)=imagenHome.shape # filas y columnas de la imagen
plt.figure()    
plt.imshow(imagenHome, cmap=plt.cm.gray)
plt.show()

imagenHome=scipy.misc.imread('../Standard test images-20190515/cameraman.png')
(n,m)=imagenHome.shape # filas y columnas de la imagen
plt.figure()    
plt.imshow(imagenHome, cmap=plt.cm.gray)
plt.show()
#%%

def deconstruir(im,size,b):
    step=size//b
    imtmp=[[] for x in range(step*step)]
    for i in range(size):
        for j in range(size):
            ib=(i//b)*step+(j//b)
            imtmp[ib]=imtmp[ib]+[im[i][j]]
    return imtmp

def eliminarvacios(vec):
    count=0
    for x in vec:
        if len(x)==0 :
            count=count+1
    for i in range(count):
        vec.pop(0)
        
    return vec
    
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
                vtmp=eliminarvacios(vtmp)
                apuntador=0
                apuntadorb=0

            #print("vtmp:")
            #print(vtmp)
            #print("vtmp:")
            #print(vtmp[apuntadorb])
            #print("vtmp apuntador")
            #print(apuntadorb)
            #print("Apuntador")
            #print("i:"+str(i)+"j:"+str(j))            
            
            res[i].append(vtmp[apuntadorb].pop(0))
            
            apuntador+=1
    
    return res
    
def generarCodebook(im,size=512,b=8,k=512):
    res=deconstruir(im,size,b)
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j]=float(res[i][j])
    #imrec=construir(imtmp,size,b)
    #imtmp=construir([[1,1,1,2,2,2,3,3,3],[1,1,1,2,2,2,3,3,3],[1,1,1,2,2,2,3,3,3],[1,1,1,2,2,2,3,3,3]],6,3)
    #return imtmp        
    #print(imtmp)
    #print("MOvida len:", len(imtmp))
    res=scipy.cluster.vq.kmeans(res,k)
    return res[0]

def distance(v1,v2):
    result=0
    for i in range(len(v1)):
        result=result+pow(v1[i]-v2[i],2)
    
    return result

def compresion(im,dic,size=512,b=8):
    imdec=deconstruir(im,size,b)
    imres=[]
    imres=vq(imdec,dic)
    return imres
    
def decompresion(imd,dic,size=512,b=8):
    tmpim=[]
    for i in imd:
        tmpim.append(dic[i])
    print("tmpim: ")
    
    return tmpim
    #im=construir(tmpim,size,b)
    #plt.figure()    
    #plt.imshow(im, cmap=plt.cm.gray)
    #plt.show()
    #return (imd,tmpim)
    
prueba=deconstruir(imagenHome,512,8)
#prueba2=construir(prueba,512,8)
print("Polla morena")
dic=generarCodebook(imagenHome).tolist()
imagencomp,errores=compresion(imagenHome,dic)
errores=decompresion(imagencomp,dic)
print("End")

for i in range(len(prueba)):
    for j in range(len(prueba[i])):
        prueba[i][j]=int( errores[i][j])

print("End 2")

imagenHomeRecons=construir(prueba,512,8)
plt.figure()    
plt.imshow(imagenHomeRecons, cmap=plt.cm.gray)
plt.show()
print("End 3")
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



