n_hamb = int(input("Ingrese el numero de hamburguesas:"))
total = 0

for i in range(n_hamb):
    tipo_h = input(f"Hamburguesa {i+1} Elige: Sencilla (S), Doble (D) Triple (T):").upper()
    if tipo_h == "S":
        total = total + 20
    elif tipo_h == "D":
        total = total + 25
    elif tipo_h == "T":
        total = total + 28

pago_tarjeta = input("¿Paga con tarjeta de credito? S/N:").upper()
if pago_tarjeta == "S":
    cargo = 0.05
    total_f = total + (total * cargo)
elif pago_tarjeta ==  "N":
    total_f = total
else:
    print("Error:Solo elige S/N")

print(f"Total a pagar:${total_f}")