dinero =int(input("Ingrese su sueldo total:"))
if dinero<=10:
    regalo = "Tarjeta"
elif dinero<=100:
    regalo = "Chocolates"
elif dinero<=250:
    regalo = "Flores"
else:
    regalo = "Anillo"

print(f"Puedes regalarle:{regalo}")
