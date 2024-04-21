import re

texto = '''Hola rey como estas?. bien espero1 lo pases hola lindo2.
 en fin es texto de pruubea 3'''

resultado= re.findall("Hola" ,texto, flags=re.IGNORECASE)

print("/////////////////////////")

print(resultado)
print("/////////////////////////")
#Expresiones regulares

#\d -- busca digitos numericos del 0 - 9

resultado = re.findall(r"\d", texto)
print("/////////////////////////")
print (resultado) #devuelve lista

#\D -- busca todo menos numeros del 0 - 9

resultado = re.findall(r"\D", texto)
print("/////////////////////////")
print (resultado)

#\w -- busca caracteres alfanumericos osea desde [a - z, A - Z, 0 - 9, _]

resultado = re.findall(r"\w", texto)
print("/////////////////////////")
print (resultado)

#\W -- busca todo menos caracteres alfanumericos osea desde [a - z, A - Z, 0 - 9, _]

resultado = re.findall(r"\W", texto)
print("/////////////////////////")
print (resultado)

print("/////////////////////////")

#\s -- busca espacios en blanco, tabs y saltos de linea

resultado = re.findall(r"\s", texto)
print("/////////////////////////")
print (resultado)
print("/////////////////////////")

#\S -- busca todo menos espacios en blanco, tabs y saltos de linea

resultado = re.findall(r"\S", texto)
print("/////////////////////////")
print (resultado)
print("/////////////////////////")

#\. -- busca todo menos saltos de linea

resultado = re.findall(r"\s", texto)
print("/////////////////////////")
print (resultado)
print("/////////////////////////")

#\n -- busca saltos de linea

resultado = re.findall(r"\n", texto)
print("/////////////////////////")
print (resultado)
print("/////////////////////////")

#\ -- Cancela caracteres especiales, cancelando la funcion del punto y buscando puntos

resultado = re.findall(r"\.", texto)
print("/////////////////////////")
print (resultado)
print("/////////////////////////")

#armando una cadena que busque un numero seguido de un punto y espacio

resultado = re.findall(r"\d\.\s", texto)
print("/////////////////////////")
print(resultado)
print("/////////////////////////")

#^ -- busca el comienzo de una linea se usa en conjunto con una palabra

resultado = re.findall(r'^Hola', texto) #con el parametro flags=M se activa la multilinea y lo busca cada salto de pagina
print("/////////////////////////")
print (resultado)
print("/////////////////////////")

#$ -- busca el final de una linea se usa en conjunto con una palabra

resultado = re.findall(r'Hola$', texto, flags=M) #con el parametro flags=M se activa la multilinea y lo busca cada salto de pagina
print("/////////////////////////")
print (resultado)
print("/////////////////////////")

#{n} -- busca n cantidad de veces el valor de la izquierda
#{n,m} -- n siendo el menor y m siendo mayor se utiliza para buscar en un intervalo de veces
# se pueden usar grupos ejemplo (ab){n,m} buscando el valor ab en toda la cadena desde hasta tantas veces que se indique
#nota una cosa es lo que encuentra y otra lo que devuelve, le estamos diciendo al programa que si encuentra "ab" tantas veces{n,b} mostrar (ab), siendo (ab) lo que tiene que buscar
#con corchetes busca [ab] aa, bb, ab, ba, siendo {n} un numero determinado de veces

resultado = re.findall(r'\d{2}', texto) #{3}encuentra 3 numeros juntos o lo que sea que tenga un patron 
print("/////////////////////////")
print (resultado)
print("/////////////////////////")

# | -- busca una cosa o la otra
resultado = re.findall(r'\d{2}| hola', texto)
print("/////////////////////////")
print (resultado)
print("/////////////////////////")