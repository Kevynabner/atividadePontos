cliente = {}

cliente['NOME'] = input("Digite seu nome: ")
cliente['IDADE'] = int(input("Digite a sua idade: "))
cliente['CIDADE'] = input("Digite a sua cidade: ")
cliente['TELEFONE'] = int(input("Digite o seu telefone: "))

print("____INFORMAÇÕES DO CLIENTE_____")
for chave, valor in cliente.items():
    print(f'{chave}: {valor}')