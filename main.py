import numpy as np
import manejo_graficas
import manejo_nodos

#falta ver error con el len(nodos)

def curva_bezier(punto_inicial,punto_final,obstaculos,radio_seguro):
    nodos = manejo_graficas.calcular(punto_inicial,punto_final,obstaculos,radio_seguro)
    manejo_graficas.graficar_curva_bezier(nodos)
    manejo_graficas.graficar_obstaculos_nodos(nodos,obstaculos)
    return

def curva_bezier_por_partes(punto_inicial,punto_final,obstaculos,radio_seguro):
    nodos = manejo_graficas.calcular(punto_inicial,punto_final,obstaculos,radio_seguro)
    n = len(nodos)
    if n < 5:
        manejo_graficas.graficar_curva_bezier(nodos)
        return
    
    paquete_nodos = manejo_nodos.separacion_nodos(nodos)
    paquete_nodos = manejo_nodos.conectando_nodos(paquete_nodos)

    k = len(paquete_nodos)
    print(k)
    for i in range(k):
        manejo_graficas.graficar_curva_bezier(paquete_nodos[i])

    nuevos_nodos = np.unique(np.concatenate(paquete_nodos))
    manejo_graficas.graficar_obstaculos_nodos(obstaculos,nuevos_nodos)



pto_inicial = np.array([0,0])
pto_final = np.array([17,6])
obs = [np.array([1,1]),np.array([1,2]),np.array([2,0]),np.array([4,2]),np.array([5,5]),np.array([7,2]),np.array([12,5]),np.array([13,4]),np.array([13,5]),np.array([15,6])]
curva_bezier(pto_inicial,pto_final,obs,1)
curva_bezier_por_partes(pto_inicial,pto_final,obs,1)