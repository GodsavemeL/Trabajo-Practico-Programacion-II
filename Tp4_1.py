m = int(input("Ingrese el numero de filas (M): "))
n = int(input("Ingrese el numero de columnas (N): "))

matriz = []
for i in range(m):
    fila = []
    for j in range(n):
        valor = float(input(f"Elemento [{i+1}][{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)

transpuesta = []
for i in range(n):
    fila_t = [0] * m
    transpuesta.append(fila_t)


for i in range(m):
    for j in range(n):
        transpuesta[j][i] = matriz[i][j]

print("Matriz original:")
for fila in matriz:
    print(fila)

print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)