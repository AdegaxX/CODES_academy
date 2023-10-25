import networkx as nx
import matplotlib as plt

# Cria gráfico vazio:
G = nx.Graph()

# Adiciona vértices:
G.add_node('v1')
G.add_node('v2')
G.add_node('v3')
G.add_node('v4')
G.add_node('v5')

# Adiciona arestas:
G.add_edge('v1','v2')
G.add_edge('v2','v3')
G.add_edge('v3','v4')
G.add_edge('v4','v5')
G.add_edge('v5','v1')
G.add_edge('v2','v4')

# Lista dos vértices:
print('Lista de vértices')
print(G.nodes())
#input()

# Percorre o conjunto de vértices:
print('Percorrendo os vértices')
for v in G.nodes():
    print(v)
#input()

# Percorre o conjunto de arestas:
print('Percorrendo as arestas')
for e in G.edges():
    print(e)
#input()

# Mostra a lista de graus:
print('Lista de graus de G')
print(G.degree())
#input()

# Acessa o grau do vértice v2:
print('O grau do vértice v2 é %d' %G.degree()['v2'])

# Grafo como lista de adjascência:
print('Grafo como lista de adjascência')
print(G['v1'])
print(G['v2'])
print(G['v3'])
print(G['v4'])
print(G['v5'])
#input()

# Matriz adjascente:
print('Matriz adjascente:')
A = nx.adj