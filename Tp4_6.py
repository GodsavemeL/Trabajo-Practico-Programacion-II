nombres = [None] * 10
edades = [0] * 10

for i in range(10):
    print(f"Datos del alumno {i + 1}")
    nombres[i] = input("Nombre: ")
    edades[i] = int(input("Edad: "))

mayor_edad = edades[0]
posicion_mayor = 0

for i in range(1, 10):
    if edades[i] > mayor_edad:
        mayor_edad = edades[i]
        posicion_mayor = i

print(f"El alumno con mayor edad es: {nombres[posicion_mayor]}")
print(f"Tiene: {mayor_edad} años.")