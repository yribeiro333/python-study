password = "1234"
tentative = 0
limit_tentatives = 3

while tentative < limit_tentatives:
    input('Digite a senha:')
    
    if tentative == password:
        print("Acesso liberado")
        break
    else:
        tentative =+ 1
        restant = limit_tentatives - tentative
        if restant > 0:
            print(f"Senha incorreta. Tentativas restantes: {limit_tentatives - tentative}")
        
else:
        print("Acesso bloqueado")