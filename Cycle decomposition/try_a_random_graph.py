import networkx as nx
import math
import numpy as np

''' find the height of a specific graphs : '''
def k(e):
    return float(e[2])

def clean_small_degree_nodes(G):
    l_n = list(G.nodes()).copy()
    for n in l_n:
        if(G.degree[n] < 6):
            G.remove_node(n)

def my_algo(m_g, R):
    cnt_bad = 0
    clean_small_degree_nodes(m_g)

    n = m_g.number_of_nodes()
    for e in m_g.edges():
        m_g[e[0]][e[1]]['weight'] = np.random.uniform()

    #print(sorted(T.edges(data=True)))
    T = nx.Graph()
    result = []
    for i in np.arange(n/math.log(n)):
        if len(m_g.edges()) < 6*n:
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
            for d in l_p:
                T[d[0]][d[1]]['weight'] = np.random.uniform() + 1
            # m_g[e_min[0]][e_min[1]]['weight'] = np.random.uniform() + 1
        # print("the length of the added cycle is " + str(len(p)))
    # print(result)
    return (result,cnt_bad)

def try_a_random_graph(i, R):
    n = 1000
    d = 30
    # R = 30

    random_reg = nx.random_regular_graph(d,n)
    G_np = nx.gnp_random_graph(n,d/n)
    if(i == 0):
        (result,cnt_bad) = my_algo(G_np, R)
    else:
        (result,cnt_bad) = my_algo(G_np, R)
    print("The max len is: " + str(len(max(result,key=len))))
    # print("Average cycle size is: " + str(sum([len(i) for i in result])/len(result)))
    print("The average len (of an edge) is: " + str(sum([len(i)**2 for i in result])/sum([len(i) for i in result])))
    print("cnt_bad = " +str(cnt_bad))

    print("num_cycles = " + str(len(result)))

    print("result is - " + str([len(i) for i in result]))
    print("The cycles - " + str(result))
