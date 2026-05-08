inversion_m = float(input("Ingrese el Deposito Mensual:"))
n_anios = int(input("Ingrese cantidad de años:"))
total = 0
intereses = 0.10

for año in range(n_anios):
    total = total + (inversion_m * 12)
    total = total (total * intereses)
    print(f"Inversion Final año {n_anios}:${total:.2f}")
