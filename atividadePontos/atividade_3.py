#cria uma tupla
conta = ()
#transforma a tupla em uma lista
dados = list(conta)

#recebe as informações do usuário
dados.append(float(input("Digite o numero da conta: ")))
dados.append(input("Digite o nome do cliente: "))
dados.append(float(input("Digite o saldo: R$ ")))

#converte a lista para uma tupla
conta = tuple(dados)
#imprime a tupla completa sem tratamento
print(conta)
#imprime a tupla com tratamento
print("_____INFORMAÇÕES DA CONTA______\n")
print(f'CONTA: {conta[0]}\nCLIENTE: {conta[1]}\nSALDO: R${conta[2]}\n')
print("_____NOME DO CLIENTE_____\n")
print(f'{conta[1]}\n')
print("_____SALDO_____\n")
print(f'R${conta[2]}')

