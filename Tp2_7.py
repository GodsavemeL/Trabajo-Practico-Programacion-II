edad = int(input("Ingrese la edad:"))
promedio = float(input("Ingrese el promedio:"))
if edad > 18:
    if promedio >= 9:
        beca = 2000
    elif promedio >= 7.5:
        beca = 1000
    elif promedio >= 6:
        beca = 500
    else:
        beca = 0
else:
    if promedio >= 9:
        beca = 3000
    elif promedio >= 8:
        beca = 2000
    elif promedio >= 6:
        beca = 100
    else:
        beca = 0
if beca > 0:
    print(f"El valor de tu beca es:${beca}")
else:
    print("Estudia mas para la proxima vez.")
    