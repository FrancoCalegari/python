#creando una funcion de 3 parametros, si o si declarar la variable en su orden de funcion
print("///////////")
def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido} sos rre {adjetivo}"

resultado = frase("franco", "Calegari", "lindo")
print(resultado)

#utilizadno keyword arguments, en este no importa el orden en el que este siempre se va a ordenar "solo"
print("///////////")
frase_resultante = frase(adjetivo= "lindo", nombre= "franco", apellido="calegari")

print(frase_resultante)

print("///////////")

def frase2(nombre,apellido,adjetivo = "tonto"):#de esta forma declaramos los parametros default que luego al pasarle la variable se pueden cambiar
    return f"Hola {nombre} {apellido} sos rre {adjetivo}"

resultado2 = frase2("franco","calegari")
print(resultado2)