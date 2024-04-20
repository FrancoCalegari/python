with open('archivos/info.txt', 'a', encoding="utf-8" ) as archivo:
    #esta parte sobreescribe el archivo
    for i in range(5):
        archivo.write(f"Hola como estan todos {i +1}\n")