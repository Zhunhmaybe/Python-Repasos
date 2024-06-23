class program:
    def __init__(self,num):
        self.num=num
        matriz=Matriz(num)
        matriz.GenerarMatriz()
        matriz.imprimir()

class Matriz:
    def __init__(self,num):
        self.num=num
        self.cont=1        
        self.matriz=[["0"for i in range(num)]for j in range(num)]

    def GenerarMatriz(self):
        for k in range(0,int (self.num/2)+1,1):
            if self.ComprobacionFilas(k)==True:
                for x in range(k,self.num-k,1):
                    # superior
                    self.matriz[k][x]=self.cont;self.cont+=1
                    #Control si sobrepasa el valor de nxn
                    if self.cont>(self.num*self.num)-0 :continue
                    #inferior
                    self.matriz[self.num-1-k][self.num-x-1]=self.cont;self.cont+=1
            if self.ComprobacionColumnas(k)==True:
                for w in range(k,self.num-k-2,1):
                    # derecha
                    self.matriz[w+1][self.num-1-k]=self.cont;self.cont+=1
                    #izquierda
                    self.matriz[self.num-2-w][k]=self.cont;self.cont+=1


    def ComprobacionFilas(self,k):        
        for i in range(k,self.num-k,1):
            if self.matriz[k][i]=="0" or self.matriz[self.matriz-1-k][i]=="0":
                return True
            else :
                return False
            
    def ComprobacionColumnas(self,k):
        for x in range(k+1,self.num-k-1,1):
            if self.matriz[x][k]=="0" or self.matriz[x][self.num-k-1]=="0":
                return True
            else:
                return False
    
    def imprimir(self):
        for i in range(self.num):
            for j in range(self.num):
                print(self.matriz[i][j],end="  ")
            print(" ")

        
programa=program(5)
programa.__init__