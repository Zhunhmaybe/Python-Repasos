#la tuplas son inmutables es decir que no se van a poder modificar 
#Se puede obtener lo que contiene pero el resultado sera otra tupla 
#son mas rapidas y menos espacio
#formatena strings
#pueden utilizarce como claves en un diccionario la listas no

miTupla=("sofia",1938,1.2)
print(miTupla[:])

#convertir de tupla a lista
miLista=list(miTupla)
#covertir de lista a tupla
mitupla2=tuple(miLista)

#saber el numero de veces que existe un elemento dentro de la tupla
print(mitupla2.count(1.2))

#truquito
nombre,ano,tex=miTupla
print(nombre)
print(1)

#---------------------------------------------------------------Diccionarios
#para obter el valor deseado se debe de poner la clave (int,str)
diccionario={1:"pito"}
print(diccionario[1],"1")

#anadir un elemento con una constrasena
diccionario[2]="tefa"
print(diccionario,"2")

#eliminar
del diccionario[2]
print(diccionario,"3")

#de tupla a diccionario
#mitupla son las contrasenas
diccionario2={miTupla[0]:1,miTupla[1]:2,miTupla[2]:3}
print(diccionario2,"4")
print(diccionario2.keys())
print(diccionario2.values())



