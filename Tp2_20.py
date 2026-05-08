pant_n = int(input("Ingrese la cantidad de pantalones a producir:"))
modelo = input("Ingrese el modelo del pantalon A/B:").upper()
if modelo == "A" or modelo == "B":
    talla = int(input("Ingrese la talla (30, 32, 36):"))
    if talla == 30 or talla == 32 or talla == 36:
        costo_m = float(input("Ingrese el costo por metro de tela:"))
        if  modelo == "A":
            metro = 1.50
            porcentaje = 0.80
        elif modelo == "B":
            metro = 1.80
            porcentaje = 0.95
        else:
            print("Modelo invalido.")
        costo_t = metro * costo_m
        mano_o = costo_t * porcentaje
        sub_t = costo_t + mano_o
        if talla == 32 or talla == 36:
            cargo_t = sub_t * 0.04
            sub_t = sub_t + cargo_t
        else:
            cargo_t = 0
        ganancia_u = sub_t * 0.30
        precio_v = sub_t + ganancia_u
        ganancia_t = ganancia_u * pant_n
        
        print(f"Modelo seleccionado:{modelo}")
        print(f"Talla seleccionada:{talla}")
        print(f"Precio de venta por pantalon:{precio_v}")
        print(f"Ganancia total:{ganancia_t}")
        
    else:
        print("Error: Solo hay tres tallas(30, 32 y 36)")
else:
    print("Error: Solo hay dos modelos de pantalones. A/B")      
