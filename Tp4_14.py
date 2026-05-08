elementos = 100
vector = [0.0] * elementos
suma_cuadrados = 0

for i in range(elementos):
    valor = float(input(f"Ingrese el valor {i+1}: "))
    vector[i] = valor
    suma_cuadrados = suma_cuadrados + (valor * valor)

magnitud = suma_cuadrados ** 0.5

print(f"La magnitud calculada es:{magnitud}")