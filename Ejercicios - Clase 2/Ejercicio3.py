"""
Ejercicio 3: Calcular el promedio de las notas que obtiene un alumno al rendir los dos parciales.

Pseudocódigo:
    1. Leer nota1
    2. Leer nota2
    3. Calcular promedio = (nota1 + nota2) / 2
    4. Imprimir promedio
"""

# Entradas
nota1 = float(input("Ingrese la nota del primer parcial: "))
nota2 = float(input("Ingrese la nota del segundo parcial: "))

# Proceso
promedio = (nota1 + nota2) / 2

# Salida
print(f"El promedio final del alumno es: {promedio}")
