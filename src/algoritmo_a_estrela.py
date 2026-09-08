# Simulação simples do algoritmo A* para encontrar uma rota

rotas = {
    "Restaurante": ["Cliente 1", "Cliente 2"],
    "Cliente 1": ["Cliente 3"],
    "Cliente 2": ["Cliente 3"],
    "Cliente 3": []
}

inicio = "Restaurante"
destino = "Cliente 3"

print("Algoritmo A* iniciado!")
print(f"Ponto de partida: {inicio}")
print(f"Destino: {destino}")

# Rota simulada encontrada
rota_encontrada = ["Restaurante", "Cliente 1", "Cliente 3"]

print("Melhor rota encontrada:")
print(" → ".join(rota_encontrada))
