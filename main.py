import numpy as np
import math

def curva_bezier(t,puntos_medios): 
    n = len(puntos_medios)
    suma_final = 0

    for k in range(n):
        suma_final += ( math.comb(n-1,k) * (t**k) * ((1-t)**(n-1-k))) * puntos_medios[k]
    
    return suma_final

