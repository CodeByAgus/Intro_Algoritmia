"""
Ejercicio 10: Convertir binario a decimal
Convertir un número binario de 4 cifras en un número decimal. 
Se ingresa como un solo número entero de cuatro dígitos.

Ayuda: 1 0 1 1 (binario) = 1 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3 = 11

Pseudocódigo:
    1. Leer binario_int
    2. Calcular d0 = binario_int % 10 (posicion 0)
    3. Calcular d1 = (binario_int // 10) % 10 (posicion 1)
    4. Calcular d2 = (binario_int // 100) % 10 (posicion 2)
    5. Calcular d3 = (binario_int // 1000) % 10 (posicion 3)
    6. Calcular decimal = (d0 * 2**0) + (d1 * 2**1) + (d2 * 2**2) + (d3 * 2**3)
    7. Imprimir decimal
"""

# Entradas
# Se lee como entero segun el enunciado.
binario_str = input("Ingrese un numero binario de 4 cifras (ej: 1011): ")
# Si lo tratamos como entero:
binario_int = int(binario_str)

# Proceso
d0 = binario_int % 10
d1 = (binario_int // 10) % 10
d2 = (binario_int // 100) % 10
d3 = (binario_int // 1000) % 10

decimal = (d0 * (2**0)) + (d1 * (2**1)) + (d2 * (2**2)) + (d3 * (2**3))

# Salida
print(f"Número Binario: {binario_str}")
print(f"Número Decimal equivalente: {decimal}")
