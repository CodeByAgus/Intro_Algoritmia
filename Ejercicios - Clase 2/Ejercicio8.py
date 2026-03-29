"""
Ejercicio 8: Distribución de Billetes y Monedas en Cajeros

Se lee una cantidad de dinero que desea retirar el cliente e imprima a cuántos billetes 
equivale, considerando que existen billetes de $1000, $500, $200, $100, $50, $20 y 
monedas de $10, $5, $2 y $1. Se debe minimizar la cantidad de billetes entregados.

Pseudocódigo:
    1. Leer monto
    2. Para cada denominación del billete/moneda (orden descendente):
        a. Calcular cantidad = monto // denominación
        b. Calcular resto = monto % denominación
        c. Imprimir cantidad si es mayor a 0
        d. Actualizar monto = resto
"""

# Entradas
monto = int(input("Ingrese la cantidad de dinero a retirar: "))

# Denominaciones (en orden descendente para minimizar billetes)
denominaciones = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

# Proceso y Salida
print("\n--- Desglose de Retiro ---")
for d in denominaciones:
    cantidad = monto // d
    monto %= d
    if cantidad > 0:
        if d >= 20:
            print(f"Billetes de ${d}: {cantidad}")
        else:
            print(f"Monedas de ${d}: {cantidad}")
