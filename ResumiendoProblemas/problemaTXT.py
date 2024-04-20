#dos listas una con nombres otra con apellidos

nombres = ["Franco", "Daniela", "Josefina", "Agostina"]
apellidos = ["Calegari", "Olmedo", "Adamo", "Nazi"]

#Registrar esta informacion en txt

with open('ResumiendoProblemas/datos.txt', 'w', encoding="utf-8") as archivo:
    archivo.writelines("Los datos son: \n")
    [archivo.writelines(f"Nombre: {n}\nApellido: {a}\n-------\n")for n,a in zip(nombres,apellidos)]
    print("Traspaso completo")


