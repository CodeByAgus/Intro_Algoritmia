"""
Ejercicio 5: Interés Bancario
Una persona quiere invertir su capital en un banco y quiere saber cuánto dinero gana en un mes 
si el banco paga 2% mensual. ¿Cuánto ganará en seis meses si deja su dinero invertido?

Pseudocódigo:
    1. Leer capital
    2. Calcular ganar_un_mes = capital * 0.02
    3. Calcular ganar_seis_meses = ganar_un_mes * 6
    4. Escribir ganar_un_mes, ganar_seis_meses
"""

# Entradas
capital = float(input("Ingrese el capital a invertir: "))

# Proceso (Interes simple)
ganar_un_mes = capital * 0.02
# Suponiendo que el interes se acumula mensualmente sobre el capital original.
ganar_seis_meses = ganar_un_mes * 6

# Salidas
print(f"En un mes ganara: ${ganar_un_mes:.2f}")
print(f"En seis meses ganara: ${ganar_seis_meses:.2f}")
print(f"Total al final de seis meses: ${capital + ganar_seis_meses:.2f}")
