import networkx
from fibHeap import FibonacciHeap

"""https://gist.github.com/Agnishom/f9b59eaf9379353edaa9595066c80634"""


def dijkstra(graph, source, sink=None):
    n = graph.number_of_nodes()  # intentionally 1 more than the number of vertices, keep the 0th entry free for
    #  convenience
    visited = [False]*n
    distance = [float('inf')]*n

    heapNodes = [None]*n
    heap = FibonacciHeap()
    for i in range(n):
        heapNodes[i] = heap.insert(float('inf'), i)     # distance, label
    print("x1: " + str(heap.total_nodes))
    distance[source] = 0
    heap.decrease_key(heapNodes[source], 0)
    print("x2: " + str(heap.total_nodes))
    while heap.total_nodes:
        print("x3: " + str(heap.total_nodes))
        min = heap.extract_min()
        print("x4: " + str(heap.total_nodes))
        if min == None:
            print("x: " + str(heap.total_nodes))
            print("error, graph isn't connected (there is infinity distances)")
            break
        current = min.value
        visited[current] = True

        #early exit
        if sink and current == sink:
            break

        for neighbor in graph[current]:
            if not visited[neighbor]:
                cost = graph[current][neighbor]['weight']
                if distance[current] + cost < distance[neighbor]:
                    distance[neighbor] = distance[current] + cost
                    heap.decrease_key(heapNodes[neighbor], distance[neighbor])

    return distance
