horas_t = float(input("Ingrese sus horas trabajadas:"))
horas_v = float(input("Ingrese su sueldo por hora:"))
if horas_t<=40:
    sueldo = horas_t * horas_v
    print(f"Tu sueldo es de:${sueldo}")
else:
    horas_extra = horas_t - 40
    sueldo = (40 * horas_v) + (horas_extra * horas_v * 2)
    print(f"Tu sueldo es de:${sueldo}")

