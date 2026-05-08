n = 5
matriz = [[0 for _ in range(n)] for _ in range(n)]
pares = 0
impares = 0

for f in range(n):
    for c in range(n):
        valor = int(input(f"Elemento [{f}][{c}]: "))
        matriz[f][c] = valor
        
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1

print(f"Cantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")