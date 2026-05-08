horas = int(input("Ingrese la cantidad de horas trabajadas:"))
dinero_hrs = int(input("Ingrese el pago por hora:"))

if horas > 50:
    print("No puedes trabajar mas de 50 horas.")
elif horas <= 40:
    sueldo = horas * dinero_hrs
elif horas <= 45:
    sueldo = ((40 * dinero_hrs)+((horas - 40) * dinero_hrs * 2))
else:
    sueldo = ((40 * dinero_hrs) + (5 * dinero_hrs * 2) + ((horas - 45) * dinero_hrs * 3))

if horas <= 50:
    print(f"Tu sueldo semanal es de:${sueldo}")

