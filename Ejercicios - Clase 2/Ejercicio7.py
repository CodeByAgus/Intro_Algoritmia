"""
Ejercicio 7: Salario de un Vendedor de una Inmobiliaria
Salario = salario base + comision fija por cada venta + 5% del valor de las ventas.

Entradas:
    - ID del vendedor.
    - Cantidad de ventas realizadas.
    - Valor total de las ventas.

Constantes asumidas (ya que no se especifican en el enunciado):
    - Salario base: ¿100000? 
    - Comision fija por cada venta: ¿5000?

Sin embargo, para mayor flexibilidad, pediremos el salario base y la comision fija tambien.

Pseudocódigo:
    1. Leer id_vendedor
    2. Leer cant_ventas
    3. Leer valor_total
    4. Leer salario_base (o usar una constante)
    5. Leer comision_fija (o usar una constante)
    6. Calcular comision_total = (cant_ventas * comision_fija) + (valor_total * 0.05)
    7. Calcular salario_total = salario_base + comision_total
    8. Imprimir id_vendedor, salario_total
"""

# Entradas
vendedor_id = input("Ingrese el Numero del Vendedor: ")
cant_ventas = int(input("Ingrese la cantidad de ventas por el vendedor: "))
valor_total_ventas = float(input("Ingrese el valor total de las ventas: "))
salario_base = float(input("Ingrese el salario base: "))
comision_fija_por_venta = float(input("Ingrese la comision fija por cada venta: "))

# Proceso
comision_ventas = (cant_ventas * comision_fija_por_venta) + (valor_total_ventas * 0.05)
salario_total = salario_base + comision_ventas

# Salida
print("\n--- Resultado Mensual ---")
print(f"Salario total para el vendedor {vendedor_id}: ${salario_total:.2f}")
print(f"Desglose:")
print(f"  Salario base: ${salario_base:.2f}")
print(f"  Comision por ventas: ${comision_ventas:.2f}")
