import numpy as np
import matplotlib.pyplot as plt
import math

def curva_bezier(t,puntos_medios): 
    # Usamos el algoritmo de Casteljau para evaluar la curva de Bezier
    n = len(puntos_medios)
    ptos_medios_aprox = puntos_medios.copy()

    for j in range (1,n):
        for k in range(n-j):
            ptos_medios_aprox[k] = ptos_medios_aprox[k]*(1-t) + ptos_medios_aprox[k+1]*t

    return ptos_medios_aprox[0]

def graficar_curva_bezier(puntos_medios):
    x = np.linspace(0,1,200)
    puntos = np.array([curva_bezier(xi, puntos_medios) for xi in x])

    xs = puntos[:,0]
    ys = puntos[:,1]

    plt.plot(xs, ys, label="Curva Bezier")
    plt.scatter(*zip(*puntos_medios), color='red', label="Puntos de control")
    plt.legend()
    plt.axis('equal')
    plt.show()

nodos = [np.array([0,0]),np.array([1,3]),np.array([2,2])]
graficar_curva_bezier(nodos)
