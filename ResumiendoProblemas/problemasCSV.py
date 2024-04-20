#cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("ResumiendoProblemas/datos.csv")
#convertir a string los datos de una columna
df["edad"] = df['edad'].astype(str)
#print(type(df['edad'][0]))


#remplazando los datos Franco por maestro
df['nombre'].replace("Franco", "maestro", inplace=True)
print(df['nombre'])

#eliminar filas faltantes

df = df.dropna()#se pueden eliminaar columnas agregando axixs=1
print(df)

#eliminar filas duplicadas

df = df.drop_duplicates()
print(df)



#creando un csv con eldata frame limpio
df.to_csv("ResumiendoProblemas/datos_limpios.csv")
print("conversion completa")