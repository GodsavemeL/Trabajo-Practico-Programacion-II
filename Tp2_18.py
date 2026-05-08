anios = int(input("Ingrese la cantidad de años trabajados:"))
sueldo = int(input("Ingrese su sueldo:"))

if anios > 4:
    bono = 1.25
else:
    bono = 1.20

if sueldo < 2000:
    bono_s = 1.25
else:
    bono_s = 1.20

sueldo = sueldo * ((bono + bono_s) - 1)
print(f"Tienes un bono total del {(bono + bono_s) - 1}%")
print(f"Tu sueldo total es de {sueldo}")
