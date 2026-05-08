n_trabajador = int(input("Ingrese la cantidad de trabajadores:"))

for informacion in range(n_trabajador):
    nombre = input("Ingrese el nombre del trabajador:")
    sueldo_h = float(input("Ingrese el sueldo por hora:"))
    horas_t = int(input("Ingrese las horas trabajadas:"))

    sueldo_total = sueldo_h * horas_t

    if sueldo_total <= 150:
        desc = sueldo_total * 0.05
    elif sueldo_total <= 300:
        desc = sueldo_total * 0.07
    elif sueldo_total <= 450:
        desc = sueldo_total * 0.09
    else:
        desc = 0
        print("No se le descuenta.")

    dinero_total = sueldo_total - desc

    print(f"Nombre del Trabajador:{nombre}")
    print(f"Sueldo Semanal:{sueldo_total}")
    print(f"Descuento:{desc}")
    print(f"Sueldo Total:{dinero_total}")

