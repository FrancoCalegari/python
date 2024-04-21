class MiExepcion(Exception): #creanso esepcion personalizada
    def __init__(self, err):
        print(f"Impresionante, Cometiste errores,{err}")
#forzando error para mostrar que funciona
#raise ZeroDivisionError("Que boludo la cagaste")


#manejando
try:
    raise ZeroDivisionError("Que boludo la cagaste")
except:
    print("Sos un weon como te vas a equivocar?")