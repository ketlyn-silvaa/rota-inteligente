import heapq
from grafo import grafo


def heuristica(atual, destino):
    """
    Heurística simples.
    Neste projeto, utilizamos valores estimados para orientar a busca.
    """
    
    estimativas = {
        "Restaurante": 10,
        "Centro": 8,
        "Liberdade": 7,
        "Bela Vista": 6,
        "Consolacao": 6,
        "Vila Mariana": 4,
        "Moema": 2,
        "Pinheiros": 4,
        "Perdizes": 0
    }

    return estimativas.get(atual, 0)


def algoritmo_a_estrela(inicio, destino):
    fila = []
    
    heapq.heappush(fila, (0, inicio))

    custo = {
        inicio: 0
    }

    caminho_anterior = {
        inicio: None
    }

    while fila:

        _, atual = heapq.heappop(fila)

        # Quando chegar ao destino
        if atual == destino:

            rota = []

            while atual is not None:
                rota.append(atual)
                atual = caminho_anterior[atual]

            rota.reverse()

            return rota, custo[destino]

        # Analisa os vizinhos
        for vizinho, distancia in grafo[atual].items():

            novo_custo = custo[atual] + distancia

            if vizinho not in custo or novo_custo < custo[vizinho]:

                custo[vizinho] = novo_custo

                prioridade = novo_custo + heuristica(
                    vizinho,
                    destino
                )

                heapq.heappush(
                    fila,
                    (prioridade, vizinho)
                )

                caminho_anterior[vizinho] = atual

    return None, None


print("⭐ Algoritmo A* carregado com sucesso!")
