def X0Y0(num):
    matriz=[["0"for i in range(num)]for j in range(num)]

    #Modificacion
    cont=0
    cont1=1
    for x in range(num):
        if(cont%2==0):
            for y in range(0,num,1):
                matriz[y][x]=cont1;
                cont1+=1;
        if cont%2!=0:
            for y in range(num-1,-1,-1):
                matriz[y][x]=cont1;
                cont1+=1;
        cont+=1;
    Imprimir(matriz)

def X0Y0R(num):
    matriz=[["0"for i in range(num)]for j in range(num)]  
    cont=0
    cont1=1
    for x in range(num):
        if cont%2==0:            
            for y in range(num):
                matriz[x][y]=cont1;
                cont1+=1
        if cont%2!=0:
            for y in range(num-1,-1,-1):
                matriz[x][y]=cont1;
                cont1+=1
        cont+=1
    Imprimir(matriz)  
def XFYF(fila,col):
    matriz=[[" "for i in range(col)]for j in range(fila)]
    cont1=0
    cont=1
    for x in range(fila-1,-1,-1):
        if cont1%2==0:
            for y in range(col-1,-1,-1):
                matriz[x][y]=cont
                cont+=1
        if cont1%2!=0:
            for y in range(col):
                matriz[x][y]=cont
                cont+=1
        cont1+=1
    for u in matriz:
        print(u)

def MatrizInversaDiagonal(fila,col):
    matriz=[[" "for y in range(col)]for x in range(fila)]
    cont=1
    i=fila-1
    j=col-1
    contx=i
    conty=j
    while (i>=0 and i<fila):
        matriz[i][j]=cont
        cont+=1
        i+=1
        j-=1
        if(i>=fila and j<col and j>=0):
            contx-=1
            i=contx
            j=col-1
    cero=0    
    #Identificacmos el cero en la ultima fila
    for k in range(col-1,-1,-1):
        for h in range(fila-1,-1,-1):
            if (matriz[h][k]==' ' and cero==0):
                i=h
                j=k
                cero=1
    #medio
    contx=j
    while(i<fila and j>=0):
        matriz[i][j]=cont
        cont+=1
        i+=1
        j-=1
        if(i>=fila and j>=0):
            contx-=1
            j=contx
            i=0
    cero=0
    #Identificacmos el cero en la ultima fila
    for k in range(col-1,-1,-1):
        for h in range(fila-1,-1,-1):
            if (matriz[h][k]==' ' and cero==0):
                i=h
                j=k
                cero=1
    conty=j
    while(j>=0 and i>=0):
        matriz[i][j]=cont
        cont+=1
        i+=1
        j-=1
        if(j<0 and i>0):
            conty-=1
            j=conty
            i=0
    print(i,j)    
    for u in matriz:
        print(u)

def Imprimir(matriz):
    for x in range(3):
        for y in range(5):
            print(matriz[x][y],end=" ")
        print()

matriz=MatrizInversaDiagonal(3,3)

