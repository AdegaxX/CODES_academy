'''k = ['grande', ['pequeno',10]]
print(k)

def quadrado(n):
    result = n ** 2
    return result
m = float(input('Digite um valor: '))
print('A raiz quadrada de M é: ', quadrado(m))
'''
lower = float(input('Num esquerda: '))
upper = float(input('Num direita: '))

def displayRange(lower, upper):
    if lower < upper:
        return 0
    else:
        return lower/upper
t = displayRange(lower, upper)
print(t)