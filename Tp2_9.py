tipo_p = input("Tipo de poliza A/B:").upper()
if tipo_p == "A" or tipo_p == "B":
    bebe = input("Toma alcohol? S/N:").upper()
    if bebe == "S" or bebe == "N":
        lentes = input("Usa lentes? S/N:").upper()
        if lentes == "S" or lentes == "N":
            enfermedad = input("Padece alguna enfermedad? S/N:")
            if enfermedad == "S" or enfermedad == "N":
                edad = int(input("Introduce su edad:"))
                if tipo_p == "A":
                    costo = 1200
                else:
                    costo = 950
                cargos = 0
                if bebe == "S":
                    cargos = costo * 0.10
                if lentes == "S":
                    cargos = costo * 0.05
                if enfermedad == "S":
                    cargos = costo * 0.05
                if edad > 40:
                    cargos = costo * 0.20
                else:
                    cargos = costo * 0.10
                print(f"El costo total de la poliza es:${costo + cargos}")
            else:
                print("Error: Solo Ingresar S o N")
        else:
            print("Error: Solo Ingresar S o N")
    else:
        print("Error: Solo Ingresar S o N")
else:
    print("Error: Tipo de poliza Invalido. Ingresar A o B")