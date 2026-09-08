# Representação das entregas utilizando um grafo

grafo = {
    "Restaurante": ["Cliente 1", "Cliente 2"],
    "Cliente 1": ["Cliente 3"],
    "Cliente 2": ["Cliente 3"],
    "Cliente 3": []
}

print("Grafo de rotas criado com sucesso!")
print(grafo)
