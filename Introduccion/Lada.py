tiempollamada = float(input("Introduce el tiempo de tu llamada: "))
clave = int(input("Introduce tu clave LADA: "))

if clave == 12:
    tiempollamada *= 2  # Multiplica tiempollamada por 2 si la clave es 12
    print(tiempollamada)
elif clave == 15:
    tiempollamada *= 2.2
    print(tiempollamada)
elif clave == 18:
    tiempollamada *= 4.5
    print(tiempollamada)
elif clave == 19:
    tiempollamada *= 3.5
    print(tiempollamada)
elif clave == 23:
    tiempollamada *= 6
    print(tiempollamada)
elif clave == 25:
    tiempollamada *= 6
    print(tiempollamada)
elif clave == 29:
    tiempollamada *= 5
    print(tiempollamada)
else:
    print ("La clave LADA que indicaste no existe.")
