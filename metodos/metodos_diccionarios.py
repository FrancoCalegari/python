diccionario = {
    "nombre" : "franco",
    "apellido" : "Si bb",
    "wenas" : 56544165416
}

#nos devuelve un objeto dict_item

claves = diccionario.keys()


#obteniendo un elemento con get y si no encuentra el programa continua
dar = diccionario.get("nombre")

#clear elimina todo del diccionario

diccionario.clear()

#eliminando un elemento del diccionario

diccionario.pop("nombre")

#obteniendo un elemento un dic_item interables

diccionario_iterable = diccionario.items()

print(claves)