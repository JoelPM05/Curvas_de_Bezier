import numpy as np
import heapq
from math import sqrt

def calcular(punto_inicial, punto_final, obstaculos, radio_seguro):
    """
    Versión simplificada y corregida
    """
    # Ampliar el radio para planificación
    radio_planificacion = radio_seguro * 1.5
    
    # 1. Crear malla
    min_x = min(punto_inicial[0], punto_final[0]) - 2
    max_x = max(punto_inicial[0], punto_final[0]) + 2
    min_y = min(punto_inicial[1], punto_final[1]) - 2
    max_y = max(punto_inicial[1], punto_final[1]) + 2
    
    paso = 1.0
    x_vals = np.arange(min_x, max_x + paso, paso)
    y_vals = np.arange(min_y, max_y + paso, paso)
    
    # Generar puntos de malla
    malla = []
    for x in x_vals:
        for y in y_vals:
            malla.append((x, y))
    
    # 2. Filtrar puntos seguros
    puntos_seguros = []
    for punto in malla:
        seguro = True
        for obstaculo in obstaculos:
            if np.linalg.norm(np.array(punto) - obstaculo) < radio_planificacion:
                seguro = False
                break
        if seguro:
            puntos_seguros.append(punto)
    
    # Añadir puntos inicial y final
    if tuple(punto_inicial) not in puntos_seguros:
        puntos_seguros.append(tuple(punto_inicial))
    if tuple(punto_final) not in puntos_seguros:
        puntos_seguros.append(tuple(punto_final))
    
    # 3. Mapear índices
    idx_a_punto = {i: p for i, p in enumerate(puntos_seguros)}
    punto_a_idx = {p: i for i, p in enumerate(puntos_seguros)}
    
    # 4. Construir grafo simple
    n = len(puntos_seguros)
    grafo = {i: [] for i in range(n)}
    
    for i in range(n):
        xi, yi = idx_a_punto[i]
        for j in range(i + 1, n):
            xj, yj = idx_a_punto[j]
            distancia_cuad = (xi - xj)**2 + (yi - yj)**2
            if distancia_cuad <= 2.1 * paso**2:  # Vecinos cercanos
                dist = sqrt(distancia_cuad)
                grafo[i].append((j, dist))
                grafo[j].append((i, dist))
    
    # 5. Dijkstra
    inicio = punto_a_idx[tuple(punto_inicial)]
    fin = punto_a_idx[tuple(punto_final)]
    
    dist = {i: float('inf') for i in range(n)}
    prev = {i: None for i in range(n)}
    dist[inicio] = 0
    
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
    
    # 6. Reconstruir ruta
    ruta = []
    u = fin
    
    if prev[u] is None and u != inicio:
        # Ruta directa si no hay camino
        return [np.array(punto_inicial), np.array(punto_final)]
    
    while u is not None:
        ruta.append(idx_a_punto[u])
        u = prev[u]
    
    ruta.reverse()
    
    # Convertir a arrays numpy
    ruta_np = [np.array(p, dtype=float) for p in ruta]
    
    return ruta_np
