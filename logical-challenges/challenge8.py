password = "1234"
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    entrada = input('Digite a senha:')
    
    if entrada == password:
        print("Acesso liberado")
        break
    else:
        tentativas += 1
        restantes = limite_tentativas - tentativas
        if restantes > 0:
            print(f"Senha incorreta. Tentativas restantes: {restantes}")       
        else:
            print("Acesso bloqueado")