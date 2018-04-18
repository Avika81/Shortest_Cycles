import snap
import sys

""" Examples for snap : """
v = snap.TIntV()

v.Add(1)
v.Add(21)
v.Add(321)

print v[1]

for item in v:
    print item

print "now hashes!"
h = snap.TIntStrH()

h[5] = "five"

h[3] = "three"

print h.Len()
print h[3]

print "now pairs"

p = snap.TIntStrPr(1, "one")
#first value: (int)
print p.GetVal1()
#second value: (string)
print p.GetVal2()


"""Graphs!!!!"""
print "and now Graphs"
G1 = snap.TUNGraph.New()  # undrected graphs
G2 = snap.TNGraph.New()   # directed graphs
N1 = snap.TNEANet.New()   # directed multigraph (won't be used prob)

# G1.AddNode(1)  # adds node with value 1 (not always 1 to n can be changed)
# G1.AddNode(5)
for i in range (100):
    G1.AddNode(i)

print G1.IsEdge(1,5)   # true if there is an edge from 1 to 5

G2 = snap.GenRndGnm(snap.PUNGraph, 100, 500)  # generates random graph (type, num odes, num edges)

G1.GetRndNId()  # returns random int id from the graph
G1.GetRndNI()   # returns node iterator starts from random location

# G1.Dump(OutF=sys.stdout)  # print the graph noramlly

for NI in G2.Nodes():
     for Id in NI.GetOutEdges():  # all the id's it can reach with an edge
         print "edge (%d %d)" % (NI.GetId(), Id)
