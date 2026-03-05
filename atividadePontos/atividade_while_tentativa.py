senha = 1234
tentativa = 3
while True:
    acesso = int(input("Digite sua senha: "))

    if acesso != senha and tentativa > 0: 
        print("SENHA INCORRETA, TENTE OUTRA VEZ ")
        tentativa = tentativa - 1
        print(f'Você tem mais {tentativa} chances!\n')
        if tentativa == 0:
            print(f'{tentativa} tentativas, CONTA BLOQUEADA')
            break    
    else:
        print("ACESSO LIBERADO")    



    

