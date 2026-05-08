m = int(input("Ingrese filas (M): "))
n = int(input("Ingrese columnas (N): "))

matriz = []
for i in range(m):
    fila = []
    for j in range(n):
        valor = float(input(f"Elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

suma_diagonal = 0
for i in range(m):
    for j in range(n):
        if i == j:
            suma_diagonal += matriz[i][j]

print(f"La suma de la diagonal es: {suma_diagonal}")