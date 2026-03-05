senha = 1234

while True:
    acesso = int(input("Digite a sua senha: "))

    if acesso != senha:
        print("SENHA INCORRETA")
    else:   
        print("ACESSO LIBERADO")    