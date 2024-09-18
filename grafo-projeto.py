import heapq

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

grafo = {
    'AC' : {'AC':0, 'AL':4119, 'AP':3194, 'AM':1444, 'BA':3768, 'CE':4.194, 'DF':3055, 'ES':3618, 'GO':2862, 'MA':3656, 'MT':2075, 'MS':2494, 'MG':3489, 'PA':3379, 'PB':4343, 'PR':3616, 'PE':4252, 'PI':3670, 'RJ':3678, 'RN':4526, 'RS':3787, 'RO':510, 'RR':2959, 'SC':3694, 'SP':3451, 'SE':4000, 'TO':2885},
    'AL' : {'AC': 4119, 'AL':0, 'AP':2171, 'AM':4666, 'BA':601, 'CE':1070, 'DF':1792, 'ES':1367, 'GO':2067, 'MA':1655, 'MT':2815, 'MS':2697, 'MG':1664, 'PA':2425, 'PB':390, 'PR':2720, 'PE':285, 'PI':1216, 'RJ':1932, 'RN':695, 'RS':3402, 'RO':3929, 'RR':5309, 'SC':2917, 'SP':2153, 'SE':294, 'TO':1841},
    'AP' : {'AC': 3194, 'AL': 2171, 'AP':0, 'AM': 1459, 'BA': 2108, 'CE': 1340, 'DF': 1888, 'ES': 2560, 'GO': 2023, 'MA': 578, 'MT': 2354, 'MS': 2993, 'MG': 2471, 'PA': 332, 'PB': 2350, 'PR': 3238, 'PE': 2185, 'PI': 1389, 'RJ': 2814, 'RN': 2524, 'RS': 3797, 'RO': 3017, 'RR': 1525, 'SC': 3435, 'SP': 2924, 'SE': 2211, 'TO': 1504},
    'AM' : {'AC': 1444, 'AL': 4666, 'AP': 1459, 'AM':0, 'BA': 4013, 'CE': 3592, 'DF': 3495, 'ES': 4234, 'GO': 3557, 'MA': 2770, 'MT': 2358, 'MS': 2687, 'MG': 3948, 'PA': 529, 'PB': 4555, 'PR': 4262, 'PE': 4369, 'PI': 3521, 'RJ': 4309, 'RN': 4756, 'RS': 4912, 'RO': 890, 'RR': 785, 'SC': 4459, 'SP': 3944, 'SE': 4598, 'TO': 2695},
    'BA' : {'AC': 3768, 'AL': 601, 'AP': 2108, 'AM': 4013, 'BA':0, 'CE': 1029, 'DF': 1446, 'ES': 1.204, 'GO': 1590, 'MA': 1.570, 'MT': 2187, 'MS': 2306, 'MG': 1372, 'PA': 2129, 'PB': 1038, 'PR': 2628, 'PE': 838, 'PI': 1.014, 'RJ': 1.643, 'RN': 1.185, 'RS': 3087, 'RO': 3.630, 'RR': 4.869, 'SC': 2832, 'SP': 1960, 'SE': 356, 'TO': 1.467},
    'CE' : {'AC': 4194, 'AL': 1070, 'AP': 1340, 'AM': 3592, 'BA': 1029,'CE':0, 'DF': 2206, 'ES': 2006, 'GO': 2260, 'MA': 1037, 'MT': 2911, 'MS': 3135, 'MG': 2382, 'PA': 1617, 'PB': 688, 'PR': 3541, 'PE': 800, 'PI': 634, 'RJ': 2805, 'RN': 533, 'RS': 4006, 'RO': 4284, 'RR': 4571, 'SC': 3744, 'SP': 2684, 'SE': 1162, 'TO': 1595},
    'ES' : {'AC': 3618, 'AL': 1367, 'AP': 2560, 'AM': 4234, 'BA': 1204, 'CE': 2006, 'ES':0, 'DF': 1232, 'GO': 1342, 'MA': 2139, 'MT': 1848, 'MS': 1808, 'MG': 524, 'PA': 2726, 'PB': 2077, 'PR': 1376, 'PE': 1891, 'PI': 2061, 'RJ': 521, 'RN': 2305, 'RS': 1929, 'RO': 3275, 'RR': 4761, 'SC': 1644, 'SP': 882, 'SE': 1123, 'TO': 1754},
    'GO' : {'AC': 2862, 'AL': 2067, 'AP': 2023, 'AM': 3557, 'BA': 1590, 'CE': 2260, 'DF': 209, 'ES': 1342, 'GO':0, 'MA': 1536, 'MT': 891, 'MS': 926, 'MG': 906, 'PA': 1883, 'PB': 2214, 'PR': 1186, 'PE': 2160, 'PI': 1521, 'RJ': 1275, 'RN': 2455, 'RS': 1821, 'RO': 2208, 'RR': 3758, 'SC': 1626, 'SP': 926, 'SE': 1832, 'TO': 874},
    'MA' : {'AC': 3656, 'AL': 1655, 'AP': 578, 'AM': 2770, 'BA': 1570, 'CE': 1037, 'DF': 2115, 'ES': 2139, 'GO': 1536, 'MA':0, 'MT': 2255, 'MS': 2685, 'MG': 2243, 'PA': 806, 'PB': 1607, 'PR': 3213, 'PE': 1338, 'PI': 954, 'RJ': 2802, 'RN': 1482, 'RS': 3678, 'RO': 3468, 'RR': 3349, 'SC': 3472, 'SP': 2823, 'SE': 1760, 'TO': 1452},
    'MT' : {'AC': 2075, 'AL': 2815, 'AP': 2354, 'AM': 2358, 'BA': 2187, 'CE': 2911, 'DF': 1132, 'ES': 1848, 'GO': 891, 'MA': 2255, 'MT':0, 'MS': 694, 'MG': 1583, 'PA': 1771, 'PB': 2949, 'PR': 1581, 'PE': 2805, 'PI': 2124, 'RJ': 1879, 'RN': 3190, 'RS': 2267, 'RO': 1458, 'RR': 3144, 'SC': 1778, 'SP': 1605, 'SE': 2662, 'TO': 1289},
    'MS' : {'AC': 2494, 'AL': 2697, 'AP': 2993, 'AM': 2687, 'BA': 2306, 'CE': 3135, 'DF': 1134, 'ES': 1808, 'GO': 935, 'MA': 2685, 'MT': 694, 'MS':0, 'MG': 1620, 'PA': 2373, 'PB': 2827, 'PR': 991, 'PE': 2678, 'PI': 2386, 'RJ': 1446, 'RN': 3073, 'RS': 1602, 'RO': 1837, 'RR': 3569, 'SC': 1293, 'SP': 1014, 'SE': 2552, 'TO': 1589},
    'MG' : {'AC': 3489, 'AL': 1664, 'AP': 2471, 'AM': 3948, 'BA': 1372, 'CE': 2382, 'DF': 716, 'ES': 524, 'GO': 906, 'MA': 2243, 'MT': 1583, 'MS': 1620, 'MG':0, 'PA': 2584, 'PB': 2073, 'PR': 1000, 'PE': 1895, 'PI': 1925, 'RJ': 434, 'RN': 2318, 'RS': 1711, 'RO': 2909, 'RR': 4515, 'SC': 1309, 'SP': 586, 'SE': 1315, 'TO': 1486},
    'PA' : {'AC': 3379, 'AL': 2425, 'AP': 332, 'AM': 529, 'BA': 2129, 'CE': 1617, 'DF': 2116, 'ES': 2726, 'GO': 1883, 'MA': 806, 'MT': 1771, 'MS': 2373, 'MG': 2584, 'PB': 2271, 'PR': 3166, 'PE': 2106, 'PI': 1301, 'RJ': 2925, 'RN': 2504, 'RS': 3735, 'RO': 2891, 'RR': 2613, 'SC': 3394, 'SP': 2937, 'SE': 2322, 'TO': 1286},
    'PB' : {'AC': 4292, 'AL': 390, 'AP': 2350, 'AM': 4555, 'BA': 1038, 'CE': 688, 'DF': 2220, 'ES': 2077, 'GO': 2214, 'MA': 1607, 'MT': 2949, 'MS': 2827, 'MG': 2073, 'PA': 2271, 'PR': 3230, 'PE': 120, 'PI': 1044, 'RJ': 2355, 'RN': 185, 'RS': 3785, 'RO': 3950, 'RR': 4811, 'SC': 3412, 'SP': 2733, 'SE': 645, 'TO': 2047},
    'PR' : {'AC': 3229, 'AL': 2720, 'AP': 3238, 'AM': 4262, 'BA': 2628, 'CE': 3541, 'DF': 1366, 'ES': 1376, 'GO': 1186, 'MA': 3213, 'MT': 1581, 'MS': 991, 'MG': 1000, 'PA': 3166, 'PB': 3230, 'PE': 3151, 'PI': 3137, 'RJ': 852, 'RN': 3455, 'RS': 711, 'RO': 2615, 'RR': 4501, 'SC': 300, 'SP': 408, 'SE': 2774, 'TO': 1908},
    'PE' : {'AC': 4396, 'AL': 285, 'AP': 2185, 'AM': 4369, 'BA': 838, 'CE': 800, 'DF': 2120, 'ES': 1891, 'GO': 2160, 'MA': 1338, 'MT': 2805, 'MS': 2678, 'MG': 1895, 'PA': 2106, 'PB': 120, 'PR': 3151, 'PI': 1053, 'RJ': 2285, 'RN': 297, 'RS': 3699, 'RO': 3846, 'RR': 4707, 'SC': 3344, 'SP': 2669, 'SE': 501, 'TO': 1947},
    'PI' : {'AC': 3955, 'AL': 1216, 'AP': 1389, 'AM': 3521, 'BA': 1014, 'CE': 634, 'DF': 1783, 'ES': 2061, 'GO': 1521, 'MA': 954, 'MT': 2124, 'MS': 2386, 'MG': 1925, 'PA': 1301, 'PB': 1044, 'PR': 3137, 'PE': 1053, 'RJ': 2268, 'RN': 1104, 'RS': 3676, 'RO': 3180, 'RR': 3896, 'SC': 3337, 'SP': 2484, 'SE': 1344, 'TO': 1029},
    'RJ' : {'AC': 3401, 'AL': 1932, 'AP': 2814, 'AM': 4309, 'BA': 1643, 'CE': 2805, 'DF': 1169, 'ES': 521, 'GO': 1275, 'MA': 2802, 'MT': 1879, 'MS': 1446, 'MG': 434, 'PA': 2925, 'PB': 2355, 'PR': 852, 'PE': 2285, 'PI': 2268, 'RN': 2570, 'RS': 1555, 'RO': 3048, 'RR': 4616, 'SC': 1122, 'SP': 434, 'SE': 1868, 'TO': 1644},
    'RN' : {'AC': 4485, 'AL': 695, 'AP': 2524, 'AM': 4756, 'BA': 1185, 'CE': 533, 'DF': 2365, 'ES': 2305,   'GO': 2455, 'MA': 1482, 'MT': 3190, 'MS': 3073, 'MG': 2318, 'PA': 2504, 'PB': 185, 'PR': 3455, 'PE': 297, 'PI': 1104, 'RJ': 2570, 'RS': 4014, 'RO': 4201, 'RR': 5061, 'SC': 3640, 'SP': 2957, 'SE': 878, 'TO': 2198},
    'RS' : {'AC': 3892, 'AL': 3402, 'AP': 3797, 'AM': 4912, 'BA': 3087, 'CE': 4006, 'DF': 2015, 'ES': 1929, 'GO': 1821, 'MA': 3678, 'MT': 2267, 'MS': 1602, 'MG': 1711, 'PA': 3735, 'PB': 3785, 'PR': 711, 'PE': 3699, 'PI': 3676, 'RJ': 1555, 'RN': 4014, 'RO': 2713, 'RR': 4821, 'SC': 476, 'SP': 1113, 'SE': 3449, 'TO': 2225},
    'RO' : {'AC': 544, 'AL': 3929, 'AP': 3017, 'AM': 890, 'BA': 3630, 'CE': 4284, 'DF': 2.309, 'ES': 3275, 'GO': 2208, 'MA': 3468, 'MT': 1458, 'MS': 1837, 'MG': 2909, 'PA': 2891, 'PB': 3950, 'PR': 2615, 'PE': 3846, 'PI': 3180, 'RJ': 3048, 'RN': 4201, 'RS': 4024, 'RR': 1316, 'SC': 2812, 'SP': 3146, 'SE': 3808, 'TO': 1654},
    'RR' : {'AC': 2335, 'AL': 5309, 'AP': 1525, 'AM': 785, 'BA': 4869, 'CE': 4571, 'DF': 3987, 'ES': 4761, 'GO': 3758, 'MA': 3349, 'MT': 3144, 'MS': 3569, 'MG': 4515, 'PA': 2613, 'PB': 4811, 'PR': 4501, 'PE': 4707, 'PI': 3896, 'RJ': 4616, 'RN': 5061, 'RS': 5080, 'RO': 1316, 'SC': 4698, 'SP': 4570, 'SE': 5065, 'TO': 3126},
    'SC' : {'AC': 3486, 'AL': 2917, 'AP': 3435, 'AM': 4459, 'BA': 2832, 'CE': 3744, 'DF': 1673, 'ES': 1644, 'GO': 1626, 'MA': 3472, 'MT': 1778, 'MS': 1293, 'MG': 1309, 'PA': 3394, 'PB': 3412, 'PR': 300, 'PE': 3344, 'PI': 3337, 'RJ': 1122, 'RN': 3640, 'RS': 476, 'RO': 2812, 'RR': 4698, 'SP': 705, 'SE': 2991, 'TO': 2079},
    'SP' : {'AC': 3451, 'AL': 2153, 'AP': 2924, 'AM': 3944, 'BA': 1960, 'CE': 2684, 'DF': 1015, 'ES': 882, 'GO': 926, 'MA': 2823, 'MT': 1605, 'MS': 1014,'MG': 586, 'PA': 2937, 'PB': 2733, 'PR': 408, 'PE': 2669, 'PI': 2484, 'RJ': 434, 'RN': 2957,'RS': 1113, 'RO': 3146, 'RR': 4570, 'SC': 705, 'SP':0, 'SE': 2087, 'TO': 1635},
    'SE' : {'AC': 4072, 'AL': 294, 'AP': 2351, 'AM': 4598, 'BA': 356, 'CE': 1162, 'DF': 1658, 'ES': 1123, 'GO': 1832, 'MA': 1760, 'MT': 2662, 'MS': 2552, 'MG': 1315, 'PA': 2322, 'PB': 645, 'PR': 2774, 'PE': 501, 'PI': 1344, 'RJ': 1868, 'RN': 878, 'RS': 3449, 'RO': 3808, 'RR': 5065, 'SC': 2991, 'SP': 2166, 'TO': 1624},
    'TO' : {'AC': 1487, 'AL': 1746, 'AP': 1504, 'AM': 2695, 'BA': 1467, 'CE': 1595, 'DF': 874, 'ES': 1754, 'GO': 874, 'MA': 1452, 'MT': 1289, 'MS': 1589, 'MG': 1486, 'PA': 1286, 'PB': 2047, 'PR': 1908, 'PE': 1947, 'PI': 1029, 'RJ': 1644, 'RN': 2198, 'RS': 2225, 'RO': 1654, 'RR': 3126, 'SC': 2079, 'SP': 1786, 'SE': 1624, 'DF': 874},
    'DF' : {'AC': 3115, 'AL': 1729, 'AP': 2073, 'AM': 3495, 'BA': 1446, 'CE': 2206, 'ES': 1232, 'GO': 209, 'MA': 2115, 'MT': 1132, 'MS': 1134, 'MG': 716, 'PA': 2116, 'PB': 2220, 'PR': 1366, 'PE': 2120, 'PI': 1783, 'RJ': 1169, 'RN': 2365, 'RS': 2015, 'RO': 2309, 'RR': 3987, 'SC': 1673, 'SP': 1015, 'SE': 1658, 'TO': 874}
}

inicio = 'SP'
destino = 'BA'
distancias, caminho_mais_curto = dijkstra(grafo, inicio, destino)
print(f"Distância mais curta de {inicio} para {destino}: {distancias[destino]}")
print(f"Caminho mais curto: {caminho_mais_curto}")