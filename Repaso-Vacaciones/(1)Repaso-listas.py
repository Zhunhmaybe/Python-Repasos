#1-los strings siempre deben que ir con [] 
miLista=["Juan","sofia","estefani","auron"]
#imprime todo
print(miLista[:],"1")
#elemento especifico de miLista
print(miLista[2],"2")
#imprimir dentro de un rango especifico <
print(miLista[0:2],"3")
#imprimir todo,sin un maximo
print(miLista[0:],"4")
#anadir un elemento al final append
miLista.append("ruben")
print(miLista[:],"5")
#si no pongo[] como lista este me deletrea la palabra extend sirve para juntar dos listas
miLista.extend(["tonyy"])
print(miLista[:],"6")
#pone el elemento donde se le indique
miLista.insert(2,"tony")
print(miLista[:],"7")
#me da el indice o lugar de un elemento a buscar
print(miLista.index("tonyy"))
print(miLista[:],"8")
#saber si es true o flase si un elemento de encuentra en la lista
print("sofia"in miLista,"9")
#milista.remove es para eliminar un elemento concreto por ejemplo "sofia" 
#miLista.pop elimina el ultimo elemento de la lista