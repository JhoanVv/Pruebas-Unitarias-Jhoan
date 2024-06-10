# Informe de Cobertura de Pruebas

Este proyecto implementa las cuatro operaciones matemáticas básicas (suma, resta, multiplicación y división) y contiene pruebas unitarias para verificar su correcto funcionamiento utilizando la herramienta `pytest`.

## Operaciones Implementadas

- Suma: `suma(a, b)`
- Resta: `resta(a, b)`
- Multiplicación: `multiplicacion(a, b)`
- División: `division(a, b)`

## Pruebas Unitarias

Las pruebas unitarias están implementadas en el archivo `test_operaciones.py` y se ejecutan utilizando `pytest`. Cada operación tiene dos pruebas unitarias que incluyen valores positivos y negativos, además de una prueba para manejar excepciones en el caso de la división por cero.

## Generación del Informe de Cobertura

Para generar el informe de cobertura de pruebas:

1. Ejecutar las pruebas con cobertura:

    ```bash
    coverage run -m pytest
    ```

2. Generar el reporte de cobertura en la terminal:

    ```bash
    coverage report
    ```

3. Generar un reporte de cobertura en formato HTML:

    ```bash
    coverage html
    ```

4. Abrir el archivo `index.html` dentro del directorio `htmlcov` en un navegador para ver el informe detallado de cobertura.

## Resultados de Cobertura

El informe de cobertura muestra que todas las funciones han sido cubiertas al 100% por las pruebas unitarias. Esto significa que cada línea de código en las funciones `suma`, `resta`, `multiplicacion`, y `division` ha sido ejecutada durante las pruebas.

A continuación se muestra un resumen del informe de cobertura:

```plaintext
Name              Stmts   Miss  Cover
-------------------------------------
operations.py        10      0   100%
test_operations.py   16      0   100%
-------------------------------------
TOTAL                26      0   100%
