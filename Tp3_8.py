n_art = int(input("Ingrese la cantidad de articulos:"))
valor_total = 0
pago_total = 0

for i in range(n_art):
    valor_art = float(input(f"Ingrese el valor del {i+1} articulo:"))
    if valor_art >= 200:
        desc = 0.15
        costo_total = valor_art - (valor_art * desc)
        pago_total = pago_total + valor_art
    elif valor_art > 100:
        desc = 0.12
        costo_total = valor_art - (valor_art * desc)
        pago_total = pago_total + valor_art
    else:
        desc = 0.10
        costo_total = valor_art - (valor_art * desc)
        pago_total = pago_total + valor_art

print(f"Los articulos cuestan:${pago_total}")
