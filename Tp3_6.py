m = int(input("Ingrese el numero de filas:"))
n = int(input("Ingrese el numero de columnas:"))
#Ciclo for
for i in range(m):
    for h in range (n):
        valor = float(input(f"Ingrese un valor en la posicion original [{h}] [{i}]:"))

print(f"Ahora el valor cambiara de posicion [{i}] [{h}].")

#Ciclo While
i = 1
while i <= n:
    h = 1
    while h <= m:
        valor_2 = float(input("Valor original [{i}] [{h}]:"))
        print(f"La transpuesta es [{h}] [{i}]")
        h = h + 1
    i = i + 1

