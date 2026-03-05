usuarios = []
qnt = 5

for i in range(qnt):
    login = input("Digite seu nome: ")
    usuarios.append(login)
    print(f'{login} CADASTRADO!\n')
print("USUARIOS")
for i in usuarios:
    print(i)
