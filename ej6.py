def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Números primos del 1 al 100:")
for numero in range(1, 101):
    if es_primo(numero):
        print(numero, end=" ")
