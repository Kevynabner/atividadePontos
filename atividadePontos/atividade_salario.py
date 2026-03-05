salarios = []
qnt = 2

for i in range(qnt):
    valores = float(input("Digite o seu salário R$: "))
    salarios.append(valores)
    
print(f'****PARABÉNS VOCÊ RECEBEU 10% DE AUMENTO*****\n')
for i in salarios:
    porcentagem = i * 0.1
    print(f'SALÁRIO ANTIGO = {i} SALÁRIO ATUAL = {i + porcentagem}')
    
     
    



