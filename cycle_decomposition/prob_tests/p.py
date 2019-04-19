import itertools
import copy
N = 10
permutations = itertools.permutations([i for i in range(N)])


def f_index(l):
    c = 10
    for i in range(N):
        l.append(0)
    return l[0]*c**2+l[1]*c+l[2]

permutations_t = []
for i in range(2**N):
    t_perm = []
    res = format(i,'#0' + str(N) +'b')

    for item in range(N):
        if res[N-1-item] == '1':
            t_perm.append(item)
    permutations_t.append(t_perm)
groups = []
for i in range(1,6):
    groups.append([i,i+1])

disct = {}
for p in permutations:
    p_l = list(p)
    to_continue = True
    groups_t = copy.deepcopy(groups)
    first_group = -1
    for i in p:
        if(to_continue):
            for index in range(len(groups)):
                if i in groups_t[index]:
                    groups_t[index].remove(i)
                    if(groups_t[index] == []):
                        # print("g is the first " + str(index + 1))
                        to_continue = False
                        first_group = index

    for item in groups[first_group]:
        # print(item, p_l)
        index = p_l.index(item)
        p_l.remove(item)
        '''trying to fix probability'''
        if(index < len(p_l) and p_l[index]not in groups[first_group]):
            p_l.remove(p_l[index])
    # print(p_l)

    permutations_tt = groups_t = copy.deepcopy(permutations_t)
    for pp in permutations_tt:
        t = True
        for i in p_l:
            if (i not in pp):
                t = False
        if t:
            cc = f_index(p_l)
            if cc not in disct:
                disct[f_index(p_l)] = 1
            else:
                disct[f_index(p_l)] += 1

print(disct)
    # print(p)
