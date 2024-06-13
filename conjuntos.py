#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Operaciones básicas sobre conjuntos en Python

# Importar la biblioteca necesaria
import numpy as np

# Crear conjuntos de ejemplo
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# 1. Unión de conjuntos
# La unión de dos conjuntos es un conjunto que contiene todos los elementos de ambos conjuntos.
union_ab = conjunto_a.union(conjunto_b)
print(f"Unión de A y B: {union_ab}")

# 2. Intersección de conjuntos
# La intersección de dos conjuntos es un conjunto que contiene solo los elementos que están en ambos conjuntos.
interseccion_ab = conjunto_a.intersection(conjunto_b)
print(f"Intersección de A y B: {interseccion_ab}")

# 3. Diferencia de conjuntos
# La diferencia de dos conjuntos es un conjunto que contiene los elementos que están en el primer conjunto pero no en el segundo.
diferencia_ab = conjunto_a.difference(conjunto_b)
print(f"Diferencia de A y B: {diferencia_ab}")

# 4. Diferencia simétrica de conjuntos
# La diferencia simétrica de dos conjuntos es un conjunto que contiene los elementos que están en uno u otro conjunto, pero no en ambos.
diferencia_simetrica_ab = conjunto_a.symmetric_difference(conjunto_b)
print(f"Diferencia simétrica de A y B: {diferencia_simetrica_ab}")

# Ejemplos específicos
print("\nEjemplos específicos:")

# Ejemplo para la unión
print(f"Unión de {conjunto_a} y {conjunto_b} es {conjunto_a | conjunto_b}")

# Ejemplo para la intersección
print(f"Intersección de {conjunto_a} y {conjunto_b} es {conjunto_a & conjunto_b}")

# Ejemplo para la diferencia
print(f"Diferencia de {conjunto_a} y {conjunto_b} es {conjunto_a - conjunto_b}")

# Ejemplo para la diferencia simétrica
print(f"Diferencia simétrica de {conjunto_a} y {conjunto_b} es {conjunto_a ^ conjunto_b}")


# In[ ]:




