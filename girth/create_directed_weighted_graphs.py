import networkx
import numpy
import random
dir_to_folder_of_graphs = "/media/avi_kadria/Windows/Users/avika/directed_weighted_graphs"
index = 1

def create_graph(num_vertices, p, min_weight, max_weight):
    global index
    graph = networkx.DiGraph()
    for i in range(num_vertices):
        graph.add_node(i)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if random.random() < p:
                # in probability p adds an edge :
                w = random.randint(min_weight, max_weight)
                graph.add_edge(i, j, weight=w)
    new_dir = dir_to_folder_of_graphs + "/" + "nodes_" + str(num_vertices) + "_edges_" \
            + str(graph.number_of_edges()) + "weight_" + str(min_weight) + "_" + str(max_weight)\
            + "_index_" + str(index)
    # open(new_dir, "w+")
    # networkx.write_gml(graph, new_dir)
    index += 1
    return graph


# for num_vertices in range(100, 1001, 100):  # 10
#     for power in numpy.arange(0.7, 1.3, 0.001):  # 6000
#         p = (num_vertices**power)/(num_vertices * (num_vertices-1))
#         for min_weight in range(0, 1001, 200):  # 5
#             for max_weight in range(min_weight + 400, min_weight + 2000, 400):  # 5
#                 create_graph(num_vertices, p, min_weight, max_weight)
#
# # big graphs:
# for num_vertices in range(1000, 10001, 1000):  # 10
#     for power in numpy.arange(0.9, 1.1, 0.01):  # 200
#         p = (num_vertices**power)/(num_vertices * (num_vertices-1))
#         for min_weight in range(10000, 100001, 10000):  # 10
#             for max_weight in range(min_weight, min_weight + 1000000, 100000):  # 11
#                 create_graph(num_vertices, p, min_weight, max_weight)
