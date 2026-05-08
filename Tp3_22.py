total_ganancia_banco = 0

clientes = int(input("Ingrese la cantidad de clientes: "))

for i in range(clientes):
    saldo_anterior = float(input("Saldo anterior: "))
    compras = float(input("Compras realizadas: "))
    pago_depositado = float(input("Pago depositado anteriormente: "))
    pago_min_requerido = saldo_anterior * 0.15
    if pago_depositado < pago_min_requerido:
        intereses_moratorios = saldo_anterior * 0.12
        multa = 200
        total_ganancia_banco += intereses_moratorios + multa
    else:
        intereses_moratorios = 0
        multa = 0
    
    saldo_actual = (saldo_anterior - pago_depositado) + compras + intereses_moratorios + multa
    
    pago_minimo = saldo_actual * 0.15
    pago_no_intereses = saldo_actual * 0.85
    
    print(f"Saldo Actual:${saldo_actual:.2f}")
    print(f"Pago Minimo:${pago_minimo:.2f}")
    print(f"Pago para no generar intereses:${pago_no_intereses:.2f}")

print(f"Monto total ganado por el banco (Intereses + Multas): ${total_ganancia_banco:.2f}")