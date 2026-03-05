numeros = []
qnt = int(input("""Digite quantos números quer somar: """))

if qnt == 0:
    print(" NÚMERO INVÁLIDO PROGRAMA ENCERRADO")

for i in range(qnt):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

    total = sum(numeros)

print(f"A soma dos números é = {total}")
            
    




   
    
   


