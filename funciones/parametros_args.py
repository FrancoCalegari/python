#forma no optima de sumar valores

def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados= numeros_sumados + numero
    return numeros_sumados



resultado = suma([5,1,5,51,6,5,1,685,])
print(resultado)

print("//////////////////////////////")

#forma optima

#utilizando el parametro args * como argumento (*args)

def suma1(nombres,*numeros1):#si se utiliza este metodo no se pueden agregar mas valores ya que nunca va detectar cuando usar el otro valor
   return f"{nombres} la suma de tus numeros es {sum(numeros1)}"

resultado1 = suma1("Franco",2,3,2,263,2,61265,1)
print(resultado1)


#forma optima de sumar valores
print("//////////////////////////////")
def suma_total(numeros3):
    return sum([*numeros3])#en cambio este si ya que se lo estamos pasando por separado
    

resultado3 = suma_total([5,1,5,51,6,5,1,685])
print(resultado3)

print("//////////////////////////////")