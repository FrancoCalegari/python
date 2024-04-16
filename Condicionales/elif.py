Ingreso_mensual = 81000
gasto_mensual = 80000

#if elif anidados

if Ingreso_mensual > 10000:
    if Ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif Ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien rey")
    else:
        print("estas gastando mucho rey bajale al consumo")

elif Ingreso_mensual >= 1000:
    print("estas bien en Latinoamerica")

elif Ingreso_mensual >= 500:
    print("Estas bien en Argentina")

else:
    print("Sos pobre")