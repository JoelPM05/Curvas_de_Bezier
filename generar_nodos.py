from math import sqrt
import numpy as np

def distancia_recta_punto(punto,punto_inicial,punto_final):
    A = (punto_inicial[1]-punto_final[1])/(punto_inicial[0]-punto_final[0])
    B = -1
    C = punto_inicial[1] - A * punto_inicial[0]

    distancia = abs(A*punto[0] + B*punto[1] + C)/sqrt(A**2 + B**2)
    return distancia


def calcular(punto_inicial,punto_final,obstaculos,radio_seguro):
    nodos = [punto_inicial]

    n = len(obstaculos)
    for k in range(n):
        if distancia_recta_punto(obstaculos[k],punto_inicial,punto_final) > radio_seguro:
            continue

        A = (punto_inicial[1]-punto_final[1])/(punto_inicial[0]-punto_final[0])
        vector_perpendicular = np.array([A,-1])
        vector_perpendicular /= np.linalg.norm(vector_perpendicular)

        nodos.append(obstaculos[k]+(2 * radio_seguro)*vector_perpendicular)
    
    nodos.append(punto_final)
    return nodos