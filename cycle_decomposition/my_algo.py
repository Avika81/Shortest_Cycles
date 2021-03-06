import networkx as nx
import math
import numpy as np

''' find the height of a specific graphs : '''
def k(e):
    return float(e[2])

def clean_small_degree_nodes(G):
    ''' remove all the nodes from the graph of degree less than 6. O(n) '''
    l_n = list(G.nodes()).copy()
    for n in l_n:
        if(G.degree[n] < 6):
            G.remove_node(n)

def my_algo(m_g, R):
    cnt_bad = 0  # counts the number of bad cycles found
    cnt_bad_edges = 0 # counts the number of bad edges in cycles 
    clean_small_degree_nodes(m_g)

    n = m_g.number_of_nodes()
    for e in m_g.edges():
        m_g[e[0]][e[1]]['weight'] = np.random.uniform()

    #print(sorted(T.edges(data=True)))
    T = nx.Graph()
    result = []
    for i in np.arange(n/math.log(n)):
        if len(m_g.edges()) < 3*n:
            print(str(2) + "n is " + str(n))
            break

        if(i!=0):
            o_edges = list(T.edges(data='weight'))
            for e in o_edges:
                m_g.add_edge(e[0],e[1])
                m_g[e[0]][e[1]]['weight'] = e[2]

            clean_small_degree_nodes(m_g)

        T = nx.minimum_spanning_tree(m_g)
        m_g.remove_edges_from(T.edges)

        l_e = m_g.edges(data='weight')
        e = min(l_e,key=k)

        p = nx.astar_path(T,e[0],e[1])
        l_p = [[p[i-1],p[i]] for i in range(1,len(p))]
        if(len(p) < R):
            result.append(p)
            T.remove_edges_from(l_p)
            m_g.remove_edge(e[0],e[1])
        else:
            cnt_bad +=1
            cnt_bad_edges += len(p)
            for d in l_p:
                T[d[0]][d[1]]['weight'] = np.random.uniform() + 1
            # m_g[e_min[0]][e_min[1]]['weight'] = np.random.uniform() + 1
        # print("the length of the added cycle is " + str(len(p)))
    # print(result)
    return (result,(cnt_bad, cnt_bad_edges))

def run_test(test):
    (result,(cnt_bad, cnt_bad_edges)) = my_algo(test.G, test.R)
    result.sort(key=len)
    if(result == []):
        print("no cycle found :( ")
        return
    print("The max len is: " + str(len(max(result,key=len))))
    # print("Average cycle size is: " + str(sum([len(i) for i in result])/len(result)))
    print("The average len (of an edge) is: " + str(sum([len(i)**2 for i in result])/sum([len(i) for i in result])))
    print("number of bad cycles = " + str(cnt_bad))
    print("number of bad edges = " + str(cnt_bad_edges))

    print("number of cycles found = " + str(len(result)))

    print("cycles length - " + str([len(i) for i in result]))
    print("The cycles - " + str(result))
