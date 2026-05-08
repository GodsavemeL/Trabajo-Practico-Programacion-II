n_salones = int(input("Ingrese la cantidad de salones:"))
suma_total_esc = 0
total_alumnos_esc = 0

for i in range(n_salones):
    n_alumnos = int(input(f"Ingrese la cantidad de alumnos en el salon {i+1}:"))
    suma_s = 0
    for u in range(n_alumnos):
        edad = int(input(f"Ingrese la edad del alumno {u+1}"))
        suma_s = suma_s + edad
    promedio_s = suma_s / n_alumnos
    print(f"El promedio del salon {i+1} es:{promedio_s:.2f}")
    suma_total_esc = suma_total_esc + suma_s
    total_alumnos_esc = total_alumnos_esc + n_alumnos

print(f"Promedio total de la escuela:{suma_total_esc / total_alumnos_esc:.2f}")

