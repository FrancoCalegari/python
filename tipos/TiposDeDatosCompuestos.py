#Una lista (se puede modificar)
lista = ["Franco Calegari", "franco", True, 1.80]

#Tupla (no se puede modificar)
tupla = ("esto no se puede modificar")

#esto se puede hacer
lista[2] = "Clara"

print(lista[2])

#Esto no porque es una tupla
#tupla[2] = "agregar"

print(lista)


#conjunto set la diferencia es que no se puede acceder por el inice al elemento del conjunto, pero lo puedo mostrar
 
conjunto = {"hola que tal", True, 1.82}

#diccionario

diccionario = {
    "hola" : "saludo",
    "como estas?" : "pregunta",
    "estas emocionado?" : True,
    "cuanto medis?" : 1.84
}

print(diccionario['hola'])

