m = int(input("Filas (M): "))
n = int(input("Columnas (N): "))

print("Matriz A:")
a = []
for i in range(m):
    fila = []
    for j in range(n):
        fila.append(float(input(f"A[{i}][{j}]: ")))
    a.append(fila)
print("Matriz B:")
b = []
for i in range(m):
    fila = []
    for j in range(n):
        fila.append(float(input(f"B[{i}][{j}]: ")))
    b.append(fila)

c = []
for i in range(m):
    fila_resta = []
    for j in range(n):
        resultado = a[i][j] - b[i][j]
        fila_resta.append(resultado)
    c.append(fila_resta)

print("Resultado A - B:")
for fila in c:
    print(fila)