nom1 = input("Primer nombre:")
edad1 = int(input("Edad1:"))
nom2 = input("Segundo nombre:")
edad2 = int(input("Edad:"))
nom3 = input("Tercer nombre:")
edad3 = int(input("Edad:"))
if edad1 <= edad2 & edad1 <= edad3:
    menor = nom1
elif edad2 <= edad1 & edad2 <= edad3:
    menor = nom2
else:
    menor = nom3
print(f"El menor de edad es:{menor}")

