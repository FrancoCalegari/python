import csv
with open("archivos/datos.csv") as archivo:
    print("data leida correctamente")
    reader = csv.reader(archivo)
    for row in reader:
        print(row)

