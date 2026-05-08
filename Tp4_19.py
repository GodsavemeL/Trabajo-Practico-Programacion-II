r = int(input("Número de renglones (R): "))
c = int(input("Número de columnas (C): "))

matriz = [[0.0 for _ in range(c)] for _ in range(r)]
suma_renglones = [0.0] * r
suma_columnas = [0.0] * c
for i in range(r):
    for j in range(c):
        valor = float(input(f"Matriz[{i}][{j}]: "))
        matriz[i][j] = valor
        suma_renglones[i] += valor
        suma_columnas[j] += valor

print(f"Suma de cada renglón: {suma_renglones}")
print(f"Suma de cada columna: {suma_columnas}")
