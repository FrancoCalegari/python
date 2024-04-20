# #se importa el archivo desde la carpeta que se utiliza y se espesifica utf-8 para evitar errores
# archivo = open("archivos/info.txt", encoding="utf-8")
# #luego se gurada el contenido en una variable haciendo que se lea el contendio del archivo
# archivoleer = archivo.read()
# #se muestra en pantalla
# print(archivoleer)

print("///////////////////")
#se importa el archivo desde la carpeta que se utiliza y se espesifica utf-8 para evitar errores
archivo = open('archivos/info.txt', encoding="utf-8")
#luego se gurada el contenido en una variable haciendo que se lea el contendio del archivo
# archivoleer = archivo.read()
#retornar solo la primera linea del archivo de texto
linea1 = archivo.readlines()
archivo.close
#se muestra en pantalla
print(linea1)

print("///////////////////")