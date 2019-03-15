import networkx
import numpy

'''
G = weighted graph
S = subset of vertices from G
r = number greater than 0
'''
def cluster_out(G,S,r):
    n = G.number_of_nodes()
    betta = log(n)/float(r)
    clusters = []
    x = numpy.zeros(n)  # ??
    for v in S:
        x[v] = numpy.random.exponential(betta)
        clusters.
    for u in G.nodes():
