with open("/dados/chave.txt") as f:
    chave = f.read()

tamanho = len(chave)

possibilidades = 26 ** tamanho

print("===== ATAQUE DE FORÇA BRUTA =====")
print(f"Tamanho da chave: {tamanho}")
print(f"Possibilidades: {possibilidades:,}")