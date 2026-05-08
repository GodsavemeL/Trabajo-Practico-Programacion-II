num = float(input("Ingrese el numero que quiera ver su tabla:"))

for numero in range(1, 11):
    resultado = num * numero

    print(f"{num:.0f} X {numero:.0f}:{resultado:.0f}")

