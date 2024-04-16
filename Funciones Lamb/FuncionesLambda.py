#es una forma de ahorrar codigo ya que es una funcion anonima
multiplicar_por_dos = lambda x : x*2
#por ejemplo se llama a la funcion y se ingresa un parametro x sirve para true o false
print(multiplicar_por_dos(5))


numeros = (5,2,74,5,6,2,4,5)
#creando funcion comun que diga si es par o no
def es_par(num):
    if (num%2==0):
        return True
    
#usando filter con una funcion comun

numeros_pares = filter(es_par, numeros)

print(list(numeros_pares))