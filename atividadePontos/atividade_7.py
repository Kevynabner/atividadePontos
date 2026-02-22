nome_preco = ()
informacao = list(nome_preco)
quantidade = {}
produtos = []

informacao.append(input("Digite o nome do produto: "))
informacao.append(float(input("Digite o preço do produto: R$ ")))
quantidade['Quantidade'] = input("Digite a quantidade: ")

nome_preco += tuple(informacao)
print("___NOME E PREÇO EM TUPLA___\n")
print(nome_preco)
print("__QUANTIDADE EM DICIONÁRIO__\n")
print(quantidade, "\n")

info_quantidade = quantidade

produtos.append((nome_preco, info_quantidade))

print("___TUDO EM UMA LISTA___\n")
print(produtos, "\n")
print("___PRODUTO___")
print(f'PRODUTO: {produtos[0][0][0]}')
print(f'PREÇO: {produtos[0][0][1]}')
print(f'QUANTIDADE: {produtos[0][1]['Quantidade']}')
