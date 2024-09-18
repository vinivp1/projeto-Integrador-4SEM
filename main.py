import heapq
from grafo import grafo

def dijkstra(grafo, inicio, destino):
    distancias = {nó: float('inf') for nó in grafo}
    distancias[inicio] = 0
    predecessores = {}

    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        (dist_atual, nó_atual) = heapq.heappop(fila_prioridade)

        if dist_atual > distancias[nó_atual]:
            continue

        for vizinho, peso in grafo[nó_atual].items():
            distancia = dist_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                predecessores[vizinho] = nó_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    # Reconstruir o caminho
    caminho = []
    nó_atual = destino
    while nó_atual != inicio:
        caminho.append(nó_atual)
        nó_atual = predecessores[nó_atual]
    caminho.append(inicio)
    caminho.reverse()

    return distancias, caminho

grafo = grafo

inicio = 'SP'
destino = 'BA'
distancias, caminho_mais_curto = dijkstra(grafo, inicio, destino)
print(f"Distância mais curta de {inicio} para {destino}: {distancias[destino]}km")
print(f"Caminho mais curto: {caminho_mais_curto}")
