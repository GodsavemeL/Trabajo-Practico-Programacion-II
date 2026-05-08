n_ventas = int(input("Ingrese el numero total de ventas:"))
menor_10k = 0
mayor_20k = 0
entre_10k_20k = 0
monto_total = 0

for i in range(n_ventas):
    venta = float(input(f"Ingrese el valor de la venta {i+1}:"))
    monto_total = monto_total + venta
    if venta <= 10000:
        menor_10k = menor_10k + 1
    elif venta < 20000:
        entre_10k_20k = entre_10k_20k + 1
    else:
        mayor_20k = mayor_20k + 1

print(f"Ventas menores de 10k:{menor_10k}")
print(f"Ventas entre 10k y 20k:{entre_10k_20k}")
print(f"Ventas mayores de 20k:{mayor_20k}")
print(f"Venta total:{monto_total}")
