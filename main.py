import numpy as np
import matplotlib.pyplot as plt
import math

def curva_bezier(t,puntos_medios): 
    n = len(puntos_medios)
    suma_final = 0

    for k in range(n):
        suma_final += ( math.comb(n-1,k) * (t**k) * ((1-t)**(n-1-k))) * puntos_medios[k]
    
    return suma_final

def graficar_curva_bezier(puntos_medios):
    x = np.linspace(0,1,100)
    y = [curva_bezier(xi) for xi in x ]

    plt.plot(x,y)
    return