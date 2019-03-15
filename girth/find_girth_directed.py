import networkx
import numpy
import Dijkstra_algorithm

'''
The algorithm:
    for each vertex, find the best girth running through him, the remove it and continue.
'''


def find_girth(graph):
    best_res_yet = float('inf')
    distances = dict(networkx.algorithms.shortest_paths.weighted.all_pairs_dijkstra_path_length(graph))

    for i in range(graph.number_of_nodes()):
        for j in list(graph.predecessors(i)):
            if j is not i:
                w = distances[i][j]
                best_res_yet = min(w + graph[j][i]['weight'], best_res_yet)
    return best_res_yet
