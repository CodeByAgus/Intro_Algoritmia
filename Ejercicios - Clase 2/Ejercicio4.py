"""
Ejercicio 4: Tres personas invierten dinero para fundar una empresa. 
Calcular qué porcentaje invirtió cada una.

Pseudocódigo:
    1. Leer inv1, inv2, inv3
    2. Calcular total = inv1 + inv2 + inv3
    3. Calcular porcent_1 = (inv1 / total) * 100
    4. Calcular porcent_2 = (inv2 / total) * 100
    5. Calcular porcent_3 = (inv3 / total) * 100
    6. Escribir porcent_1, porcent_2, porcent_3
"""

# Entradas
inv1 = float(input("Inversion de la primera persona: "))
inv2 = float(input("Inversion de la segunda persona: "))
inv3 = float(input("Inversion de la tercera persona: "))

# Proceso
total = inv1 + inv2 + inv3
# Si total es 0, no se puede calcular el porcentaje.
if total > 0:
    porcent_1 = (inv1 / total) * 100
    porcent_2 = (inv2 / total) * 100
    porcent_3 = (inv3 / total) * 100

    # Salidas
    print(f"La inversion total es: ${total:.2f}")
    print(f"Porcentaje de la persona 1: {porcent_1:.2f}%")
    print(f"Porcentaje de la persona 2: {porcent_2:.2f}%")
    print(f"Porcentaje de la persona 3: {porcent_3:.2f}%")
else:
    print("La inversión total debe ser mayor a 0.")
