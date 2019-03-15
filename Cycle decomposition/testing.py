import try_a_random_graph
import sys
sys.path.append(sys.path[0] + "/..")

import pulp
from subprocess import call
from multiprocessing import Process

folder_of_tests = '/home/avi_kadria/Desktop/t/tests'

GNP_name = folder_of_tests + '/gnp_'
random_reg_name = folder_of_tests + '/reg_'


def f(i,b, R):
	global GNP_name
	global random_reg_name
	if(b == 0):
		default_name = GNP_name
	else:
		default_name = random_reg_name
	default_name += "max_" + str(R) + "_"

	new_file_name = default_name
	new_file_name += str(i)
	new_file_name += ".txt"
	new_file = open(new_file_name, "w")
	sys.stdout = new_file
	try_a_random_graph.try_a_random_graph(b, R)

all = range(1,6)

for i in all:
	p_0_30 = Process(target=f,args=(str(i),0, 30))
	p_0_30.start()
	p_1_30 = Process(target=f,args=(str(i),1, 30))
	p_1_30.start()

	p_0_40 = Process(target=f,args=(str(i),0, 40))
	p_0_40.start()
	p_1_40 = Process(target=f,args=(str(i),1, 40))
	p_1_40.start()
