n = int(input("Ingrese la cantidad de elementos: "))
vector_a = [0] * n
vector_b = [0] * n

for i in range(n):
    vector_a[i] = input(f"Ingrese elemento {i}: ")

vector_b[0] = vector_a[n-1]

for i in range(0, n-1):
    vector_b[i+1] = vector_a[i]

# 3. Resultado
print(f"Vector original:{vector_a}")
print(f"Vector resultante:{vector_b}")
