filas = 12
columnas = 19
matriz = [[0] * columnas for _ in range(filas)]

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = float(input(f"Elemento [{f}][{c}]: "))

for f in range(filas):
    for c in range(columnas):
        if matriz[f][c] < 0:
            matriz[f][c] = 0

print("Matriz final:")
for fila in matriz:
    print(fila)