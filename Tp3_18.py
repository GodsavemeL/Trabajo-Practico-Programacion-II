capital = 1500
interes = 0.15
anio_vendido = 1961
anio_actual = 2026

tiempo = anio_actual - anio_vendido
valor_acu = capital

for i in range(tiempo):
    valor_acu = valor_acu + (valor_acu * interes)

print(f"El valor de la inversion actualmente despues de {tiempo} años es de:${valor_acu:.2f}")
