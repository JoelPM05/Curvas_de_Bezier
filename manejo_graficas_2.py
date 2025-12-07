import numpy as np
import matplotlib.pyplot as plt

def curva_bezier(t, nodos):
    # Convertir nodos a arrays de numpy si no lo son
    nodos_array = [np.array(p, dtype=float) for p in nodos]
    n = len(nodos_array)
    
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

def graficar_curva_bezier(nodos, obstaculos, radio_seguro):
    t = np.linspace(0, 1, 500)
    nodos_array = []
    for nodo in nodos:
        if isinstance(nodo, (list, tuple)):
            nodos_array.append(np.array(nodo, dtype=float))
        else:
            nodos_array.append(nodo)
    
    puntos_curva = curva_bezier(t, nodos_array)
    if puntos_curva.ndim == 2:
        xs = puntos_curva[:, 0]
        ys = puntos_curva[:, 1]
    else:
        xs = [p[0] for p in puntos_curva]
        ys = [p[1] for p in puntos_curva]
    plt.plot(xs, ys, linewidth=2, label="Trayectoria Bezier")
    
    # Verificar distancia a obstaculos
    puntos_cercanos = []
    for pt in puntos_curva:
        for obs in obstaculos:
            distancia = np.linalg.norm(pt - obs)
            if distancia < radio_seguro:
                puntos_cercanos.append((pt, obs, distancia))
        
    if puntos_cercanos:
        print(f"\nHay {len(puntos_cercanos)} puntos cercanos a obstaculos")
        for i, (punto, obstaculo, distancia) in enumerate(puntos_cercanos[:3]):
            print(f"  Punto {punto}: distancia a {obstaculo} = {distancia:.3f}")
    
    return puntos_curva

def graficar_obstaculos_nodos(obstaculos, nodos, radio_seguro=1.0):
    # Graficar puntos de control
    x_control = [p[0] for p in nodos]
    y_control = [p[1] for p in nodos]
    plt.scatter(x_control, y_control, color='green', s=100, zorder=5, label="Puntos de control")
    
    # Graficar obstaculos con circulos de seguridad
    for obstaculo in obstaculos:
        plt.scatter(obstaculo[0], obstaculo[1], color='red', s=150, zorder=5)
        # Dibujar circulo de seguridad
        circle = plt.Circle(obstaculo, radio_seguro, color='red', alpha=0.2, zorder=3)
        plt.gca().add_patch(circle)
    
    # Dibujar linea entre puntos de control
    plt.plot(x_control, y_control, 'g--', alpha=0.5, linewidth=1, label="Poligono de control")
    
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.xlabel("X")
    plt.ylabel("Y")
    
    # Ajustar limites del grafico
    all_x = x_control + [o[0] for o in obstaculos]
    all_y = y_control + [o[1] for o in obstaculos]
    plt.xlim(min(all_x) - 2, max(all_x) + 2)
    plt.ylim(min(all_y) - 2, max(all_y) + 2)
