import numpy as np
import nodos_puntuales




pto_inicial = np.array([0,0])
pto_final = np.array([8,3])
obs = [np.array([1,2]),np.array([2,0]),np.array([4,2]),np.array([5,5]),np.array([7,2])]


def curva_bezier(punto_inicial,punto_final,obstaculos,radio_seguro):
    nodos = nodos_puntuales.calcular(punto_inicial,punto_final,obstaculos,radio_seguro)
    nodos_puntuales.graficar_curva_bezier(nodos,obstaculos)
    return

def curva_bezier_por_partes(punto_inicial,punto_final,obstaculos,radio_seguro):
    nodos = nodos_puntuales.calcular(punto_inicial,punto_final,obstaculos,radio_seguro)

    n = len(nodos)
    if n < 5:
        nodos_puntuales.graficar_curva_bezier(nodos,obstaculos)
        return

    paquete_nodos = [nodos[:5]] #Se encarga de divir los nodos en paquetes de 5 nodos
    k = 1
    while 5*(k+1) <= n:
        paquete_nodos.append(nodos[k:k+5])
        k += 1
    
    if n- 5*k < 3:
        paquete_nodos[k-1].concatenate(nodos[5*k:n])
    else:
        paquete_nodos.append(nodos[5*k:n])