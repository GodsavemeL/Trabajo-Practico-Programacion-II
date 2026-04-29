dias = int(input("Ingrese la cantidad de dias del viaje:"))
hotel = int(input("Ingrese los gastos diarios por hotel:"))
comida = int(input("Ingrese los gastos diarios por comida:"))
gasto_diario = 100.00
cheque = dias * (hotel + comida + gasto_diario)
print(f"El gasto total es de:{cheque}")
print(f"El gasto por comida es de:{comida}")
print(f"El gasto por hotel es de:{hotel}")
