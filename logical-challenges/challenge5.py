name = input('Qual seu nome: ')
age = int(input('Qual sua idade: '))

if age >= 100:
    print('Sério isso?!')
elif age >= 18:
    print(f'{name}, você é maior de idade.')
else:
    print(f'{name}, você é menor de idade e faltam {18 - age} ano(s) pra completar 18.')
