puntos = int(input("Ingrese los puntos del profesor:"))
sueldo_m = int(input("Ingrese su sueldo minimo:"))

if puntos <= 100:
    salario = 1
elif puntos <= 150:
    salario = 2
else:
    salario = 3

print(f"El profesor tiene un total de {puntos} puntos y tiene un total de {salario} salario/s minimos.")
print(f"Su sueldo total es de:${sueldo_m * salario}.")
