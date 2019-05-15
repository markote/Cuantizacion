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

generarCodebook(im,k=512,b=8):
    res=[]
    imtmp=[]
    for v in im:
        v8=v.split(k/b);
        imtmp=imtmp+[v8]
    bloque=[]
    for i in range(0,k+1):
        for j in range(0,(k/b)+1):
    
    return scipy.kmeans(res,512)

code(im):
    

decode(imd):           
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



