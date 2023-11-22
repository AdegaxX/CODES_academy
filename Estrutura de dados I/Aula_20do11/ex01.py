import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
def bfs(G, s):
    P = {}
    for v in G.nodes():
        G.nodes[v]['color'] = 'white'
        G.nodes[v]['lambda'] = float('inf')
        G.nodes[s]['color'] = 'gray'
        G.nodes[s]['lambda'] = 0
        Q = deque()
        Q.append(s)
        while (len(Q)> 0):
            u = Q.popleft()
            for v in G.neighbors(u):
                if (G.nodes[v]['color'] == 'white'):
                G.nodes[v]['lambda'] = G.nodes[u]['lambda'] + 1
                