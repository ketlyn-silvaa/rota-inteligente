# Representação do mapa utilizando um grafo

grafo = {
    "Restaurante": {
        "Centro": 2,
        "Bela Vista": 3
    },

    "Centro": {
        "Restaurante": 2,
        "Liberdade": 2,
        "Consolacao": 3
    },

    "Liberdade": {
        "Centro": 2,
        "Vila Mariana": 4
    },

    "Bela Vista": {
        "Restaurante": 3,
        "Vila Mariana": 3,
        "Consolacao": 2
    },

    "Consolacao": {
        "Centro": 3,
        "Bela Vista": 2,
        "Pinheiros": 5
    },

    "Vila Mariana": {
        "Liberdade": 4,
        "Bela Vista": 3,
        "Moema": 4
    },

    "Moema": {
        "Vila Mariana": 4,
        "Pinheiros": 6
    },

    "Pinheiros": {
        "Consolacao": 5,
        "Moema": 6,
        "Perdizes": 4
    },

    "Perdizes": {
        "Pinheiros": 4
    }
}

print("🗺️ Grafo de rotas criado com sucesso!")
