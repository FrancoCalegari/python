import datetime
import time

# Usamos un bucle while verdadero (True) para ejecutar continuamente
while True:
    # Obtenemos la hora actual en formato de tiempo
    
    horaactual = datetime.datetime.now()
    # Formateamos la hora, minutos y segundos
    hora = horaactual.strftime("%H")
    minutos = horaactual.strftime("%M")
    segundos = horaactual.strftime("%S")

    # Imprimimos la hora actual
    print(f"{hora}:{minutos}:{segundos}")

    # Esperamos 1 segundo antes de la próxima iteració
    time.sleep(1)