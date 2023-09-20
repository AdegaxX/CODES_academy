# Exemplo 1: lista indexada

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
r = int(input('Digite o tamanho do passo: '))

inicio = n1
fim = n2
passo = r

for i in range(inicio, fim, passo):
    print(i)