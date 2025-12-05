from math import sqrt
def distancia_recta_punto(punto,punto_inicial,punto_final):
    A = (punto_inicial[1]-punto_final[1])/(punto_inicial[0]-punto_final[0])
    B = -1
    C = punto_inicial[1] - A * punto_inicial[0]

    distancia = abs(A*punto[0] + B*punto[1] + C)/sqrt(A**2 + B**2)
    return distancia


def calcular(punto_inicial,punto_final,obstaculos,radio_seguro):
    n = len(obstaculos)
    for k in range(n):
        if distancia_recta_punto(obstaculos[k],punto_inicial,punto_final) > radio_seguro:
            continue
