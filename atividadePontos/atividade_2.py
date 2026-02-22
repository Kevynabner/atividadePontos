#CRIA UM DICIONARIO
estoque = {}
#DEFINE A QUANTIDADE DE PRODUTOS QUE O CLIENTE VAI DIGITAR
qnt = 4
#LAÇO DE REPETIÇÃO QUE ALIMENTA O ESTOQUE
for i in range(qnt):
    nome = input("Digite o nome do produto: ")
    quantidade = float(input("Digite a quantidade em estoque: "))
    estoque[nome] = quantidade

#COLOCA O ESTOQUE DENTRO DE OUTRA VARIÁVEL, PARA TRATAR O ACESSO AS CHAVES DO DICIONARIO
produto = estoque

#IMPRIME A LISTA DE PRODUTOS
print("____LISTA DE PRODUTOS____\n")

for produto in estoque:
    
    print(f'Produto: {produto}\nQuantidade: {quantidade} - Unidades')
    print("_____________________\n")

#VARIAVEL PARA ACESSAR A PRIMEIRA CHAVE, VALOR DO DICIONARIO   
primeiro_produto = list(estoque.keys())[0]
primero_valor = estoque[primeiro_produto]
#VARIAVEL PARA ACESSAR A ULTIMA CHAVE, VALOR DO DICIONARIO
ultimo_produto = list(estoque.keys())[-1]
ultimo_valor = estoque[ultimo_produto]

#IMPRIME O PRIMEIRO PRODUTO
print("______PRIMEIRO PRODUTO________\n")
print(f'Produto: {primeiro_produto}\nQuantidade: {primero_valor} - Unidades\n')

#IMPRIME O ULTIMO PRODUTO
print("______ÚLTIMO PRODUTO________\n")
print(f'Produto: {ultimo_produto}\nQuantidade: {ultimo_valor} - Unidades\n')

#IMPRIME A QUANTIDADE DE PRODUTOS
quantidade_produtos = len(estoque)
print(f'Existe {quantidade_produtos} produtos no estoque')

    