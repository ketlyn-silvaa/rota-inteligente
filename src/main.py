# Projeto Rota Inteligente
# Arquivo principal do sistema

from algoritmo_a_estrela import algoritmo_a_estrela
from clustering import executar_clustering

print("🚚 PROJETO ROTA INTELIGENTE")
print("Sistema de otimização de rotas de entrega")
print("=" * 50)

# =====================================
# PARTE 1 - ALGORITMO A*
# =====================================

print("\n⭐ OTIMIZAÇÃO DE ROTA COM A*")

inicio = "Restaurante"
destino = "Perdizes"

print(f"\n📍 Ponto de partida: {inicio}")
print(f"🎯 Destino: {destino}")

rota, distancia = algoritmo_a_estrela(inicio, destino)

if rota:
    print("\n✅ Melhor rota encontrada:")
    print(" → ".join(rota))
    print(f"\n📏 Distância total: {distancia} km")
else:
    print("\n❌ Não foi possível encontrar uma rota.")

# =====================================
# PARTE 2 - K-MEANS
# =====================================

print("\n" + "=" * 50)
print("📦 AGRUPAMENTO DE ENTREGAS COM K-MEANS")
print("=" * 50)

executar_clustering()

print("\n🚚 Projeto executado com sucesso!")
