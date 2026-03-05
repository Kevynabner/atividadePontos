email = []

while "@" not in email:
    login = input("Digite seu e-mail: ")
    email.append(login)
    print(f'e-mail digitado = {email[-1]}')


