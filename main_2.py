import numpy as np
import manejo_graficas_2 as mg
import generar_nodos_2 as gn
import matplotlib.pyplot as plt
from datos_prueba import casos_prueba

def generar_trayectoria(punto_inicial,punto_final,obstaculos,radio_seguro):
    # Genera ruta inicial usando Dijkstra
    ruta = gn.calcular(punto_inicial, punto_final, obstaculos, radio_seguro)
    print(f"Numero de puntos en la ruta: {len(ruta)}")

    #Optimizar manualmente los puntos de control
    nodos_optimizados = []
    if len(ruta) >= 4: 

        indices = [0] 
        paso = max(1, len(ruta) // 4)
        for i in range(paso, len(ruta) - 1, paso):
            indices.append(i)
        indices.append(len(ruta) - 1)  
        
        for idx in indices:
            nodos_optimizados.append(ruta[idx])
    else:
        nodos_optimizados = ruta.copy()

    #Verificar que los nodos esten a una distancia de seguridad correcta
    for i, nodo in enumerate(nodos_optimizados):
        for obstaculo in obstaculos:
            distancia = np.linalg.norm(nodo - obstaculo)
            if distancia < radio_seguro:
                direccion = nodo - obstaculo
                if np.linalg.norm(direccion) > 0:
                    direccion = direccion / np.linalg.norm(direccion)
                    nodos_optimizados[i] = obstaculo + direccion * (radio_seguro + 0.1)

    #Graficar la curva de Bezier
    fig, ax = plt.subplots(figsize=(10, 8))
    puntos_curva = mg.graficar_curva_bezier(nodos_optimizados, obstaculos, radio_seguro)
    mg.graficar_obstaculos_nodos(obstaculos, nodos_optimizados, radio_seguro)

    # Calcular informacion sobre la trayectoria
    if len(puntos_curva) > 0:
        distancias = []
        for punto in puntos_curva:
            dist_min = min([np.linalg.norm(punto - o) for o in obstaculos])
            distancias.append(dist_min)
        
        dist_min_total = min(distancias)
        dist_prom = np.mean(distancias)
    
        print(f"  Distancia minima a obstaculos: {dist_min_total:.3f}")
        print(f"  Distancia promedio: {dist_prom:.3f}")
        print(f"  Radio seguro: {radio_seguro}")
        
        if dist_min_total >= radio_seguro:
            print("La trayectoria es segura")
        else:
            print("La trayectoria no es segura")
    else:
        print("No se pudieron generar puntos de la curva")
    print(f"\nPuntos de control utilizados: {len(nodos_optimizados)}")
    for i, nodo in enumerate(nodos_optimizados):
        print(f"  Nodo {i}: ({nodo[0]:.2f}, {nodo[1]:.2f})")

    plt.show()

# Ejecutar todas las pruebas
for i, caso in enumerate(casos_prueba):
    print(f"\n{'='*60}")
    print(f"Caso {i+1}/{len(casos_prueba)}: n={caso['n']}, conjunto={caso['conjunto']}")
    print(f"Punto inicial: {caso['punto_inicial']}")
    print(f"Punto final: {caso['punto_final']}")
    print(f"Numero de obstaculos: {len(caso['obstaculos'])}")
    
    generar_trayectoria(
        caso['punto_inicial'], 
        caso['punto_final'], 
        caso['obstaculos'], 
        caso['radio_seguro'],
    )
