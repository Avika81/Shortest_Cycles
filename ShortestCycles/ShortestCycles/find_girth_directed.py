import snap
import numpy
import queue
import random
import math
import networkx

def find_shortest_cycle(Graph):
    """
    calculates the exact girth using apsp. 
    """
    m = float('inf')
    d = all_pairs_bellman_ford_path(Graph, cutoff=None, weight='weight')
    for e in Graph.Edges:
        m = min(m,e['weight'] + d[e.second] + d[e.first])
    return m