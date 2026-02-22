usuario = {}

usuario['NOME'] = input("Digite seu nome: ")
usuario['SENHA'] = input("Digite a sua senha: ")

print("____DADOS CADASTRADOS_____")
for chave, valor in usuario.items():
    print(f'{chave}: {valor}')  