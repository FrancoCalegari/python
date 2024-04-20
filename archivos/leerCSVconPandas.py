import pandas as pd
#usando la funcion read_csv para leer el archivo csv
df = pd.read_csv("archivos/datos.csv") #names=["name","lastname","age"])
df2 = pd.read_csv("archivos/datos.csv")

print(df)#data frame es "df"

nombres = df["nombre"]

cadena = "123456789"

print(cadena[1:3]) #1:2 slizing desde tal numero hasta tal numero

#ordenar de mayor a menor

dfOrdenAcendente = df.sort_values("edad")#orendando de menor a mayor

print("////////////")
#dataframe ordenado
print(dfOrdenAcendente)#de menor a mayor
print("////////////")
dfOrdenDecreciente = df.sort_values("edad", ascending=False)#de mayor a menor
print(dfOrdenDecreciente)

print("////////////")
#vamos a concatenarlos los dos df
dfConcatenado = pd.concat([df,df2])
print(dfConcatenado)

print("////////////")
#acediendo a la primer fila con head() y tambien a las primeras 3 filas de arriba hacia abajo
primerasFilas = df.head(1)
print(primerasFilas)
##acediendo a la primer fila con tail() y tambien a las ultimas 3 filas de abajo hacia arriba
primerasUltimas = df.tail(1)
print(primerasUltimas)
print("////////////")
#acediendo a la cantidad de filas y columnas con shape
filasTotales,columnasTotales = df.shape #desempaquetamos
print(f"estas son las filas totales: {filasTotales}")
print(f"estas son las columnas totales: {columnasTotales}")
print("////////////")
#obteniendo data analitica de dataframe
dfInfo = df.describe()
print(dfInfo)

print("////////////")
#accedieno a un elemento espesifico con loc
elementoEspesifico = df.loc[2, "edad"] #accediendo a la edad de la fila 2
print(elementoEspesifico)
#accedieno a un elemento espesifico con iloc #la "i" es de indice
elementoEspesifico = df.iloc[2, 2]#accediendo a la edad de la fila 2 con iloc
print(elementoEspesifico)

print("////////////")
#accediendo a todas las filas de una columna loc
apellidos_loc = df.loc[:,"apellido"]
print(apellidos_loc)

#accediendo a todas las filas de una columna iloc
apellidos = df.iloc[:,1]
print(apellidos)

print("////////////")
#acediendo a la fila 3 con loc
fila3 = df.loc[2,:]
print(fila3)

#acediendo a la fila 3 con iloc #en este caso es lo mismo porque funciona asi
fila3 = df.iloc[2,:]
print(fila3)
print("////////////")
#accediedno a filas con edad mayor que 30
mayorQue30 = df.loc[df["edad"]>30,:]

print(mayorQue30)
print("////////////")