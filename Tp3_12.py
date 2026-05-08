total_b = 0
total_m = 0
n = int(input("Cuantos ingresos de dinero realizara en total?:"))

for dinero in range(n):
    tipo = input(f"Ingreso {dinero} - Es billete (B) o moneda (M):")
    valor = float(input("Ingrese el valor:"))
    cantidad = int(input("Ingrese la cantidad de unidad:"))
    if tipo == "B":
        total_b = total_b + (valor * cantidad)
    elif tipo == "M":
        total_m = total_m + (valor * cantidad)
    else:
        print("Tipo no conocido, no se sumara al final.")

total_g = total_b + total_m
print(f"Total de billetes:${total_b}")
print(f"Total de monedas:${total_m}")
print(f"Total en General:${total_g}")
