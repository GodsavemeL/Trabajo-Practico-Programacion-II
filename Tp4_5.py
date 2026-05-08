# Entrada de dimensiones
m = int(input("Ingrese numero de filas: "))
n = int(input("Ingrese numero de columnas: "))

if m != n:
    print("La matriz debe ser cuadrada para ser diagonal.")
else:
    matriz = []
    es_diagonal = True 
    
    for i in range(m):
        fila = []
        for j in range(n):
            valor = float(input(f"Elemento [{i}][{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    
    for i in range(m):
        for j in range(n):
            if i != j and matriz[i][j] != 0:
                es_diagonal = False
    
    if es_diagonal:
        print("Es una matriz diagonal.")
    else:
        print("No es una matriz diagonal.")