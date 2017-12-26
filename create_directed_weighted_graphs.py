import networkx
import random

def create_graph(num_vertices, p, min_weight, max_weight):
    graph = networkx.Graph()
    for i in range(num_vertices):
        graph.add_node(i)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if random.random() < p:
                # in probability p adds an edge :
                w = random.randint(min_weight, max_weight)
                graph.add_edge(i, j, weight=w)

