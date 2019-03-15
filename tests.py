import create_directed_weighted_graphs
import Dijkstra_algorithm
import find_girth_directed

graph = create_directed_weighted_graphs.create_graph(100, 1/5, 10, 100)
distances = find_girth_directed.dijkstra(graph, 1)
print(distances[5])
