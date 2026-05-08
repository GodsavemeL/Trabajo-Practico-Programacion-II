cantidad_a = int(input("Ingrese la cantidad de alumnos que van al viaje:"))

if cantidad_a > 100:
    boleto = 20
elif cantidad_a >= 50:
    boleto = 35
elif cantidad_a >=20:
    boleto = 40
else:
    boleto = 70

print(f"El costo de pasaje para los {cantidad_a} alumnos es un total de:${boleto}")
print(f"El costo total es de:{boleto * cantidad_a}")
