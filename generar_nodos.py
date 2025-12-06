import numpy as np
import heapq
from math import sqrt

def calcular(punto_inicial, punto_final, obstaculos, radio_seguro):
    
    #Aplicamos el algoritmo de Dijkstra para generar los nodos
    
    # 1. Crear una malla de puntos discretos
    min_x = min(punto_inicial[0], punto_final[0]) - 2
    max_x = max(punto_inicial[0], punto_final[0]) + 2
    min_y = min(punto_inicial[1], punto_final[1]) - 2
    max_y = max(punto_inicial[1], punto_final[1]) + 2
    
    # Resolucion de la malla
    paso = 1.0
    x_vals = np.arange(min_x, max_x + paso, paso)
    y_vals = np.arange(min_y, max_y + paso, paso)
    
    # Generar todos los puntos de la malla
    malla = []
    for x in x_vals:
        for y in y_vals:
            malla.append((x, y))
    
    # Filtrar puntos seguros
    puntos_seguros = []
    for punto in malla:
        seguro = True
        for obstaculo in obstaculos:
            if np.linalg.norm(np.array(punto) - obstaculo) < radio_seguro:
                seguro = False
                break
        if seguro:
            puntos_seguros.append(punto)
    
    # Añadir puntos inicial y final si no estan
    puntos_seguros = list(set(puntos_seguros))
    if tuple(punto_inicial) not in puntos_seguros:
        puntos_seguros.append(tuple(punto_inicial))
    if tuple(punto_final) not in puntos_seguros:
        puntos_seguros.append(tuple(punto_final))
    
    # Mapear puntos a indices
    idx_a_punto = {i: p for i, p in enumerate(puntos_seguros)}
    punto_a_idx = {p: i for i, p in enumerate(puntos_seguros)}
    
    # Construir grafo (conexiones entre puntos cercanos)
    n = len(puntos_seguros)
    grafo = {i: [] for i in range(n)}
    
    for i in range(n):
        xi, yi = idx_a_punto[i]
        for j in range(i + 1, n):
            xj, yj = idx_a_punto[j]
            # Conectar si estan en la vecindad
            if (xi - xj)**2 + (yi - yj)**2 <= 2.1 * paso**2:
                dist = np.linalg.norm([xi - xj, yi - yj])
                grafo[i].append((j, dist))
                grafo[j].append((i, dist))
    
    # Algoritmo de Dijkstra
    inicio = punto_a_idx[tuple(punto_inicial)]
    fin = punto_a_idx[tuple(punto_final)]
    
    dist = {i: float('inf') for i in range(n)}
    prev = {i: None for i in range(n)}
    dist[inicio] = 0
    
    # Cola de prioridad
    cola = [(0, inicio)]
    
    while cola:
        d, u = heapq.heappop(cola)
        if d > dist[u]:
            continue
        if u == fin:
            break
        
        for v, peso in grafo[u]:
            alt = d + peso
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(cola, (alt, v))
    
    # Reconstruir ruta
    ruta = []
    u = fin
    
    # Si no hay camino, usar ruta directa
    if prev[u] is None and u != inicio:
        return [punto_inicial, punto_final]
    
    while u is not None:
        ruta.append(idx_a_punto[u])
        u = prev[u]
    
    ruta.reverse()
    
    # Convertir a arrays numpy
    ruta = [np.array(p) for p in ruta]
    
    # Simplificar ruta para Bezier (tomar puntos clave)
    if len(ruta) > 5:
        # Tomar inicio, fin y puntos intermedios espaciados
        nodos = [ruta[0]]
        paso_simplificar = max(1, len(ruta) // 4)
        for i in range(paso_simplificar, len(ruta) - 1, paso_simplificar):
            nodos.append(ruta[i])
        nodos.append(ruta[-1])
        return nodos
    else:
        return ruta
