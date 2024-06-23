class program:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.num=6
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre2):
        self.__nombre=nombre2

#se pone "__" dos lineas bajas para decir que el atributo solo sera accesible desde dentro del mismo 
programa=program("David")
print(programa.getNombre())

programa.setNombre("PEDRO")
print(programa.getNombre())
