# Questão 1:
# b)
def cal_quadrado():
    list = int(input('Até qual valor deseja elevar ao quadrado? '))
    contador = 0
    for i in range(1, list + 1):
        contador += i ** 2
    soma = (list * (list + 1)) * (2 * (list + 1))
    div = soma / 6
    print('A fórmula da soma dos quadrados é: S = (n * (n+1) * (2n+1)) / 6')
    print(f'S = ({list} * ({list}+1) * (2*({list}+1)) / 6')
    print(f'S = {soma} / 6')
    print(f'S = {div}')
    print(f'A soma dos quadrados até o {list} é igual à {contador}')
    return 'Fim'
print(cal_quadrado())
