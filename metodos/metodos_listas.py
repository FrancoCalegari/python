#creando una lista con list

lista = list(["hola", "que tal", 58])

#devuelve la cantidad de elemntos 

cantidad_elemntos = len(lista)

#agregando elementos a la lista

lista.append("jajajajja")

#agregando elementos en el indice espesifico

lista.insert(2, "te amu chemy")

#agregando varios elementos a la lista

lista.extend([False,2023])

#eliminando un elemento de la lista por un indice

lista.pop(0)#si se pone -1 elimina dsde el ultimo elemento

#removiendo un elemento de la lista por su valor

lista.remove("hola")#sirve para eliminar un valor que sabemos que existe

#esto elimina toda la lista

lista.clear()


#sirve para ordenar la lista de menor a menor si usamor reverse invierte el orden

lista.sort()

#dar vuelta el orden de la lista

lista.reverse()



print(lista)


