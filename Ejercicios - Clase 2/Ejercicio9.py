"""
Ejercicio 9: Conversión de segundos
Leer un período en segundos e imprimir expresado en días, horas, minutos y segundos.

Pseudocódigo:
    1. Leer segundos_totales
    2. Segs_por_dia = 24 * 60 * 60 (86400)
    3. Segs_por_hora = 60 * 60 (3600)
    4. Segs_por_min = 60
    5. Calcular dias = segundos_totales // 86400
    6. Calcular resto = segundos_totales % 86400
    7. Calcular horas = resto // 3600
    8. Calcular resto = resto % 3600
    9. Calcular minutos = resto // 60
    10. Calcular segundos = resto % 60
    11. Escribir dias, horas, minutos, segundos
"""

# Entradas
segundos_totales = int(input("Ingrese el periodo en segundos: "))

# Proceso
dias = segundos_totales // 86400
resto_dias = segundos_totales % 86400

horas = resto_dias // 3600
resto_horas = resto_dias % 3600

minutos = resto_horas // 60
segundos = resto_horas % 60

# Salida
print(f"\n{segundos_totales} segundos equivalen a:")
print(f"{dias} dias, {horas} horas, {minutos} minutos y {segundos} segundos.")
