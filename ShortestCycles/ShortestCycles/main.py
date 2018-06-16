import approximating_girth
import find_girth_directed
import create_directed_weighted_graphs
n = 100

for i in range(number_of_tests):
    p = random.random()
    G = create_directed_weighted_graphs.create_graph(next,p,10,10000)