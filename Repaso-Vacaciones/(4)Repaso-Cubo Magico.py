class program:
    def __init__(self,num):
        self.num=num
        matriz=Matriz(num)
        matriz.GenerarMatriz()
        matriz.imprimir()

class Matriz:
    def __init__(self,num):
        self.num=num
        self.cont=0
        self.i,self.j=0,int(num/2)
        self.matriz=[["0"for i in range(num)]for j in range(num)]

    def GenerarMatriz(self):
        while self.cont<(self.num*self.num):
            #caso=superior e inferior
            if self.i<0 and self.j>=self.num:
                self.j-=1
                self.i+=2 
            #caso=superior
            if self.i <0:
                self.i=self.num-1
            #caso=derecha
            if self.j>=self.num:
                self.j=0
            #caso=ocupado
            if self.matriz[self.i][self.j]!="0":
                self.j-=1
                self.i+=2                

            self.matriz[self.i][self.j]=self.cont+1
            self.i-=1
            self.j+=1
            self.cont+=1

        
    def imprimir(self):
        for i in range(self.num):
            for j in range(self.num):
                print(self.matriz[i][j],end=" ")
            print(" ")

        
programa=program(5)
programa.__init__
