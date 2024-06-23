class SerVivo():
    def __init__(self):        
        self.energia="consumo Energia"
        self.reproduccion="Me reprodusco"
    def Respirar(self):
        print("Se respirar")

class Ser():
    def __init__(self):        
        self.ser="segundo ser vivo"
    def imprimir(self):
        print("Ser")

#Revisar la herencia multiple en python
class Humano(SerVivo,Ser):
    def imprimir():
        print("Soy humano")
        super().Respirar()
        print("khe")
        

David=Humano()
David.imprimir
print(David.energia)
print(David.imprimir)
    