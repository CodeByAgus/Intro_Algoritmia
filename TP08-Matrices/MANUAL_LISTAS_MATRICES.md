# Manual: Listas y Matrices

## Conceptos Fundamentales

### Listas
```python
lista = []
lista = [1, 2, 3, 4, 5]
lista.append(valor)
lista[indice] = nuevo_valor
len(lista)
lista.pop()
lista.insert(indice, valor)
lista.remove(valor)
lista.sort()
```

### Matrices (Listas de Listas)
```python
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz[fila][columna]
len(matriz)
len(matriz[0])
```

### Iteración
```python
for elemento in lista:
    print(elemento)

for i in range(len(lista)):
    print(lista[i])

for i, elemento in enumerate(lista):
    print(i, elemento)

for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j])
```

---

## Ejercicio 1: Matriz Aleatoria 3x4

**Objetivo:** Crear matriz 3x4 con valores aleatorios entre 1 y 10, mostrarla formateada.

```python
import random

rows, cols = 3, 4
matriz = []

for i in range(rows):
    fila = []
    for j in range(cols):
        fila.append(random.randint(1, 10))
    matriz.append(fila)

for fila in matriz:
    print("  ".join(f"{val:2d}" for val in fila))
```

---

## Ejercicio 2: Suma Triángulo Superior

**Objetivo:** Matriz cuadrada (NxN), sumar elementos del triángulo superior (diagonal incluida).

**Concepto:** En triángulo superior, para cada fila i, se suman desde columna j=i hasta el final.

```python
import random

def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(random.randint(1, 10))
        matriz.append(fila)
    return matriz

def suma_triangulo_superior(matriz):
    total = 0
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            total += matriz[i][j]
    return total

n = int(input("Tamaño matriz: "))
matriz = crear_matriz(n)

print("Matriz:")
for fila in matriz:
    print("  ".join(f"{val:2d}" for val in fila))

print(f"Suma triángulo superior: {suma_triangulo_superior(matriz)}")
```

---

## Ejercicio 3: Suma Diagonal Principal

**Objetivo:** Matriz NxM, sumar valores sobre diagonal principal.

**Concepto:** Diagonal principal: posiciones donde fila == columna (i == j).

```python
import random

def crear_matriz(filas, columnas, a, b):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(a, b))
        matriz.append(fila)
    return matriz

def suma_diagonal(matriz):
    total = 0
    for i in range(len(matriz)):
        if i < len(matriz[0]):
            total += matriz[i][i]
    return total

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))
a = int(input("Valor mínimo: "))
b = int(input("Valor máximo: "))

matriz = crear_matriz(filas, columnas, a, b)

print("Matriz:")
for fila in matriz:
    print("  ".join(f"{val:3d}" for val in fila))

print(f"Suma diagonal: {suma_diagonal(matriz)}")
```

---

## Ejercicio 4: Coordenadas del Mayor Valor

**Objetivo:** Encontrar posición (fila, columna) del mayor valor en matriz NxM.

```python
import random

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(100, 1000))
        matriz.append(fila)
    return matriz

def encontrar_maximo(matriz):
    max_valor = matriz[0][0]
    max_fila, max_col = 0, 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > max_valor:
                max_valor = matriz[i][j]
                max_fila, max_col = i, j
    
    return max_valor, max_fila, max_col

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

matriz = crear_matriz(filas, columnas)

print("Matriz:")
for fila in matriz:
    print("  ".join(f"{val:4d}" for val in fila))

valor, fila, col = encontrar_maximo(matriz)
print(f"Mayor valor: {valor} en posición ({fila}, {col})")
```

---

## Ejercicio 5: Función Crear Matriz con Validación

**Objetivo:** Función NxM con parámetros (n, m, a, b). Validar rango y dimensiones.

```python
import random

def crear_matriz(n, m, a, b):
    if n <= 0 or m <= 0 or a >= b:
        return []
    
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(random.randint(a, b))
        matriz.append(fila)
    return matriz

def suma_filas_columnas(matriz):
    if not matriz:
        return [], []
    
    sumas_filas = []
    for fila in matriz:
        sumas_filas.append(sum(fila))
    
    sumas_columnas = []
    for j in range(len(matriz[0])):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        sumas_columnas.append(suma)
    
    return sumas_filas, sumas_columnas

n = int(input("Filas: "))
m = int(input("Columnas: "))
a = int(input("Mínimo: "))
b = int(input("Máximo: "))

matriz = crear_matriz(n, m, a, b)

if matriz:
    print("Matriz:")
    for fila in matriz:
        print("  ".join(f"{val:3d}" for val in fila))
    
    sumas_f, sumas_c = suma_filas_columnas(matriz)
    
    print(f"\nSumas filas: {sumas_f}")
    print(f"Sumas columnas: {sumas_c}")
else:
    print("Matriz vacía (parámetros inválidos)")
```

---

## Ejercicio 6: Suma de Dos Matrices 3x3

**Objetivo:** Crear dos matrices 3x3, sumarlas elemento a elemento.

```python
import random

def crear_matriz(n, m, a, b):
    if n <= 0 or m <= 0 or a >= b:
        return []
    matriz = []
    for i in range(n):
        fila = []
        for j in range(m):
            fila.append(random.randint(a, b))
        matriz.append(fila)
    return matriz

def validar_rango():
    while True:
        a = int(input("Valor mínimo: "))
        b = int(input("Valor máximo: "))
        if a < b:
            return a, b
        print("El mínimo debe ser menor que el máximo")

def sumar_matrices(m1, m2):
    resultado = []
    for i in range(len(m1)):
        fila = []
        for j in range(len(m1[0])):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)
    return resultado

a, b = validar_rango()
matriz1 = crear_matriz(3, 3, a, b)
matriz2 = crear_matriz(3, 3, a, b)

print("Matriz 1:")
for fila in matriz1:
    print("  ".join(f"{val:3d}" for val in fila))

print("\nMatriz 2:")
for fila in matriz2:
    print("  ".join(f"{val:3d}" for val in fila))

resultado = sumar_matrices(matriz1, matriz2)
print("\nMatriz Suma:")
for fila in resultado:
    print("  ".join(f"{val:3d}" for val in fila))

print(f"Suma total de elementos: {sum(sum(fila) for fila in resultado)}")
```

---

## Ejercicio 7: Matriz de 4 Columnas

**Objetivo:** Ingresar cantidad de números (múltiplo de 4), crear matriz con 4 elementos por fila.

```python
import random

def crear_matriz_4columnas(cantidad):
    if cantidad % 4 != 0:
        return []
    
    filas = cantidad // 4
    matriz = []
    
    for i in range(filas):
        fila = []
        for j in range(4):
            fila.append(random.randint(1, 100))
        matriz.append(fila)
    
    return matriz

while True:
    cantidad = int(input("Cantidad de números (múltiplo de 4): "))
    if cantidad % 4 == 0 and cantidad > 0:
        break
    print("Debe ser múltiplo de 4 y mayor a 0")

matriz = crear_matriz_4columnas(cantidad)

print("Matriz:")
for fila in matriz:
    print("  ".join(f"{val:3d}" for val in fila))

print(f"Filas creadas: {len(matriz)}")
```

---

## Ejercicio 8: Matriz con Patrón Específico

**Objetivo:** Generar matriz NxM con patrón de números consecutivos.

Patrón:
```
1   3   5   7
2   4   6   8
9  11  13  15
10 12  14  16
```

```python
def crear_matriz_patron(filas, columnas):
    matriz = []
    contador = 1
    
    for j in range(columnas):
        for i in range(filas):
            if not matriz[i] if i < len(matriz) else False:
                matriz.append([])
            if len(matriz[i]) <= j:
                matriz[i].append(contador)
            contador += 1
    
    return matriz
```

**Solución alternativa más clara:**

```python
def crear_matriz_patron(filas, columnas):
    matriz = [[0] * columnas for _ in range(filas)]
    contador = 1
    
    for j in range(columnas):
        for i in range(filas):
            matriz[i][j] = contador
            contador += 1
    
    return matriz

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

matriz = crear_matriz_patron(filas, columnas)

print("Matriz:")
for fila in matriz:
    print("  ".join(f"{val:3d}" for val in fila))
```

---

## Ejercicio 9: Suma de Filas sin Repetidos

**Objetivo:** Sumar cada fila, guardar en lista sin valores repetidos, mostrar ordenada.

```python
import random

def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(random.randint(1, 20))
        matriz.append(fila)
    return matriz

def sumas_filas_sin_repetidos(matriz):
    sumas = []
    for fila in matriz:
        suma = sum(fila)
        if suma not in sumas:
            sumas.append(suma)
    
    sumas.sort()
    return sumas

n = int(input("Tamaño matriz: "))
matriz = crear_matriz(n)

print("Matriz:")
for fila in matriz:
    print("  ".join(f"{val:3d}" for val in fila))

sumas = sumas_filas_sin_repetidos(matriz)
print(f"Sumas (sin repetidos, ordenadas): {sumas}")
```

---

## Ejercicio 10: Ordenar Filas por Selección

**Objetivo:** Ingresar matriz NxM, ordenar cada fila con método selección, mostrar resultado.

**Método de Selección:**

```python
def ordenar_seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

n = int(input("Filas: "))
m = int(input("Columnas: "))

matriz = []
print("Ingrese los valores:")
for i in range(n):
    fila = []
    for j in range(m):
        valor = int(input(f"Matriz[{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\nMatriz original:")
for fila in matriz:
    print("  ".join(f"{val:3d}" for val in fila))

for i in range(len(matriz)):
    matriz[i] = ordenar_seleccion(matriz[i])

print("\nMatriz ordenada:")
for fila in matriz:
    print("  ".join(f"{val:3d}" for val in fila))
```

---

## Conceptos Clave

### Triángulo Superior
- Fila i, columnas desde j=i hasta el final
- `for j in range(i, len(matriz))`

### Triángulo Inferior  
- Fila i, columnas desde j=0 hasta j=i
- `for j in range(0, i+1)`

### Diagonal Principal
- Elementos donde i == j
- `matriz[i][i]`

### Diagonal Secundaria
- Elementos donde i + j == n - 1 (matriz nxn)
- `matriz[i][n-1-i]`

### Validación de Rango
```python
if a >= b:
    return []
```

### Sin Duplicados
```python
if elemento not in lista:
    lista.append(elemento)
```

### Método Selección
```python
for i in range(len(lista)):
    minimo = i
    for j in range(i+1, len(lista)):
        if lista[j] < lista[minimo]:
            minimo = j
    lista[i], lista[minimo] = lista[minimo], lista[i]
```
