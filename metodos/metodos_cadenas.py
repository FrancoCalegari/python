cadena = "hola"
cadena2 = "como estas"

#convierte a mayusculas
mayusc = cadena.upper()

#primera letra en minusculas

minusc = cadena.lower()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
primera_letra_mayusc = cadena.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion

busqueda_find = cadena.find("a")

#buscamos una cadena en otra cadena, si no se encuentra lanza una exepcion

busqueda_index = cadena.index("o")

# si es numerico muestra true

esnumerico = cadena.isnumeric()

#si es alfa numerico devuelve true, solo funciona si son solo letras sin espacios

esalpha = cadena.isalpha()

#devuelve el numero de ocurrencias de una subcadena en la cadena dada, cuenta cuantas veces se encuentra algo

contar_coincidencias = cadena.count("a")

#cuenta los caracteres de una cadena

contar_caracteres = len(cadena)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true

empieza_con = cadena.startswith("ho")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena.endswith("la")

# remplaza un pedaza de la cadena dada por otra, siempre y cuando en el valor 1 sea encontrado, en el ejemplo si encuentra "la" lo remplaza por "lu"

cadena_nueva = cadena.replace("la","lu")

#separar cadenas por la cadena que le pasemos y lo separa en una lista, el resultado es una lista de lo que sepaaro en la cadena

cadena_separada = cadena.split(",")



