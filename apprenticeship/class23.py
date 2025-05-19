# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7
#  H e n r i q u e
# -8-7-6-5-4-3-2-1

# nome = 'Henrique'
# print(nome[2])
# print(nome[-2])

# print('H' in nome)
# print('T' in nome)
# print(10 * '-')
# print('rique' not in nome)
# print('oque' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')