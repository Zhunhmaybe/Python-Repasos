import os
import time

class Texto :
    def __init__(self,palabra) :
        self.palabra=palabra
        self.lista=[]
        self.lista.extend(self.palabra)


    def Generar(self,i):        
        self.lista.pop(i)
        self.lista.insert(i,"🔥")

    def imprimir(self):
        for i in range(len(self.lista)+1):
            if i>0:
                self.Generar(i-1)
                limpiar_consola()
                self.palabra=''.join(self.lista)
                print("Su palabra se quema o.o?")
                print(self.palabra)
            if i==0:
                print("Su palabra se quema o.o?")
                print(self.palabra)                                        
def limpiar_consola():
    #for x in range(0,)
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')

limpiar_consola()
progam=Texto("tetrahijuputa")
progam.__init__
progam.imprimir()







        
        
