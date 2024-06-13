#!/usr/bin/env python
# coding: utf-8

# In[2]:


import networkx as nx
import itertools

def is_hamiltonian_path(grafo, path):
   
    n = len(graph.nodes)
   
    if len(path) != n:
        return False
    
    if len(set(path)) != n:
        return False
    
    for i in range(n - 1):
        if not graph.has_edge(path[i], path[i + 1]):
            return False
    return True

def find_hamiltonian_path(grafo):
    
    n = len(graph.nodes)
    vertices = list(graph.nodes)
    
    for perm in itertools.permutations(vertices):
        if is_hamiltonian_path(grafo, perm):
            return perm
    return None

def calculate_graph_properties(grafo):
    """calcula propiedades del grafo."""
    propiedades = {
        "grados": dict(graph.degree),
        "excentricidad": nx.eccentricity(graph),
        "centro": nx.center(graph),
        "diametro": nx.diameter(graph),
        "perimetro": nx.periphery(graph),
        "radio": nx.radius(graph),
    }
    return properties


if __name__ == "__menu__":
    # Ejemplo de grafo
    grafo = nx.Graph()
    edges = [
        (1, 2), (2, 3), (3, 4), (4, 5),
        (5, 1), (1, 3), (2, 4), (3, 5)
    ]
    graph.add_edges_from(edges)
    
    
    path = find_hamiltonian_path(grafo)
    if path:
        print("Camino Hamiltoniano Encontrado:", path)
    else:
        print("El camino hamiltoniano no existe.")
    
    # Se calcula
    properties = calculate_graph_properties(grafo)
    print("Propiedades del grafo:")
    for prop, value in properties.items():
        print(f"{prop}: {value}")


# In[ ]:





# In[ ]:




