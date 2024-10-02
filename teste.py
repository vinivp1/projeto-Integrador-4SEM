import tkinter as tk
from tkinter import messagebox
import heapq
from grafo import grafo

# Algoritmo de Dijkstra
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

# Função para abrir a janela pop-up com os resultados
def mostrar_resultado(distancia, caminho):
    resultado_popup = tk.Toplevel()
    resultado_popup.title("Resultado")

    texto_resultado = f"Distância mais curta: {distancia}km\nCaminho mais curto: {caminho}"
    label_resultado = tk.Label(resultado_popup, text=texto_resultado, padx=20, pady=20)
    label_resultado.pack()

    fechar_botao = tk.Button(resultado_popup, text="Fechar", command=resultado_popup.destroy)
    fechar_botao.pack()

# Função que executa o algoritmo Dijkstra e exibe os resultados
def calcular_dijkstra():
    inicio = entrada_inicio.get().upper()
    destino = entrada_destino.get().upper()

    if inicio not in grafo or destino not in grafo:
        messagebox.showerror("Erro", "Por favor, insira estados válidos.")
        return

    try:
        distancias, caminho_mais_curto = dijkstra(grafo, inicio, destino)
        mostrar_resultado(distancias[destino], caminho_mais_curto)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao calcular o caminho: {e}")

# Janela principal
root = tk.Tk()
root.title("PROGRAMA CAMINHO CERTO")
root.geometry("800x500")

# Texto de introdução
label_texto = tk.Label(root, text=("Escolha os estados para calcular a menor rota.\n"
                                   "Estados: AC, AL, AP, AM, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA, PB, PR, PE, PI,\n"
                                   "RJ, RN, RS, RO, RR, SC, SP, SE, TO"), padx=20, pady=20)
label_texto.pack()

# Campo de entrada para o estado de início
label_inicio = tk.Label(root, text="Estado de Início:")
label_inicio.pack()
entrada_inicio = tk.Entry(root)
entrada_inicio.pack()

# Campo de entrada para o estado de destino
label_destino = tk.Label(root, text="Estado de Destino:")
label_destino.pack()
entrada_destino = tk.Entry(root)
entrada_destino.pack()

# Botão para calcular o caminho
botao_calcular = tk.Button(root, text="Calcular Caminho", command=calcular_dijkstra)
botao_calcular.pack(pady=20)

# Executar a janela principal
root.mainloop()
