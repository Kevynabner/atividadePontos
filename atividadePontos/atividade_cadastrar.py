menu = int(input(f'_______MENU_______\n1 - CADASTRAR\n2- LISTAR\n3- SAIR\nDigite sua opção: '))
usuario = []

while menu == 1: 
    
    login = input("Digite seu Login: ")
    
    usuario.append(login)
    print(f'{usuario[-1]} cadastrado com sucesso'.upper())
    menu = int(input(f'_______MENU_______\n1 - CADASTRAR\n2- LISTAR\n3- SAIR\nDigite sua opção: '))    
while menu == 2:
    print(f'___USUÁRIOS___')
    for i in usuario:
        print(i)
    menu = int(input(f'_______MENU_______\n1 - CADASTRAR\n2- LISTAR\n3- SAIR\nDigite sua opção: '))
            
while menu == 3:
    if menu == 3:
        print("___PROGRAMA ENCERRADO___")  
        break      
                