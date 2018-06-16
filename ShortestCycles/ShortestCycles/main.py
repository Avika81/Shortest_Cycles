import approximating_girth
import find_girth_directed
import create_directed_weighted_graphs
n = 100  # more will get very slow on both
number_of_test = 100
for i in range(number_of_tests):
    p = random.random()
    G = create_directed_weighted_graphs.create_graph(next,p,10,10000)
    print("exact = " + find_girth_directed.find_shortest_cycle(G) + "approx = " + approximating_girth.approximate_girth(G))