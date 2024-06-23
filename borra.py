class CuboEspiral():
    def __init__(self,tam):
        self.arreglo=[["0"for j in range(tam)]for i in range(tam)]
        

    def Generar(self):
        self.tam,cont1,k=len(self.arreglo),0,1
        while(cont1<(self.tam+1)//2):
            #Arriba            
            for a in range(cont1,(self.tam)-cont1):
                self.arreglo[cont1][a]=k
                k+=1
            #righyt
            for b in range(cont1+1,(self.tam-1)-cont1):
                self.arreglo[b][self.tam-1-cont1]=k
                k+=1
            if k>(self.tam*self.tam):
                cont1+=1                
                continue
            #abajo           
            for c in range((self.tam-1)-cont1,cont1-1,-1):
                self.arreglo[self.tam-1-cont1][c]=k
                k+=1

            #left
            for d in range(self.tam-2-cont1,cont1,-1):
                self.arreglo[d][cont1]=k
                k+=1

            cont1+=1
        
    def Imprimir(self):
        for x in range(len(self.arreglo)):
            for y in range(len(self.arreglo)):
                print(self.arreglo[x][y],end=" ")
            print()

cubo=CuboEspiral(5)
cubo.Generar()
cubo.Imprimir()

