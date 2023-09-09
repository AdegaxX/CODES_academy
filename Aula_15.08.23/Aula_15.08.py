
'''
x = int(input('Digite o valor de X: '))
y = int(input('Digite o valor de Y: '))
if x > y:
    print(x,'é maior que',y)
elif x < y:
    print('x é menor que y')
else:
    print('x é igual a y')
'''

'''
produto = 1
valor = 1
while valor <= 10:
    produto *= valor
    valor += 1
print(produto)
'''
'''
p1 = 'Universidade'[0] # retorna a primeira letra da palavra.
print(p1)

p2 = 'Universidade'[1:6] # retorna as letras 2 até a 6.
print(p2)
'''

for expoent in range(7,11):
    print('Contém',expoent,'zeros:', 10 ** expoent)
