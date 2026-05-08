salario = 1500
incremento = 1.10

for año in range(1, 7):
    salario = salario * 1.10
    print(f"Año {año}:${salario:,.2f}")

print(f"Salario total de los 6 años:${salario:,.2f}")

