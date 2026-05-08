n = 10
v_fila = [0.0] * n
v_columna = [0.0] * n
producto_punto = 0

print("Ingreso de elementos para los vectores:")
for i in range(n):
    v_fila[i] = float(input(f"Fila - Posicion {i+1}: "))
    v_columna[i] = float(input(f"Columna - Posicion {i+1}: "))

for i in range(n):
    producto_punto += v_fila[i] * v_columna[i]

print(f"El producto escalar es: {producto_punto}")