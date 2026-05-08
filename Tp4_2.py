# Entrada de dimensiones
m = int(input("Filas Matriz A (M): "))
n = int(input("Columnas Matriz A (N): "))
p = int(input("Filas Matriz B (P): "))
q = int(input("Columnas Matriz B (Q): "))

if n != p:
    print("Error:El numero de columnas de A debe ser igual a las filas de B")
else:
    matriz_a = []
    print("Ingrese Matriz A:")
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append(float(input(f"A[{i+1}][{j+1}]: ")))
        matriz_a.append(fila)
    matriz_b = []
    print("Ingrese Matriz B:")
    for i in range(p):
        fila = []
        for j in range(q):
            fila.append(float(input(f"B[{i+1}][{j+1}]: ")))
        matriz_b.append(fila)
    matriz_c = []
    for i in range(m):
        matriz_c.append(* q)
    for i in range(m):        
        for j in range(q):    
            for k in range(n): 
                matriz_c[i][j] += matriz_a[i][k] * matriz_b[k][j]

    print("Matriz Resultante A x B:")
    for fila in matriz_c:
        print(fila)