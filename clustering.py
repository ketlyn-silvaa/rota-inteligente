import pandas as pd
from sklearn.cluster import KMeans
import os


def executar_clustering():
    # Localiza o arquivo entregas.csv
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_dados = os.path.join(
        caminho_atual,
        "..",
        "data",
        "entregas.csv"
    )

    # Lê os dados
    dados = pd.read_csv(caminho_dados)

    # Seleciona latitude e longitude
    coordenadas = dados[["latitude", "longitude"]]

    # Cria 3 grupos
    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    # Executa o agrupamento
    dados["cluster"] = kmeans.fit_predict(coordenadas)

    print("\n📍 Entregas agrupadas:")

    for _, entrega in dados.iterrows():
        print(
            f"📍 {entrega['localizacao']} "
            f"→ Cluster {entrega['cluster']}"
        )

    print("\n📊 Quantidade de entregas por cluster:")
    print(dados["cluster"].value_counts().sort_index())

    return dados