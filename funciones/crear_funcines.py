#creando una funcion simple

def amar():
    print("loco como te amo chemy amor de mi vida")

amar()

#crear una funcion que tenga parametros

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        print(f"hola {nombre} eres una hermosura")
    elif (sexo == "hombre"):
        print(f"hola {nombre} eres un galan")
    else:
        print("che me tenes que decir que sos y que genero rey")

saludar("Chemy","mujer")
saludar("Franco","hombre")
saludar("Gabi","Spiderman")


#crear una funcion que nos retorne valores

def crear_contraseña(num):
    chars = "abcdefg"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num
    c4 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c3]}{num_entero*2}"
    return contraseña,num#este nos retorna el valor, sin esto no me daria el dato
   
#desempaquetando la funcion
pasdas,num = crear_contraseña(16541)

frase = f"tu contraseña es: {pasdas}"

#mostrando la funcion y los datos desempaquetados

print(f"tu contraseña es {pasdas}")
print(f"y el numero utilizado fue {num}")
