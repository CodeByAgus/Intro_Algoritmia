"""
Ejercicio 6: Conversiones de longitud
Leer una medida en metros e imprimir esta medida expresada en centímetros, pulgadas, pies y yardas.

Conversiones:
    1 metro = 100 cm
    1 pulgada = 2.54 cm
    1 pie = 12 pulgadas
    1 yarda = 3 pies

Pseudocódigo:
    1. Leer m (metros)
    2. Calcular cm = m * 100
    3. Calcular pulgadas = cm / 2.54
    4. Calcular pies = pulgadas / 12
    5. Calcular yardas = pies / 3
    6. Escribir cm, pulgadas, pies, yardas
"""

# Entradas
metros = float(input("Ingrese la medida en metros: "))

# Proceso
cm = metros * 100
pulgadas = cm / 2.54
pies = pulgadas / 12
yardas = pies / 3

# Salidas
print(f"Medida ingresada: {metros}m")
print(f"En centímetros: {cm:.2f} cm")
print(f"En pulgadas: {pulgadas:.2f} in")
print(f"En pies: {pies:.2f} ft")
print(f"En yardas: {yardas:.2f} yd")
