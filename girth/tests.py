import create_directed_weighted_graphs
import Dijkstra_algorithm
import networkx
import find_girth_directed

# print ("dijekstra tests: ")
#
# graph = create_directed_weighted_graphs.create_graph(100, 1/5, 10, 100)
# distances = Dijkstra_algorithm.dijkstra(graph, 1)
#
# print(distances[5])
#
# print("networks tests:")
#
# graph = networkx.DiGraph()
# graph.add_node(0)
# graph.add_node(1)
# graph.add_node(2)
# graph.add_edge(0, 1, weight=0.5)
# print(graph[0])
# print(graph[1])
#
# print("files")
# open("x","w+")

print ("calculate girth")
graph = create_directed_weighted_graphs.create_graph(1000, 1/5, 10, 100)
# print(graph[5])
# it1 = graph.predecessors(5)
# it2 = graph.neighbors(5)
# print(list(it1))
# print(list(it2))

x = find_girth_directed.find_girth(graph)
print(x)
