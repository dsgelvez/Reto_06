# Reto 6 - Ejercicios de Python

## Contenido
- **Ejercicio 1**: Imprime los números del 1 al 100 junto con sus cuadrados.
- **Ejercicio 2**: Imprime los números impares del 1 al 999 y los pares del 2 al 1000.
- **Ejercicio 3**: Imprime números pares descendentes hasta 2, o muestra error si n < 2.
- **Ejercicio 4**: Calcula el factorial de un número "n" dado.
- **Ejercicio 5**: Muestra los divisores de un número de 2 a 50.
- **Ejercicio 6**: Lista los números primos del 1 al 100.

## Diagramas de flujo

```mermaid
%% Ejercicio 1
flowchart TD
    A[Inicio] --> B[i = 1]
    B --> C{i <= 100?}
    C -- Sí --> D[Imprimir i y i²]
    D --> E[i = i + 1]
    E --> C
    C -- No --> F[Fin]

%% Ejercicio 2
flowchart TD
    A2[Inicio] --> B2[Imprimir 'Números impares 1-999']
    B2 --> C2[i = 1]
    C2 --> D2{i <= 999?}
    D2 -- Sí --> E2[Imprimir i]
    E2 --> F2[i = i + 2]
    F2 --> D2
    D2 -- No --> G2[Imprimir 'Números pares 2-1000']
    G2 --> H2[j = 2]
    H2 --> I2{j <= 1000?}
    I2 -- Sí --> J2[Imprimir j]
    J2 --> K2[j = j + 2]
    K2 --> I2
    I2 -- No --> L2[Fin]

%% Ejercicio 3
flowchart TD
    A3[Inicio] --> B3[Leer n]
    B3 --> C3{n >= 2?}
    C3 -- No --> D3[Mostrar error] --> E3[Fin]
    C3 -- Sí --> F3{n es par?}
    F3 -- No --> G3[n = n - 1] --> H3
    F3 -- Sí --> H3[Imprimir n]
    H3 --> I3[n = n - 2]
    I3 --> J3{n >= 2?}
    J3 -- Sí --> H3
    J3 -- No --> E3[Fin]
