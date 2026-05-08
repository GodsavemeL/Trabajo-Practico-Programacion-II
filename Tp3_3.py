n_num = int(input("Ingrese cuantos numeros quiere registrar:"))
ceros = 0
menor = 0
mayor = 0
for i in range(n_num):
    num = float(input(f"Ingrese el numero {i+1}:"))
    if num == 0:
        ceros = ceros + 1
    elif num < 0:
        menor = menor + 1
    else:
        mayor = mayor + 1

print("Tienes una cantidad de:")
print(f"Ceros:{ceros}")
print(f"Menores:{menor}")
print(f"Mayores:{mayor}")
