import numpy as np
import matplotlib.pyplot as plt
import math
import nodos_puntuales




pto_inicial = np.array([0,0])
pto_final = np.array([8,3])
obs = [np.array([1,2]),np.array([2,0]),np.array([4,2]),np.array([5,5]),np.array([7,2])]
nod = nodos_puntuales.calcular(pto_inicial,pto_final,obs,1)
nodos_puntuales.graficar_curva_bezier(nod,obs)


def graficar_curva_bezier(nodos):
    x = np.linspace(0,1,200)
    puntos = np.array([curva_bezier(xi, nodos) for xi in x])

    xs = puntos[:,0]
    ys = puntos[:,1]

    plt.plot(xs, ys, label="Curva Bezier")
    plt.scatter(*zip(*nodos), color='red', label="Puntos de control")
    plt.legend()
    plt.axis('equal')
    plt.show()