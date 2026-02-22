produtos = []
preco = []

#DEFINE A QUANTIDADE DE PRODUTOS
qnt = 4
#LAÇO para pegar produto e valor de acordo com a quantidade
for i in range(qnt):
    produtos.append(input("Digite o nome do produto: "))
    preco.append(float(input("Digite o valor do produto R$")))
    
#RETORNA A LISTA DE PRODUTOS
print(f'__Lista de produtos__ ')
for i in produtos:
    print(i)

#RETORNA O PRIMEIRO PRODUTO E PRIMEIRO VALOR
print("PRIMEIRO PRODUTO E PRIMEIRO PREÇO \n ----------------")
for i in range(1):
    print(f'{produtos[0]} : R${preco[0]}\n ----------------')

#RETORNA O ULTIMO PRODUTO E ULTIMO VALOR
print("ULTIMO PRODUTO E ULTIMO PREÇO \n ----------------")
for i in range(1):
    print(f'{produtos[-1]} : R${preco[-1]}\n ----------------')

total = sum(preco)
print(f'O valor total da compra é de R${total}')

novoProduto = input("Deseja adicionar um novo produto? Digite o novo produto:  ")

produtos[0] = novoProduto 


for i in range(1):
    print(f'{produtos[0]} foi alterado com sucesso')
    #RETORNA A LISTA DE PRODUTOS
print(f'__Lista de produtos atualizada__ ')
for i in produtos:
    print(i)



