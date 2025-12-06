import numpy as np
import matplotlib.pyplot as plt

def curva_bezier(t, nodos):
    """
    Calcula un punto en la curva de Bézier usando el algoritmo de Casteljau.
    t: parámetro escalar o array de parámetros
    nodos: lista de puntos de control
    """
    # Convertir nodos a arrays de numpy si no lo son
    nodos_array = [np.array(p, dtype=float) for p in nodos]
    n = len(nodos_array)
    
    # Si t es un array, procesar cada valor individualmente
    if isinstance(t, np.ndarray):
        # Para array de t, calcular punto por punto
        puntos = []
        for ti in t:
            ptos_medios = nodos_array.copy()
            for j in range(1, n):
                for k in range(n - j):
                    ptos_medios[k] = (1 - ti) * ptos_medios[k] + ti * ptos_medios[k + 1]
            puntos.append(ptos_medios[0])
        return np.array(puntos)
    else:
        # Para t escalar
        ptos_medios = nodos_array.copy()
        for j in range(1, n):
            for k in range(n - j):
                ptos_medios[k] = (1 - t) * ptos_medios[k] + t * ptos_medios[k + 1]
        return ptos_medios[0]

def graficar_curva_bezier(nodos, obstaculos=None, radio_seguro=1.0):
    """
    Grafica la curva de Bézier y verifica distancia a obstáculos
    """
    # Generar puntos de la curva
    t = np.linspace(0, 1, 500)
    
    # Verificar que nodos sean arrays de numpy
    nodos_array = []
    for nodo in nodos:
        if isinstance(nodo, (list, tuple)):
            nodos_array.append(np.array(nodo, dtype=float))
        else:
            nodos_array.append(nodo)
    
    puntos_curva = curva_bezier(t, nodos_array)
    
    # Extraer coordenadas para graficar
    if puntos_curva.ndim == 2:
        xs = puntos_curva[:, 0]
        ys = puntos_curva[:, 1]
    else:
        xs = [p[0] for p in puntos_curva]
        ys = [p[1] for p in puntos_curva]
    
    plt.plot(xs, ys, linewidth=2, label="Trayectoria Bézier")
    
    # Verificar distancia a obstáculos si se proporcionan
    if obstaculos is not None:
        puntos_cercanos = []
        for punto in puntos_curva:
            for obstaculo in obstaculos:
                distancia = np.linalg.norm(punto - obstaculo)
                if distancia < radio_seguro:
                    puntos_cercanos.append((punto, obstaculo, distancia))
        
        if puntos_cercanos:
            print(f"\n¡ADVERTENCIA! Se encontraron {len(puntos_cercanos)} puntos cercanos a obstáculos")
            for i, (punto, obstaculo, distancia) in enumerate(puntos_cercanos[:3]):
                print(f"  Punto {punto}: distancia a {obstaculo} = {distancia:.3f}")
    
    return puntos_curva

def graficar_obstaculos_nodos(obstaculos, nodos, radio_seguro=1.0):
    """
    Grafica obstáculos, círculos de seguridad y puntos de control
    """
    # Graficar puntos de control
    x_control = [p[0] for p in nodos]
    y_control = [p[1] for p in nodos]
    plt.scatter(x_control, y_control, color='green', s=100, zorder=5, label="Puntos de control")
    
    # Graficar obstáculos con círculos de seguridad
    for obstaculo in obstaculos:
        plt.scatter(obstaculo[0], obstaculo[1], color='red', s=150, zorder=5)
        # Dibujar círculo de seguridad
        circle = plt.Circle(obstaculo, radio_seguro, color='red', alpha=0.2, zorder=3)
        plt.gca().add_patch(circle)
    
    # Dibujar línea entre puntos de control
    plt.plot(x_control, y_control, 'g--', alpha=0.5, linewidth=1, label="Polígono de control")
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.title("Trayectoria con Evasión de Obstáculos")
    plt.xlabel("X")
    plt.ylabel("Y")
    
    # Ajustar límites del gráfico
    all_x = x_control + [o[0] for o in obstaculos]
    all_y = y_control + [o[1] for o in obstaculos]
    plt.xlim(min(all_x) - 2, max(all_x) + 2)
    plt.ylim(min(all_y) - 2, max(all_y) + 2)
