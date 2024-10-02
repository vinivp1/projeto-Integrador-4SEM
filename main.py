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

    caminho = []
    nó_atual = destino
    while nó_atual != inicio:
        caminho.append(nó_atual)
        nó_atual = predecessores[nó_atual]
    caminho.append(inicio)
    caminho.reverse()

    return distancias, caminho

grafo = grafo

print("PROGRAMA CAMINHO CERTO")
print("Estados: Acre (AC), Alagoas (AL), Amapá (AP), Amazonas (AM), Bahia (BA), Ceará (CE), Distrito Federal (DF), Espírito Santo (ES),"
      "\n Goiás (GO), Maranhão (MA), Mato Grosso (MT), Mato Grosso do Sul (MS), Minas Gerais (MG), Pará (PA), Paraíba (PB), Paraná (PR), Pernambuco (PE),"
      "\n Piauí (PI) ,Rio de Janeiro (RJ), Rio Grande do Norte (RN), Rio Grande do Sul (RS), Rondônia (RO), Roraima (RR), Santa Catarina (SC), São Paulo (SP),"
      "\n Sergipe (SE), Tocantins (TO)")

inicio = input("\nEscolha o estado para o início da viagem?").upper().strip()
destino = input("Escolha o estado para a chegada da viagem?").upper().strip()
distancias, caminho_mais_curto = dijkstra(grafo, inicio, destino)
print(f"\nDistância mais curta de {inicio} para {destino}: {distancias[destino]}km")
print(f"Caminho mais curto: {caminho_mais_curto}")
