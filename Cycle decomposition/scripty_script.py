import numpy as np
import networkx as nx
import random
import math

import matplotlib.pyplot as plt
import numpy as np

# n = 100
# N = 10000
# start_v = np.zeros(n)
# start_v[0] = 1
# for k in np.arange(1,N):
#     for i in np.arange(n-1,0,-1):
#         if(i!=0): start_v[i] += start_v[i-1]*(1.0/k)
#
#
# print(start_v)
# for i in range(n):
#     if(start_v[i]<1):
#         print(i)
#         break
#22

''' xi,j = xi,j-1 - xi,j-1 / n (lost) + 2 * xi-1,j-1 (new) '''

n = 55
N = 2**20
start_v = np.zeros(n) # 0 - old
end_v = np.zeros(n) # 1 - new
start_v[0] = 1
# print(start_v)
D = 2
for k in np.arange(1,N,D-1): # number of leaves
    for i in np.arange(0,n):
        end_v[i] = start_v[i] - (float(start_v[i])/float(k)) + float(D) * float(start_v[i-1]) / float(k)
        # print((start_v[i]/float(i)))
    for i in np.arange(n):
        start_v[i] = end_v[i]

print(end_v)
printed_final = False
printed_sum = False

for i in np.arange(n):
    is_final = True
    s = 0
    for j in range(i,n):
        s += end_v[j]
        if(end_v[j]>1):
            is_final = False
            break

    if is_final and not printed_final:
        printed_final = True
        print("final - " + str(i))
        print("s - " + str(s))

    if s < 1 and not printed_sum:
        printed_sum = True
        print("sum - " + str(i))

max = 0
avg = 0
m_i = 0
for i in np.arange(n):
    avg += end_v[i] * i
    if end_v[i] > max:
        max = end_v[i]
        m_i = i
print("max - " + str(max) +", at level - " + str(m_i))
print("avg - " + str(avg/N))


total_leaves = 0
for i in np.arange(n):
    total_leaves+=end_v[i]
print("total - " + str(total_leaves))

x = range(n)
y = end_v
plt.plot(y)
plt.show()

#plot all data
# plt.subplots_adjust(hspace=0.5)
# plt.subplot(311)
# plt.plot(x_values, y_values,'ko')
plt.title('All values')
plt.subplot(312)
plt.plot(x, y,'ko')
plt.title('Plot without masked values')
ax.set_xlim(x_values[0], x_values[-1])

ax = plt.subplot(313)
ax.plot(x_values, y_values_masked,'ko')
