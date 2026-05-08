filas, columnas = 6, 8
matriz = [ [0] * columnas for _ in range(filas)]

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = float(input(f"Valor en [{f}][{c}]: "))

fila_encontrada = -1
col_encontrada = -1

for f in range(filas):
    for c in range(columnas):
        if matriz[f][c] < 0:
            fila_encontrada = f
            col_encontrada = c
            break
    if fila_encontrada != -1:
        break

if fila_encontrada != -1:
    print(f"Negativo localizado en: Fila {fila_encontrada}, Columna {col_encontrada}")
else:
    print("No se hallaron valores negativos.")