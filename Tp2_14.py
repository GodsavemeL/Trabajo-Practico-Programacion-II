calificacion = int(input("Ingrese la nota del estudiante:"))

if calificacion > 10:
    print("Error: La nota maxima es de 10.")
elif calificacion == 10:
    print("Tu calificacion:A")
elif calificacion == 9:
    print("Tu Calificacion:B")
elif calificacion == 8:
    print("Tu Calificacion:C")
elif calificacion == 7 or calificacion == 6:
    print("Tu Calificacion:D")
else:
    print("Tu Calificacion:F")
