"""
Ejercicio 1: Basico
a. Mostrar el mensaje “Hola Mundo”.
b. Ingresar el nombre del usuario y saludarlo.
c. Ingresar dos números y mostrar la suma y la diferencia.
d. Ingresar tres números y mostrar la suma y el promedio.
e. Ingresar el monto de una factura y calcular el IVA (21%).
"""

# a
print("--- a ---")
print("Hola Mundo")

# b
print("\n--- b ---")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

# c
print("\n--- c ---")
n1 = float(input("Ingrese primer numero: "))
n2 = float(input("Ingrese segundo numero: "))
print(f"Suma: {n1 + n2}")
print(f"Diferencia: {n1 - n2}")

# d
print("\n--- d ---")
num1 = float(input("Ingrese primer numero: "))
num2 = float(input("Ingrese segundo numero: "))
num3 = float(input("Ingrese tercer numero: "))
suma_d = num1 + num2 + num3
promedio_d = suma_d / 3
print(f"Suma: {suma_d}")
print(f"Promedio: {promedio_d}")

# e
print("\n--- e ---")
factura = float(input("Ingrese el monto de la factura: "))
iva = factura * 0.21
print(f"Monto: {factura}")
print(f"IVA (21%): {iva}")
print(f"Total con IVA: {factura + iva}")
