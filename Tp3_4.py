n_foco = int(input("Ingrese la cantidad de focos en el lote:"))
verde, blanco, rojo = 0, 0, 0

for i in range(n_foco):
    color = input("Color del foco V/B/R:").upper()
    if color == "V":
        verde = verde + 1
    elif color == "B":
        blanco = blanco + 1
    elif color == "R":
        rojo = rojo + 1
    else:
        print("Error:Solo elige V/B/R.")

print(f"Tienes en tu lote de focos un total de:{verde} foco/s verdes, {blanco} foco/s blancos y {rojo} foco/s rojos")