dinero = int(input("Ingrese su presupuesto total:"))

if dinero < 10000:
    paq = "Paquete D"
    cont = "1 Par de zapatos, 2 Camisas y 2 Pantalones."
elif dinero < 20000:
    paq = "Paquete C"
    cont = "2 Pares de zapato, 3 Camisas y 3 Pantalones."
elif dinero < 50000:
    paq = "Paquete B"
    cont = "1 Grabadora, 3 Pares de zapato, 5 Camisas y 5 Pantalones"
else:
    paq = "Paquete A"
    cont = "1 Television, 1 Modular, 3 Pares de zapato, 5 Camisas y 5 Pantalones."

print(f"Puedes pagarte el {paq} y contiene:")
print(f"{cont}")
