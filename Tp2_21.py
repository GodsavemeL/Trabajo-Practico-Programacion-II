saldo_a = float(input("Ingrese su saldo anterior:"))
monto_c = float(input("Ingrese su monto de las compras realizadas:"))
pago_a = float(input("Ingrese su pago realizado en el corte anterior:"))
pago_min_requerido_a = saldo_a * 0.15
if pago_a < pago_min_requerido_a:
    intereses = saldo_a * 0.12
    multa = 200
else:
    intereses = 0
    multa = 0

deuda_rem = saldo_a - pago_a

saldo_actual = deuda_rem + monto_c + intereses + multa

pago_min = saldo_a * 0.15
pago_sin_int = saldo_a * 0.85

print(f"Saldo Actual:${saldo_a}")
print(f"Pago Minimo:${pago_min}")
print(f"Pago para no generar intereses:${pago_sin_int}")
