total_dinero = 0
contador = 1

while contador <= 6:
    if contador == 1:
        valor = 50
        tipo = "billetes de $50"
    elif contador == 2:
        valor = 20
        tipo = "billetes de $20"
    elif contador == 3:
        valor = 10
        tipo = "billetes de $10"
    elif contador == 4:
        valor = 10
        tipo = "monedas de $10"
    elif contador == 5:
        valor = 5
        tipo = "monedas de $5"
    elif contador == 6:
        valor = 1
        tipo = "monedas de $1"
    
    cantidad = int(input(f"Ingrese la cantidad de {tipo}: "))
    total_dinero = total_dinero + (cantidad * valor)
    
    contador = contador + 1

print(f"El dinero total en el monedero es: ${total_dinero}")