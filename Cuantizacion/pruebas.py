def deconstruir(im,size,b):
    step=size//b
    imtmp=[[] for x in range(step*step)]
    print("movida",str(imtmp))
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
        
print(eliminarvacios([[],[],[1],[2],[3]]))

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
            
            res[i].append(vtmp[apuntadorb].pop(0))
            
            apuntador+=1
    
    return res
ej=[[1,1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3],[1,1,1,1,1,1],[2,2,2,2,2,2],[3,3,3,3,3,3]]
im=deconstruir(ej,6,3)
print(im)
im2=construir(im,6,3)
print(im2)