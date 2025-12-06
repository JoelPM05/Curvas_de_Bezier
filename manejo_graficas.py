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