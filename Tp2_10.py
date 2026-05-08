presupuesto = int(input("Ingrese su presupuesto:"))
valor_bus = int(input("Ingrese el valor por km:"))
if presupuesto >= (1800 * 2) * valor_bus:
    viaje = "Cancún"
elif presupuesto >= (1200 * 2) * valor_bus:
    viaje = "Acapulco"
elif presupuesto >= (800 * 2) * valor_bus:
    viaje = "P.V"
elif presupuesto >= (750 * 2) * valor_bus:
    viaje = "Mexico"
else:
    print("Quedate en casa.")
print(f"Tu destino es hacia:{viaje}")
