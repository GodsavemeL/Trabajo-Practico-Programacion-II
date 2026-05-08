
grados = float(input("Ingrese el angulo en grados: "))
radianes = grados * (3.141592653589793 / 180)
seno = 0
n_terminos = 10  

for n in range(n_terminos):
    signo = (-1)**n
    exponente = 2 * n + 1
    factorial = 1
    for j in range(1, exponente + 1):
        factorial = factorial * j
    seno += signo * (radianes**exponente / factorial)

print(f"El seno aproximado de {grados}° es: {seno:.5f}")