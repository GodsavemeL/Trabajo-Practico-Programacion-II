n = 5
matriz = [[0.0 for _ in range(n)] for _ in range(n)]

for f in range(n):
    for c in range(n):
        matriz[f][c] = float(input(f"Elemento [{f}][{c}]: "))

producto_diagonal = 1.0
for i in range(n):
    producto_diagonal *= matriz[i][i]

print(f"Resultado del producto de la diagonal: {producto_diagonal}")