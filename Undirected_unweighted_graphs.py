import snap
import numpy
import queue
import random


def find_shortest_cycle(Graph):
    best = [999999999999999999999999999999, -1]
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
                    if result[0] < best[0]:
                        best = result
    print "length :" + str(best[0]) + "\tstart :" + str(best[1])


def create_random_graph(num_vertices, p):
    print "started the random graph"
    # generates the empty graph with n vertices:
    Graph = snap.TUNGraph.New()
    for i in range(num_vertices):
        Graph.AddNode(i)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if random.random() < p:
                Graph.AddEdge(i, j)
    print "finished creating the random graph!:"
    print "p = " + str(p) + "\tnumber of edges = " + str(Graph.GetEdges()) + "\tEstimate was : " + str((num_vertices**2)/p)

    #Graph.Dump()
    return Graph

TempGraph = create_random_graph(100, 0.01)
# TempGraph = snap.GenRndGnm(snap.PUNGraph, 100, 100)  # generates random graph (type, num odes, num edges

find_shortest_cycle(TempGraph)
# TempGraph.Dump()
