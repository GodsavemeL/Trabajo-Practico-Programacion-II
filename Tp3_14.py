n_alumnos = int(input("Ingrese la cantidad de Alumnos:"))
cantidad_a = 0
cantidad_r = 0

for nota in range(n_alumnos):
    n_nota = float(input("Ingrese la nota del Alumno:"))
    if n_nota < 6:
        cantidad_r = cantidad_r + 1
    elif n_nota < 11:
        cantidad_a = cantidad_a + 1
    else:
        print("Error:No hay nota mas alta que 10.")

print(f"La cantidad de aprobados es un total de {cantidad_a} y la cantidad de desaprobados es un total de {cantidad_r}")
