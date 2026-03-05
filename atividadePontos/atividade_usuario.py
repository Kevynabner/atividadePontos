usuarios =  []

while "sair" not in usuarios:
    print("--CADASTRAR USUÁRIO = (NOME)")
    usuarios.append(input(f'--ENCERRAR = (SAIR)\n\nDIGITE SEU NOME|SAIR: ').lower())
else :
    while "sair" in usuarios:
        usuarios.pop(-1)
        print("PROGRAMA ENCERRADO")
        print(usuarios)
        break 

