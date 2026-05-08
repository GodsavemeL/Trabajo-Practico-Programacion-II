antiguedad =  int(input("Ingrese los años trabajados:"))

if antiguedad == 1:
    bono = 100
elif antiguedad == 2:
    bono = 200
elif antiguedad == 3:
    bono = 300
elif antiguedad == 4:
    bono = 400
elif antiguedad == 5:
    bono = 500
else:
    bono = 1000

print(f"Tu bono total es de:${bono}")
