# Reto 6 - Ejercicios de Python

## Contenido
- **Ejercicio 1**: Imprime los números del 1 al 100 junto con sus cuadrados.
- **Ejercicio 2**: Imprime los números impares del 1 al 999 y los pares del 2 al 1000.
- **Ejercicio 3**: Imprime números pares descendentes hasta 2, o muestra error si n < 2.
- **Ejercicio 4**: Calcula el factorial de un número "n" dado.
- **Ejercicio 5**: Muestra los divisores de un número de 2 a 50.
- **Ejercicio 6**: Lista los números primos del 1 al 100.

## Diagramas de flujo

## Diagrama 1: Números con sus cuadrados
```mermaid
flowchart TD
    A[Inicio] --> B[i = 1]
    B --> C{"i <= 100?"}
    C -->|Sí| D[Imprimir i y i²]
    D --> E[i = i + 1]
    E --> C
    C -->|No| F[Fin]
```
## Diagrama 2: Números impares y pares
```mermaid
flowchart TD
    A[Inicio] --> B["Imprimir 'Impares 1-999'"]
    B --> C[i = 1]
    C --> D{"i <= 999?"}
    D -->|Sí| E[Imprimir i]
    E --> F[i = i + 2]
    F --> D
    D -->|No| G["Imprimir 'Pares 2-1000'"]
    G --> H[j = 2]
    H --> I{"j <= 1000?"}
    I -->|Sí| J[Imprimir j]
    J --> K[j = j + 2]
    K --> I
    I -->|No| L[Fin]
```
## Diagrama 3: Números pares descendentes
```mermaid
flowchart TD
    A[Inicio] --> B["Leer n (n >= 2)"]
    B --> C{"n >= 2?"}
    C -->|No| D["Mostrar error"] --> E[Fin]
    C -->|Sí| F{"n es par?"}
    F -->|No| G[n = n - 1] --> H
    F -->|Sí| H[Imprimir n]
    H --> I[n = n - 2]
    I --> J{"n >= 2?"}
    J -->|Sí| H
    J -->|No| E[Fin]
```
