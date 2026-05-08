vector_a = [0] * 100
vector_b = [0] * 100
vector_suma = [0] * 100

print("Ingreso de datos para los vectores (100 elementos)")
for i in range(100):
    vector_a[i] = float(input(f"Vector A - Elemento {i+1}: "))
    vector_b[i] = float(input(f"Vector B - Elemento {i+1}: "))

for i in range(100):
    vector_suma[i] = vector_a[i] + vector_b[i]

print("Resultado de la suma")
for i in range(100):
    print(f"Índice {i}: {vector_a[i]} + {vector_b[i]} = {vector_suma[i]}")