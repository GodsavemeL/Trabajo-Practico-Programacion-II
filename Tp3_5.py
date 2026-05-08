ahorro = 3
total_a = 0

for dia in range(1, 366):
    total_a = total_a + (ahorro / 100)
    ahorro = ahorro * 3

print(f"El ahorro total del año es:${total_a}")