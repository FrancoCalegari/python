def sumar_dos(): #creamos una funcion donde sume numeros

    while True:#creamos un bucle
        a = input("Numero 1: ")#pedimos dato al usuario
        b = input("Numero 2: ")    
        try:#probamos a sumar el resultado
            resultado = int(a) + int(b) #los convertimos a enteros
            break
        except:#en caso de tirar una esepcion le pedimos al usuario que ingrese otra vez #se pueden detectar varios errores del padre Exeption
            print("Te pedi un numero Flaco")
    return resultado #una vez que se vuelva verdad retorna el resultado mientras tanto siempre sera false
#se llama a la funcion
print(sumar_dos())