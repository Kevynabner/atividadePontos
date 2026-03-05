usuarios = []

online = 0
offline = 0
qnt = 4

for i in range(qnt):
    usuarios.append(input("(STATUS) = ON / OFF: ").lower())
  
for i in usuarios:
    if i == "on":
        online += 1
    else :
        offline += 1
            

print(f'{online} USUÁRIOS ONLINE')
print(f'{offline} USUÁRIOS OFFLINE')
 

    

