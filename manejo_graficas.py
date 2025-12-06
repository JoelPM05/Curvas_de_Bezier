from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def curva_bezier(t,nodos): 
    # Usamos el algoritmo de Casteljau para evaluar la curva de Bezier
    n = len(nodos)
    ptos_medios_aprox = nodos.copy()

    for j in range (1,n):
        for k in range(n-j):
            ptos_medios_aprox[k] = ptos_medios_aprox[k]*(1-t) + ptos_medios_aprox[k+1]*t

    return ptos_medios_aprox[0]

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

def graficar_curva_bezier(nodos):
    x = np.linspace(0,1,200)
    puntos = np.array([curva_bezier(xi, nodos) for xi in x])

    xs = puntos[:,0]
    ys = puntos[:,1]

    plt.plot(xs, ys)
    return
    

def graficar_obstaculos_nodos(obstaculos,nodos):
    plt.scatter(*zip(*nodos), color='green', label="Puntos de control")
    plt.scatter(*zip(*obstaculos), color='red', label="Obstaculos")
    plt.legend()
    plt.axis('equal')
    plt.show()