import numpy as np
import matplotlib.pyplot as plt

def verificar_distancia_minima(curva, obstaculos, radio_seguro):
    if len(curva) == 0:
        return float('inf'), 0
    
    distancias_minimas = []
    puntos_problematicos = []
    
    for punto in curva:
        distancias = [np.linalg.norm(punto - obstaculo) for obstaculo in obstaculos]
        distancia_min = min(distancias)
        distancias_minimas.append(distancia_min)
        
        if distancia_min < radio_seguro:
            puntos_problematicos.append((punto, distancia_min))
    
    if puntos_problematicos:
        print(f"\nHay {len(puntos_problematicos)} puntos muy cerca de obstáculos:")
        for punto, distancia in puntos_problematicos[:5]:
            print(f"  Punto {punto}: distancia = {distancia:.3f} (mínimo requerido: {radio_seguro})")
    
    return min(distancias_minimas), np.mean(distancias_minimas)

def optimizar_nodos_simple(nodos, obstaculos, radio_seguro):
    nodos_opt = []
    for nodo in nodos:
        # Convertir a array si no lo es
        if not isinstance(nodo, np.ndarray):
            p = np.array(nodo, dtype=float)
        else:
            p = nodo.copy()
        
        # Verificar distancia a cada obstáculo
        for obstaculo in obstaculos:
            distancia = np.linalg.norm(p - obstaculo)
            if distancia < radio_seguro * 1.2:
                # Mover el punto alejándolo del obstáculo
                direccion = p - obstaculo
                if np.linalg.norm(direccion) > 0:
                    direccion = direccion / np.linalg.norm(direccion)
                    p += direccion * (radio_seguro * 1.2 - distancia)
        
        nodos_opt.append(p)
    
    return nodos_opt
