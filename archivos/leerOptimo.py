#abriendo archivo con with open
with open('archivos/info.txt', encoding="utf-8") as archivo:
    #leemos el archivo
    contentenido = archivo.read()
    #mostramos el archivo
    print(archivo.read())

#no es necesario cerrar el archivo como en el caso anterior y consume menos recursos teniendo menos esepciones