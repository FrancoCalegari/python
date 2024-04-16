#creando las listas

frutas = ["banana", "manzana", "ciruela", "granada", "durazno"]
cadena = "Hola Franco"
numeros = [2,5,6,10]


#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"Me voy a comer una {fruta}")

print("/////////")

#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)

for fruta in frutas:
    if fruta == "ciruela":
        break
    print(f"Me voy a comer una {fruta}")

#iterar una cadena de texto
print("/////////")
for letra in cadena:
    print(letra)

print("/////////")
#for en una sola linea de codigo (Duplicamos los numeros)
            #numeros_duplicados = list()
            #for num in numeros:
            # numeros_duplicados.append(num*2)
            # print(numeros_duplicados)


numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
