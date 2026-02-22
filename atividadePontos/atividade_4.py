#cria uma tupla
empresa = ()
#transforma a tupla em uma lista
dados = list(empresa)

#recebe as informações do usuário
dados.append(input("Digite o nome da empresa: "))
dados.append(int(input("Digite o CNPJ: ")))
dados.append(input("Digite a cidade: "))

#converte a lista para uma tupla
empresa = tuple(dados)
#imprime a tupla completa sem tratamento
print(empresa)
#imprime a tupla com tratamento
print("_____INFORMAÇÕES DA EMPRESA______\n")
print(f'EMPRESA: {empresa[0]}\nCNPJ: {empresa[1]}\nCIDADE: {empresa[2]}\n')
print("_____NOME DA EMPRESA_____\n")
print(f'{empresa[0]}\n')
print("_____CIDADE_____\n")
print(f'{empresa[2]}')