# Lista de valores x
lista_x = [10, 100, 1000]

# Função para calcular y = x^3 - x^2
def calcular_y(x):
    return x**3 - x**2  # Realiza a subtração do cubo pelo quadrado dos valores a serem estabelecidos

# Calcular e imprimir os valores de y para cada x
for x in lista_x:
    y = calcular_y(x)   # irá fazer o cálculo com cada elemento da lista 'lista_x'
    print(f'Para x = {x}, y = {y}')     # print de cada um dos resultados
