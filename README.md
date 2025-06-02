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
    A[Inicio] --> B[Inicializar n = 1]
    B --> C{"n <= 100?"}
    C -->|Sí| D[calcular cuadrado = n²]
    D --> E[Imprimir n y cuadrado]
    E --> F[n = n + 1]
    F --> C
    C -->|No| G[Fin]
```
## Diagrama 2: Números impares y pares
```mermaid
flowchart TD
    A[Inicio] --> B["Imprimir 'Números impares 1-999'"]
    B --> C[Inicializar n = 1]
    C --> D{"n < 1000?"}
    D -->|Sí| E[Imprimir n]
    E --> F[n = n + 2]
    F --> D
    D -->|No| G["Imprimir 'Números pares 2-1000'"]
    G --> H[Inicializar n = 2]
    H --> I{"n <= 1000?"}
    I -->|Sí| J[Imprimir n]
    J --> K[n = n + 2]
    K --> I
    I -->|No| L[Fin]
```
## Diagrama 3: Números pares descendentes
```mermaid
flowchart TD
    A[Inicio] --> B[Leer n]
    B --> C{"n >= 2?"}
    C -->|No| D["Imprimir 'Error: n debe ser ≥ 2'"]
    D --> E[Fin]
    C -->|Sí| F{"n es impar?"}
    F -->|Sí| G[n = n - 1]
    G --> H
    F -->|No| H["Imprimir 'Números pares descendentes desde n hasta 2'"]
    H --> I[Inicializar numero = n]
    I --> J{"numero >= 2?"}
    J -->|Sí| K[Imprimir numero]
    K --> L[numero = numero - 2]
    L --> J
    J -->|No| M[Fin]
```
