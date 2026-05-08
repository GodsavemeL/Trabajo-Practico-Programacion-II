x = float(input("Ingrese el valor de X:"))
a = float(input("Ingrese el valor de A:"))
b = float(input("Ingrese el valor de B:"))
potencia = 1

for i in range(a):
    potencia = potencia * x
f = potencia + b
print(f"El resultado de f = x**a + b es:{f}")