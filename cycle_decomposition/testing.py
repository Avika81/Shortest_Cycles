import my_algo
import sys
sys.path.append(sys.path[0] + "/..")

import pulp
from subprocess import call
from multiprocessing import Process
import networkx as nx


folder_of_tests = '/home/avi_kadria/Desktop/Master/cycle_decomposition/tests'

GNP_name = folder_of_tests + '/gnp_'
random_reg_name = folder_of_tests + '/reg_'

class Test:
    G = -1
    type = ''
    R = -1

    N = -1
    d = -1

    def __init__(self, G, type, R, n, d):
        self.G = G
        self.type = type
        self.R = R

        self.N = n
        self.d = d

def f(t):
    global folder_of_tests
    default_name = folder_of_tests + '/' + t.type + '_'
    default_name += "n_" + str(t.N) + "_max_" + str(t.R) + ".txt"

    new_file_name = default_name
    new_file = open(new_file_name, "w")
    sys.stdout = new_file
    my_algo.run_test(t)



tests = []

def random_gnp_test(n,d,R):
    G_np = nx.gnp_random_graph(n,d/n)
    return Test(G_np, 'gnp', R, n, d)

def random_reg_test(n,d,R):
    random_reg = nx.random_regular_graph(d,n)
    return Test(random_reg, 'reg', R, n, d)

def get_football_graph_test():
    #from https://networkx.github.io/documentation/stable/auto_examples/graph/plot_football.html#sphx-glr-auto-examples-graph-plot-football-py
    try:  # Python 3.x
        import urllib.request as urllib
    except ImportError:  # Python 2.x
        import urllib
    import io
    import zipfile

    import matplotlib.pyplot as plt
    import networkx as nx

    url = "http://www-personal.umich.edu/~mejn/netdata/football.zip"

    sock = urllib.urlopen(url)  # open URL
    s = io.BytesIO(sock.read())  # read into BytesIO "file"
    sock.close()

    zf = zipfile.ZipFile(s)  # zipfile object
    txt = zf.read('football.txt').decode()  # read info file
    gml = zf.read('football.gml').decode()  # read gml data
    # throw away bogus first line with # from mejn files
    gml = gml.split('\n')[1:]
    G = nx.parse_gml(gml)  # parse gml data

    return Test(G, 'football', 10, G.number_of_nodes(), -1)

def get_lollipop_graph_test(n,m,R):
    G = nx.lollipop_graph(m,n)
    return Test(G, "lollipop", R, G.number_of_nodes(), -1)

def get_complete_graph_test(n, R):
    G = nx.complete_graph(n)
    return Test(G, "complete", R, G.number_of_nodes(), -1)

tests = []
'''already got results :
for i in range(1,6):
    tests.append(random_gnp_test(200*i,30,20))

for i in range(1,6):
    tests.append(random_reg_test(200*i,30,20))

tests.append(get_football_graph_test())

tests.append(get_lollipop_graph_test(100,200,20))
tests.append(get_lollipop_graph_test(100,200,15))
'''
tests.append(get_complete_graph_test(200,20))
tests.append(get_complete_graph_test(400,22))
tests.append(get_complete_graph_test(600,24))
tests.append(get_complete_graph_test(800,26))
tests.append(get_complete_graph_test(1000,28))
for t in tests:
    p = Process(target=f,args=(t, ))
    p.start()
