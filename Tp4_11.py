n = 12
m1 = [[0]*n for _ in range(n)]
m2 = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        m1[i][j] = int(input(f"M1 [{i}][{j}]: "))
        m2[i][j] = int(input(f"M2 [{i}][{j}]: "))

diagonales_identicas = True

for i in range(n):
    if m1[i][i] != m2[i][i]:
        diagonales_identicas = False
        break 

if diagonales_identicas:
    print("Las diagonales son iguales.")
else:
    print("Las diagonales no son iguales.")