import numpy as np
import manejo_graficas_2 as mg
import generar_nodos_2 as gn
import verifica_trayectorias as vt
import matplotlib.pyplot as plt

# Configuración
pto_inicial = np.array([0, 0])
pto_final = np.array([10, 12])
obs = [
    np.array([1, 1]), np.array([1, 2]), np.array([2, 0]),
    np.array([4, 2]), np.array([5, 5]), np.array([7, 2]),
    np.array([12, 5]), np.array([13, 4]), np.array([13, 5]),
    np.array([15, 6]),np.array([12,18]),np.array([20,30])
]
radio_seguro = 1.0

# 1. Generar ruta inicial usando Dijkstra
print("Generando ruta inicial con Dijkstra...")
ruta = gn.calcular(pto_inicial, pto_final, obs, radio_seguro)

print(f"Número de puntos en la ruta: {len(ruta)}")

# 2. Optimizar manualmente los puntos de control (versión simple)
print("Optimizando puntos de control...")
nodos_optimizados = []

# Tomar puntos clave de la ruta (inicio, fin y algunos intermedios)
if len(ruta) >= 4:
    # Tomar puntos distribuidos
    indices = [0]  # Inicio
    paso = max(1, len(ruta) // 4)
    for i in range(paso, len(ruta) - 1, paso):
        indices.append(i)
    indices.append(len(ruta) - 1)  # Fin
    
    for idx in indices:
        nodos_optimizados.append(ruta[idx])
else:
    nodos_optimizados = ruta.copy()

# 3. Verificar que los nodos estén seguros
for i, nodo in enumerate(nodos_optimizados):
    for obstaculo in obs:
        distancia = np.linalg.norm(nodo - obstaculo)
        if distancia < radio_seguro:
            # Ajustar nodo
            direccion = nodo - obstaculo
            if np.linalg.norm(direccion) > 0:
                direccion = direccion / np.linalg.norm(direccion)
                nodos_optimizados[i] = obstaculo + direccion * (radio_seguro + 0.1)

# 4. Generar y graficar curva de Bézier
print("Generando curva de Bézier...")
fig, ax = plt.subplots(figsize=(10, 8))

# Primero graficar la curva
puntos_curva = mg.graficar_curva_bezier(nodos_optimizados, obs, radio_seguro)

# Luego graficar obstáculos y nodos
mg.graficar_obstaculos_nodos(obs, nodos_optimizados, radio_seguro)

# 5. Verificar distancia mínima
print("\nVerificando seguridad de la trayectoria...")
if len(puntos_curva) > 0:
    distancias = []
    for punto in puntos_curva:
        dist_min = min([np.linalg.norm(punto - o) for o in obs])
        distancias.append(dist_min)
    
    dist_min_total = min(distancias)
    dist_prom = np.mean(distancias)
    
    print(f"\nResumen:")
    print(f"  Distancia mínima a obstáculos: {dist_min_total:.3f}")
    print(f"  Distancia promedio: {dist_prom:.3f}")
    print(f"  Radio seguro requerido: {radio_seguro}")
    
    if dist_min_total >= radio_seguro:
        print("  ✓ TRAYECTORIA SEGURA")
    else:
        print("  ✗ TRAYECTORIA NO SEGURA - Ajuste necesario")
else:
    print("No se pudieron generar puntos de la curva")

# 6. Mostrar información adicional
print(f"\nPuntos de control utilizados: {len(nodos_optimizados)}")
for i, nodo in enumerate(nodos_optimizados):
    print(f"  Nodo {i}: ({nodo[0]:.2f}, {nodo[1]:.2f})")

plt.show()
