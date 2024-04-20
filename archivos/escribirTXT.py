with open('archivos/info.txt', 'w', encoding="utf-8" ) as archivo:
    #esta parte sobreescribe el archivo
    #archivo.write("Te cambiamos todo jaja")
    archivo.writelines(["Hola como ests?\n", "Bien esto es una lista jdasj\n"])
    archivo.writelines(["esto se puede acumular y queda increible\n", "Bien esto es una lista jdasj\n"])
    

#forma universal del salto de linea en codigo "\n"
#como nota el 'w' que significa write borra todo el archivo y lo escribe denuevo mientras 'a' agrega al archivo