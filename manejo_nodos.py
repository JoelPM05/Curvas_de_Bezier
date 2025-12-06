import numpy as np
def separacion_nodos(nodos):
    n = len(nodos)

    paquete_nodos = [nodos[:5]] #Se encarga de divir los nodos en paquetes de 5 nodos
    k = 1
    while 5*(k+1) <= n:
        paquete_nodos.append(nodos[k:k+5])
        k += 1
    if n == 5*k:
        return paquete_nodos
    
    elif n- 5*k < 3:              #Distribuye los que sobraron si no es multiplo de 5
        paquete_nodos[k-1] = np.concatenate([paquete_nodos[k-1],nodos[5*k:n]])
    else:
        paquete_nodos.append(nodos[5*k:n])

    return paquete_nodos

def conectando_nodos(paquete_nodos):
    k = len(paquete_nodos)
    nuevos_nodos = []
    for i in range(k):
        if(i+1 >= k):
            nuevos_nodos.append(paquete_nodos[i])
            break

        s = len(paquete_nodos[i])
        middle_point1 = (paquete_nodos[i][s-2] + paquete_nodos[i][s-1])/2
        middle_point2 = paquete_nodos[i][s-1]
        middle_point3 = (paquete_nodos[i][s-1] + paquete_nodos[i+1][0])/2



        nuevos_nodos.append(np.concatenate([paquete_nodos[i][:s-2],[middle_point1]]))
        nuevos_nodos.append([middle_point1,middle_point2,middle_point3])
        paquete_nodos[i+1] = [middle_point3].append(paquete_nodos[i+1])
    return nuevos_nodos