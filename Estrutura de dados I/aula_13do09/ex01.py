# Cria uma pilha vazia:
pilha = list()
print('Pilha vazia: ', pilha)

# Insere elementos na pilha:
for i in range(5):
    pilha.insert(i, i)
    print(f'Insere o valor {i} no topo da pilha: {pilha}')

# Remove elementos da pilha:
while pilha:
    if not pilha:
        pass
    else:
        pilha.pop()
print('Removendo elemento que está no topo da lista: ',pilha)
