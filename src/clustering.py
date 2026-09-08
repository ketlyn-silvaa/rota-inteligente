# Agrupamento de entregas por região

entregas = {
    "Zona Norte": ["Cliente 1", "Cliente 2"],
    "Zona Sul": ["Cliente 3"]
}

print("Agrupamento de entregas realizado com sucesso!")

for zona, clientes in entregas.items():
    print(f"{zona}: {clientes}")
