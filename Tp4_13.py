notas = [0.0] * 100
suma = 0

for i in range(100):
    notas[i] = float(input(f"Calificacion estudiante {i+1}: "))
    suma += notas[i]

promedio = suma / 100

estudiantes_arriba = 0
for i in range(100):
    if notas[i] > promedio:
        estudiantes_arriba += 1

print(f"Promedio grupal: {promedio:.2f}")
print(f"Estudiantes con mejor promedio: {estudiantes_arriba}")