def imprimir (a,b):
    c=a+b
    yield c
    d=c+a
    yield d   

#yield sirve como un return pero infinito
#yield tiene menor uso en la memoria 
Yield=imprimir(2,3)

#for i in Yield:
#    print (i)

#next =siguiente este lo que hace es buscar el valor siguiente de una secuencia.
print(next(Yield))
print(next(Yield))





