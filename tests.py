import create_directed_weighted_graphs
import Dijkstra_algorithm


graph = create_directed_weighted_graphs.create_graph(100, 1/5, 10, 100)
distances = Dijkstra_algorithm.dijkstra(graph, 1)
print(distances[5])
