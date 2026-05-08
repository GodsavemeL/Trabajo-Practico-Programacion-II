m = int(input("Fila de la matriz A:"))
n = int(input("Columna de la matriz A:"))
p = int(input("Fila de la matriz B:"))
q = int(input("Columna de la matriz B:"))

if n != p:
    print("Error:El numero de columnas de A debe ser igual a las filas del B")
else:
    for i in range(m):
        for j in range(q):
            suma = 0
            for k in range(n):
                a = float(input(f"A [{i}] [{k}]:"))
                b = float(input(f"B [{k}] [{j}]:"))
                suma = suma + (a * b)
            print(f"Resultado en [{i}] [{j}]:{suma}")


    i = 1
    while i <=  m:
        j = 1
        while j <= q:
            suma = 0
            k = 1
            while k <= n:
                a = float(input(f"A [{i}] [{k}]"))
                b = float(input(f"B [{k}] [{j}]"))
                suma = suma + (a * b)
                k = k + 1
            print(f"Resultado en [{i}] [{j}]: {suma}")
            j = j + 1
        i = i + 1
        