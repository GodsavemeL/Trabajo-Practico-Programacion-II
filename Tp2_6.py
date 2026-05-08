articulo = int(input("Ingrese el valor del articulo:"))
if articulo >= 200:
    desc = 0.15
elif articulo >= 100:
    desc = 0.12
else:
    desc = 0.10
articulo = articulo - (articulo * desc)
print(f"El valor total del articulo es:${articulo}")
