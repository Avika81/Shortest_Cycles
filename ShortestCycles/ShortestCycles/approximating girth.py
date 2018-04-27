import networkx
import numpy
import queue
from heapq import heappush, heappop
import create_directed_weighted_graphs

def BoundDijkstra(G,s,t):
    d = numpy.zeros(G.number_of_nodes() + 1)
    q = queue.PriorityQueue(G.number_of_nodes() + 1)

    #init:
    d[s] = 0
    for i in range(0,number_of_nodes):
        if i != s:
            d[i] = float("inf")
        q.put((d[i],i))  # tuple of (d(s,u),u)    
    while not q.empty():
        u = q.get()
        for v in G.neighbors(u[1]):
            alt = d[u] + G[u[1]][v]['weight']
            if alt<d[v]:
                d[v] = alt
    return d

G = create_directed_weighted_graphs.create_graph(20,1/20,5,20)

print(BoundDijkstra(G,0,t))