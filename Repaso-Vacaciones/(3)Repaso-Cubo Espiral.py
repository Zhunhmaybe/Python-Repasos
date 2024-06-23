class program:

    #__init__ significa que siempre se va a ejecutar primero es como el meotod main 
    '''self no es una palabra reservada, pero esta va a guardar la referencia de el objeto creado
    ,es decir que va a tener la direccion en memoria de el obejto
    cualquier cosa agregada con self en los parametros de los metodos ira al objeto para ser usado
    '''
    def __init__(self,num):
        self.num=num
        matriz=Matriz(self.num)
        matriz.GenerarMatriz()
        matriz.imprimir()

class Matriz:

    def __init__(self,num):
        self.num=num
        self.cont=1
        self.matriz=[[" " for i  in range(num)] for j in range(num)]    
    def GenerarMatriz(self):
        k,a,b=0,0,1
        while k<=int(self.num/2):
            # superior            
            for x in range(k,self.num-k,1):
                self.matriz[k][x]=self.cont                
                c=a+b
                a=b
                b=c
                self.cont+=1
            # derecha
            for y in range(k+1,self.num-k,1):
                self.matriz[y][self.num-k-1]=self.cont                
                c=a+b
                a=b
                b=c
                self.cont+=1
            # inferior
            for z in range(self.num-2-k,-1+k,-1):
                self.matriz[self.num-1-k][z]=self.cont                
                c=a+b
                a=b
                b=c
                self.cont+=1
            # izquierda   
            for w in range(self.num-2-k,+k,-1):
                self.matriz[w][k]=self.cont                
                c=a+b
                a=b
                b=c
                self.cont+=1
            k+=1
                     

    def imprimir(self):        
        for i in range(self.num):
            for j in range(self.num):
                print(self.matriz[i][j],end=" ")
            print("")

programa=program(5)
programa.__init__
