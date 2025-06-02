n = int(input("Ingrese un número natural (n ≥ 2): "))

if n < 2:
    print("El número debe ser mayor o igual a 2.")
else:
    if n % 2 != 0:
        n -= 1

    print(f"Números pares descendentes desde {n} hasta 2:")
    for numero in range(n, 1, -2):
        print(numero, end=" ")
    
