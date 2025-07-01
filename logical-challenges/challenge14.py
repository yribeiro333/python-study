quantidade = int(input("Quantos alunos deseja cadastrar: "))

for i in range(quantidade):
    nome = input("Nome do aluno: ")
    notas = []

resumo = []

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i}: "))  
    notas.append(nota)
        
media = sum(notas) / len(notas)

resumo.append((nome, media))

print("\nResumo final:")
for nome in resumo:
    print(f"{nome[0]}: média {nome[1]:.1f}")