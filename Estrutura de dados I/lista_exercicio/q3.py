# Lista de valores x
lista_x = [10, 100, 1000]

# Função para calcular y = x^3 - x^2
def calcular_y(x):
    return x**3 - x**2

# Calcular e imprimir os valores de y para cada x
for x in lista_x:
    y = calcular_y(x)
    print(f'Para x = {x}, y = {y}')
