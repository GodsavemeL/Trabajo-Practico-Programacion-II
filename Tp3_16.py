num = int(input("Ingrese la cantidad de numeros:"))

for numeros in range(num):
    numero = float(input(f"Ingrese el numero {numeros + 1}:"))

    cubo = numero * 3
    
    print(f"El cubo del numero {numero} es:{cubo}")
    