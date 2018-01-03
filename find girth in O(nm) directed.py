import networkx
import numpy
import random
import create_directed_weighted_graphs

def min_length(s,G):
    bucket = [[]] * networkx.number_of_nodes(G)  # array, set 1 value for each node representing the length from it to 1 in G'.
    d = numpy.array(networkx.number_of_nodes(G))  # array, set 1 value for each node representing the length from it to 1 in G'.
    d[s] = 0
    pred[s] = 0
    distance-update(s,s)
    is_there_non_empty_buckets = True
    while is_there_non_empty_buckets:
        k = '''min bucket that is not empty?'''
        j = bucket(k).pop()
        mldc = min(mldc,d(j) + G.get_edge_data(j,s))

def min_length_directed_cycle(G):
    min_length_directed_cycle,mean_of_cycle = weight_of_any_cycle(G)  # returns the total length and the mean.
    p = numpy.array(networkx.number_of_nodes(G))  # array, set 1 value for each node representing the length from it to 1 in G'.
    '''**set p values**'''
    '''update the values of the arcs'''
    for s in networkx.nodes(G):
        mldc = min(min_length(s,G),min_length_directed_cycle)

T = create_directed_weighted_graphs.create_graph(10,1,1,1)
min_length_directed_cycle(T)
