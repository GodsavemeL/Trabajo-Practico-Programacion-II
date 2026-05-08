estacionamiento = int(input("Ingrese las horas estacionadas:"))
if estacionamiento <= 2:
    pago = estacionamiento * 5
elif estacionamiento <= 5:
    pago = ((2 * 5) + (estacionamiento - 2) * 4)
elif estacionamiento <= 10 :
    pago = ((2 * 5) + (3 * 4) + (estacionamiento - 5) * 3)
else:
    pago = ((2 * 5) + (3 * 4) + (5 * 3) + (estacionamiento - 10) * 2)
print(f"El total a pagar es:${pago}")
