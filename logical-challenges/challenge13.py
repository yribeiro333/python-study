nome = input("Nome do aluno: ")
notas = []

for i in range(1, 4):
    nota = float(input(f"Digite a nota {i}:"))
    notas.append(nota)
    
media = sum(notas) / len(notas)

if media >= 7:
    print(f'{nome} teve média {media:.1f} e foi aprovado!')
else:
    print(f'{nome} teve média {media:.1f} e foi reprovado!')
    
print(notas, nome)