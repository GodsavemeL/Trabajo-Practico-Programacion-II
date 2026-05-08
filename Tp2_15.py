print("1:Lunes. 7:Domingo.")
num_dia = int(input("Ingrese el numero del dia que quieres saber:"))

if num_dia > 7:
    print("Error: Ingrese un numero del 1 al 7.")
elif num_dia == 7:
    dia = "Domingo"
elif num_dia == 6:
    dia = "Sabado"
elif num_dia == 5:
    dia = "Viernes"
elif num_dia == 4:
    dia = "Jueves"
elif num_dia == 3:
    dia = "Miercoles"
elif num_dia == 2:
    dia = "Martes"
else:
    dia = "Lunes"

print(f"El dia que ingresaste es {dia}.")