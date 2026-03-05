saldo = 1000
saque = float(input("Valor de saque: R$ "))

while saque > saldo:
    print("SALDO INSUFICIENTE")
    saque = float(input("Digite outro valor: R$"))

else:
    saldo = saldo - saque
    print(f'SAQUE REALIZADO COM SUCESSO\n VALOR RESTANTE: R${saldo:.2f}')
   

    
        


 