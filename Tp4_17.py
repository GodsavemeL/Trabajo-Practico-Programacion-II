n_choferes = 5
dias = 6
nombres = [""] * n_choferes
sueldo_hora = [0.0] * n_choferes
horas = [[0] * dias for _ in range(n_choferes)]

total_horas_semana = [0] * n_choferes
sueldo_semanal = [0.0] * n_choferes
total_empresa = 0.0

max_lunes = -1
chofer_mas_lunes = ""

for f in range(n_choferes):
    nombres[f] = input("Nombre: ")
    sueldo_hora[f] = float(input("Pago por hora: "))
    
    for d in range(dias):
        h = int(input(f"Horas día {d+1}: "))
        horas[f][d] = h
        total_horas_semana[f] += h
        if d == 0 and h > max_lunes:
            max_lunes = h
            chofer_mas_lunes = nombres[f]
    sueldo_semanal[f] = total_horas_semana[f] * sueldo_hora[f]
    total_empresa += sueldo_semanal[f]
for i in range(n_choferes):
    print(f"Chofer: {nombres[i]:10}  Horas: {total_horas_semana[i]:3}  Sueldo: ${sueldo_semanal[i]:8.2f}")

print(f"Total pagado por la empresa: ${total_empresa:.2f}")
print(f"Chofer que más trabajó el lunes: {chofer_mas_lunes} ({max_lunes} hrs)")