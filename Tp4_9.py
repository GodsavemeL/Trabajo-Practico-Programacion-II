filas = 15
columnas = 12
matriz = [[0] * columnas for _ in range(filas)]

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(input(f"Ingrese valor en [{f}][{c}]: "))

menor = matriz[0][0]
suma_primeras_cinco = 0
total_negativos = 0

for f in range(filas):
    for c in range(columnas):
        valor_actual = matriz[f][c]
        if valor_actual < menor:
            menor = valor_actual
            
        if f < 5:
            suma_primeras_cinco += valor_actual
            
        if 4 <= c <= 8:
            if valor_actual < 0:
                total_negativos += 1

print(f"Elemento menor: {menor}")
print(f"Suma primeras 5 filas: {suma_primeras_cinco}")
print(f"Total negativos en columnas 5-9: {total_negativos}")