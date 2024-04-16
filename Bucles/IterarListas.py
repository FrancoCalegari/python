animales = ["gato", "perro", "jirafa"]
numeros = [11,55,22]

#for animal in animales:
    #print(animal)


#iterando dos listas del mismo tamaño al mismo tiempo
for animal,numero in zip(animales,numeros):
    print(f"Los animales: {animal}")
    print(f"Los animales: {numero}")


#iterando for con range

for num in range(0,20):
    print(num)

print("//////////")

#forma no optima de recorrer una lista

for num in range(len(numeros)):
    print(numeros[num])

print("//////////")
#forma correcta de recorrer una lista con su inidce

for num in enumerate(numeros):
        print(type(num))

print("//////////")

for num in enumerate(numeros):
        indice = num[0]
        valor = num[1]
        print(f"el indice es {indice} y su valor es {valor}")

#usando el else
print("//////////")

for numero in numeros:
      print(f"ejecutando el ultimo bucle, valor actual {numero}")
else:
      print("el bucle termino")

#si se usa lista o tubpla funciona exactamente igual para tuplas y listas