sexo = input("Ingrese el sexo Hombre/Mujer:").capitalize()
if sexo == "Hombre" or sexo == "Mujer":
    edad = int(input("Ingrese la edad:"))
    if edad < 16:
        vacuna = "A"
    elif edad > 70:
        vacuna = "C"
    elif sexo == "Hombre":
        vacuna = "A"
    else:
        vacuna = "B"
    print(f"La/El {sexo} se debe aplicar la vacuna tipo {vacuna}.")
else:
    print("Error: Coloque Hombre o Mujer.")
