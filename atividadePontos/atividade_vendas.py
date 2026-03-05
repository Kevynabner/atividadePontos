vendas = []

qnt = 4

for i in range(qnt):
    valor = (float(input("Digite um valor R$: ")))
    vendas.append(valor)
total = sum(vendas)
print(f'Você vendeu R${total}')