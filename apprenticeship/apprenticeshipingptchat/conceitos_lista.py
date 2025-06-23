nomes = ["Thayla", "Henrique", "Eterno"]

print(nomes[0])            # Thayla
print(len(nomes))          # 3
nomes.append("Amor")       # Adiciona no fim
nomes.remove("Henrique")   # remove
nomes[1] = "Thayla"        # atualiza position

# Usar for com lista

for nome in nomes:
    print(f"Olá, {nome}")