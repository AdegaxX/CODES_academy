# Aula Programação Orientada a Objeto:
'''
def zera(x):
    for i in range(len(x)):
        x[i] = 0        # Zera a lista, tornando todos zeros

a = [1,2,3]
zera(a)
print(a)
'''

'''
def zera(x):
    x = [0] * len(x)

a = [1,2,3]
zera(a)
print(a)
'''

def imprime_linha(tamanho):
    print(':' * tamanho)

texto = 'PROGRAMAR É LEGAL'
imprime_linha(len(texto))
print(texto)
imprime_linha(len(texto))