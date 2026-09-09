import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# Localiza o arquivo CSV
caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_dados = os.path.join(
    caminho_atual,
    "..",
    "data",
    "entregas.csv"
)

# Lê os dados
dados = pd.read_csv(caminho_dados)

# Seleciona as coordenadas
coordenadas = dados[["latitude", "longitude"]]

# Cria os clusters
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

dados["cluster"] = kmeans.fit_predict(coordenadas)

# Cria o gráfico
plt.figure(figsize=(8, 6))

for cluster in sorted(dados["cluster"].unique()):
    grupo = dados[dados["cluster"] == cluster]

    plt.scatter(
        grupo["longitude"],
        grupo["latitude"],
        label=f"Cluster {cluster}"
    )

# Adiciona os nomes das regiões
for _, entrega in dados.iterrows():
    plt.annotate(
        entrega["localizacao"],
        (entrega["longitude"], entrega["latitude"])
    )

plt.title("Agrupamento de Entregas com K-Means")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend()
plt.grid()

# Caminho para salvar a imagem
caminho_saida = os.path.join(
    caminho_atual,
    "..",
    "outputs",
    "clusters.png"
)

plt.savefig(caminho_saida, dpi=300, bbox_inches="tight")

print("📊 Gráfico criado com sucesso!")
print(f"Imagem salva em: {caminho_saida}")

plt.show()