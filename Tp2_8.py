antiguedad = int(input("Ingrese la cantidad de años que estuvo en la empresa:"))
sueldo = int(input("Ingrese su sueldo:"))

if 2 < antiguedad < 5:
    bono = 1.20
elif antiguedad > 4:
    bono = 1.30
else:
    bono = 1
if sueldo < 1000:
    bono_s = 1.25
elif 1000 < sueldo < 3500:
    bono_s = 1.10
else:
    bono_s = 1
if bono > bono_s:
    bono_f = bono
    tipo = "por la antiguedad"
else:
    bono_f = bono_s
    tipo = "por el sueldo"

sueldo = sueldo * bono_f 
print(f"Tu sueldo total es de:${sueldo} y es {tipo}")
