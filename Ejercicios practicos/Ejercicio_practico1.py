#duraciones

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4

Dalto_curso = 1.5

#diferencias de duracion en porcentaje

diferencia_min = 100 - Dalto_curso / otros_cursos_min * 100
diferencia_max = 100 - Dalto_curso *1000 // otros_cursos_max / 10
diferencia_promedio = 100 - Dalto_curso / otros_cursos_promedio * 100


print("/////////")
print("El curso de dalto dura:")
print(f"el curso de Dalto dura un {diferencia_min}% menos que el mas rapido de otors cursos")

print(f"el curso de Dalto dura un {diferencia_max}% menos que el mas lento de otors cursos")

print(f"el curso de Dalto dura un {diferencia_promedio}% menos que el promedio de otors cursos")



#calculo de diferencias tiempo vacio
crudo_promedio = 5
dalto_crudo = 3.5

tiempo_vacio_Promedio = 100 - otros_cursos_promedio *1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - Dalto_curso *1000 // dalto_crudo / 10

print("/////////")
print("")
print(f"Un curso promedio elimina un {tiempo_vacio_Promedio}% de tiempo vacio")
print(f"Dalto elimina un {tiempo_vacio_dalto}% de tiempo vacio")
print("/////////")

#mostrando diferencias de 10 horas

print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // Dalto_curso / 10} horas de otros cursos")
print(f"Ver 10 horas otros cursos equivale a ver {Dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso")

#Segundo Ejercicio

#datos

persona_Promedio_palabras = 2
persona_Promedio_segundos = 1
minutos = 1

#en esta seccion le preguntamos al usuario una frase
frase = input("Decime una frase maestro y te calculo cuanto te tardarias en decrilo: ")
#en esta parte procesamos lo ingresado por el usuario separando las palabras y luego contandolas
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
#mostramos al usuario los resultados
print(f"dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras*100//2 /1.3/100}")

if cantidad_de_palabras > 120:
    print("mucho texto man")