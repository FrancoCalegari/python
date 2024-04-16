#Creando diccionarios con dict()

diccionario = dict(nombre = "Franco", apellido = "BB")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos

diccionario2 = {frozenset(["Franco", "Chemy"]): "amor"}

#creando diccionarios con fromkeys

diccionario3 = dict.fromkeys(["AMOR", "Divino"])#primer dato iterable segundo dato un valor fijo



print(diccionario)