import os
import matplotlib.pyplot as plt
import networkx as nx
from grafo import grafo

# Cria o grafo
G = nx.Graph()

# Adiciona os nós e conexões
for origem, destinos in grafo.items():
    for destino, distancia in destinos.items():
        G.add_edge(origem, destino, weight=distancia)

# Define a organização visual do grafo
pos = nx.spring_layout(G, seed=42)

# Cria a imagem
plt.figure(figsize=(10, 7))

# Desenha os nós
nx.draw_networkx_nodes(
    G,
    pos,
    node_size=2000
)

# Desenha as conexões
nx.draw_networkx_edges(
    G,
    pos,
    width=2
)

# Adiciona os nomes dos locais
nx.draw_networkx_labels(
    G,
    pos,
    font_size=10
)

# Mostra as distâncias nas conexões
pesos = nx.get_edge_attributes(G, "weight")

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=pesos,
    font_size=9
)

plt.title("Mapa de Rotas - Projeto Rota Inteligente")
plt.axis("off")

# Define o caminho para salvar
caminho_atual = os.path.dirname(os.path.abspath(__file__))

caminho_saida = os.path.join(
    caminho_atual,
    "..",
    "outputs",
    "grafo_rotas.png"
)

# Salva a imagem
plt.savefig(
    caminho_saida,
    dpi=300,
    bbox_inches="tight"
)

print("🗺️ Grafo criado com sucesso!")
print(f"Imagem salva em: {caminho_saida}")

plt.show()