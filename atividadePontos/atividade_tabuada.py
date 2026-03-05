numero = int(input("Digite o número que deseja multiplicar: "))

print(f'TABUADA DO NÚMERO {numero}')
for i in range(1,11):
    multi = numero * i
    total = multi
    print(f'{numero} X {i} = {total}')