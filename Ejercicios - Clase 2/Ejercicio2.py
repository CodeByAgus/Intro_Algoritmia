"""
Ejercicio 2: Operaciones Aritmeticas y Precedencia
Indicar el orden que ejecuta el intérprete Python cada una de ellas y calcular el valor.
"""

# a. 12 * 4 + 4 * 5
# Orden: multiplicaciones, luego suma.
res_a = 12 * 4 + 4 * 5
print(f"a. 12 * 4 + 4 * 5 = {res_a} (orden: multiplicaciones, suma)")

# b. 12 * (4 + 4) * 5
# Orden: paréntesis (suma), luego multiplicaciones.
res_b = 12 * (4 + 4) * 5
print(f"b. 12 * (4 + 4) * 5 = {res_b} (orden: parentesis, multiplicaciones)")

# c. 5 * 4 / 2
# Orden: multiplicación, división (de izquierda a derecha).
res_c = 5 * 4 / 2
print(f"c. 5 * 4 / 2 = {res_c} (orden: multiplicacion, division)")

# d. 5 * (4 / 2)
# Orden: paréntesis (división), luego multiplicación.
res_d = 5 * (4 / 2)
print(f"d. 5 * (4 / 2) = {res_d} (orden: parentesis, multiplicacion)")

# e. 24 / 2 ** 2
# Orden: potencia, luego división.
res_e = 24 / 2 ** 2
print(f"e. 24 / 2 ** 2 = {res_e} (orden: potencia, division)")

# f. (24 / 2) ** 2
# Orden: paréntesis (división), luego potencia.
res_f = (24 / 2) ** 2
print(f"f. (24 / 2) ** 2 = {res_f} (orden: parentesis, potencia)")

# g. - 9 ** 2
# Orden: potencia, luego negación. (En Python, ** tiene mayor precedencia que el operador unario -)
res_g = - 9 ** 2
print(f"g. - 9 ** 2 = {res_g} (orden: potencia, negacion)")

# h. (- 9) ** 2
# Orden: paréntesis (negación), luego potencia.
res_h = (- 9) ** 2
print(f"h. (- 9) ** 2 = {res_h} (orden: parentesis, potencia)")

# i. 10 / 3
# Orden: división.
res_i = 10 / 3
print(f"i. 10 / 3 = {res_i} (orden: division)")

# j. 10 // 3
# Orden: división entera.
res_j = 10 // 3
print(f"j. 10 // 3 = {res_j} (orden: division entera)")

# k. 12 % 5
# Orden: residuo/módulo.
res_k = 12 % 5
print(f"k. 12 % 5 = {res_k} (orden: residuo/modulo)")
