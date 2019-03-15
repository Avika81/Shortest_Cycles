import snap
import numpy
import queue
import random
import math


def find_shortest_cycle(Graph):
    best = [float("nan"), -1]
    for node in Graph.Nodes():
        is_seen = numpy.zeros(Graph.GetNodes())
        is_seen[node.GetId()] = 1
        node.GetOutEdges()
        distance = 0
        vert_queue = []
        vert_queue.append([node, node])
        # print "start node: " + str(node.GetId())
        while len(vert_queue) > 0:
            # print "going on: " + str(vert_queue[0])
            distance += 1
            current = vert_queue.pop(0)
            curr_vertex = current[0]
            for neighbor in curr_vertex.GetOutEdges():
                if neighbor == current[1].GetId():
                    continue
                # print "neighbor :" + str(neighbor)
                if is_seen[neighbor] == 0:
                    is_seen[neighbor] = distance
                    vert_queue.append([Graph.GetNI(neighbor), curr_vertex])
                elif is_seen[neighbor]:  # distance > 2 because we don't want x->y->x cycles
                    result = [distance + is_seen[neighbor], neighbor]
                    if result[0] < best[0] or math.isnan(best[0]):
                        best = result
    if math.isnan(best[0]):
        print("There is no cycle in this graph!")
        return -1
    else:
        print("length : " + str(best[0]) + "\tstart : " + str(best[1]))
        return best[0]

def create_random_graph(num_vertices, p):
    # generates the empty graph with n vertices:
    Graph = snap.TUNGraph.New()
    for i in range(num_vertices):
        Graph.AddNode(i)

    for i in range(num_vertices):
        for j in range(i, num_vertices):
            if random.random() < p:
                Graph.AddEdge(i, j)
    print("num_vertices = " + str(num_vertices) + "\tp = " + str(p) + "\tnumber of edges = " + str(Graph.GetEdges()) + "\tEstimate was : " + str((num_vertices*(num_vertices-1)/2*p)))

    #Graph.Dump()
    return Graph

Max = 0
power_max = -1
for i in range(100):
    num_vertices = 1000
    for power in numpy.arange(0.8, 1, 0.001):
        print("m =  n ^ " + str(power))
        print("num vertices = " + str(num_vertices))
        # TempGraph = snap.GenRndGnm(snap.PUNGraph, num_vertices, int(num_vertices**power))  # generates random graph (type, num odes, num edges
        TempGraph = create_random_graph(num_vertices, (num_vertices**power)/(2* num_vertices * (num_vertices - 1))
        girth = find_shortest_cycle(TempGraph)
        if girth > Max:
            power_max = power
            Max = girth
        print("---------------------------------------------------------------------------------------------")    # delimiter
print("maximum length :" + str(Max) + "with power" + str(power))
# TempGraph.Dump()
