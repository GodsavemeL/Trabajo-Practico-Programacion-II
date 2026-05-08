matriz = [[0] * 6 for _ in range(5)]
negativos = 0
ceros_diagonal = 0

for f in range(5):
    for c in range(6):
        matriz[f][c] = int(input(f"Valor en [{f}][{c}]: "))
        
        if matriz[f][c] < 0:
            negativos += 1
            
        if f == c and matriz[f][c] == 0:
            ceros_diagonal += 1

print(f"Cantidad de negativos: {negativos}")
print(f"Ceros en diagonal principal: {ceros_diagonal}")