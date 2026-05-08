n_autos = int(input("Ingrese la cantidad de autos:"))
total_1 = 0
total_2 = 0
total_3 = 0
total_g = 0

for i in range(n_autos):
    clave = int(input("Ingrese la clave del auto (1, 2 o 3):"))
    costo = float(input("Ingrese el valor del auto:"))

    if clave == 1:
        impuesto = costo * 0.10
        total_1 = total_1 + impuesto
    elif clave == 2:
        impuesto = costo * 0.07
        total_2 = total_2 + impuesto
    elif clave == 3:
        impuesto = costo * 0.05
        total_3 = total_3 + impuesto
    else:
        print("Error:Clave no valida, el impuesto sera de 0%")
    total_g = total_g + impuesto
    print(f"Impuesto a pagar por este auto:${impuesto:.2f}")

print(f"Total categoria 1:${total_1:.2f}")
print(f"Total categoria 2:${total_2:.2f}")
print(f"Total categoria 3:${total_3:.2f}")
print(f"Total general:${total_g:.2f}")
