diccionario = {
    "Nombre": "Chemy",
    "Estado civil": "Casada",
    "plata en el banco": 100000
}

#recorriendo diccionario para obtener las claves

for key in diccionario.items():
    print(f"la clave es: {key}")

print("////////")

#recorriendo diccionario con items() para obtener la clave y valor


for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es {key} y el valor es {value}")

print("////////")