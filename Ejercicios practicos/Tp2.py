#falto el profe y los pibes van a armar la clse
#anotar el nombre y la edad de los compañeros si vinieron hoy a clase

#Funcion para obtener al asistente y al profesor segun la edad
def obtenerCompañeros(cantidad):
    compañeros = [] #creando la lista de compañeros
    for i in range(cantidad):
        nombre = str(input("Ingresar Nombre del compañero:"))
        edad = int(input("Ingresar Edad del compañero:"))
        compañero = (nombre, edad) #se agrega nombre y edad en compañero
        compañeros.append(compañero)#agregando informacion a la lista
    compañeros.sort(key=lambda x:x[1])#ordenando segun edad
    asistente = compañeros[0][0]#definiendo el asistente y profe
    profesor = compañeros[-1][0]
    return asistente,profesor #retornamos tupla

asistente, profesor = obtenerCompañeros(5) #desempaquetamos lo que nos retorna la funcion
print(f"El profesor es {profesor} y su asistente es {asistente}") #se muestra en pantalla


print("////////////////////////")
#una funcion que verifica si es primo
def esPrimo(num):
    #verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1

    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
        #si termina el bucle significa que no fue dibisible entonces es primo
    return True

#creando una funcion que devuelve la lista de los numeros primos
def eshasta(num):
    primos = [] #creamos una lista
    for i in range(3,num+1): #verificamos si el valor es primo
        resultado = esPrimo(i) #en caso de que sa lo agregamos a la lista
        if resultado == True: primos.append(i)
    return primos # devolvemos a la lista
# se muestra en pantalla
resultado = eshasta(98)
print(resultado)

#fivonachi python entre 0 y numero dado

def fibo(num):
    a,b= 0,1
    fiboLista = [0]
    for i in range(num):
        if b > num: return fiboLista
        else:
            fiboLista.append(b)
            a,b = b,a+b

resultado = fibo(30)
print(resultado)
