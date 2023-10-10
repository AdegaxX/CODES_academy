# Questão 1:
# a)
def cal_quadrado():
    list = int(input('Até qual valor deseja elevar ao quadrado? '))
    contador = 0
    for i in range(1, list + 1):
        contador += i ** 2
    print(f'A soma dos quadrados até o {list} é igual à {contador}')
    return 'Fim'
print(cal_quadrado())