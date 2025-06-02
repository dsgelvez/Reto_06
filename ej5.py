n = int(input("Ingrese un número entre 2 y 50: "))

if n < 2 or n > 50:
    print("El número debe estar entre 2 y 50.")
else:
    print(f"Divisores de {n}:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

