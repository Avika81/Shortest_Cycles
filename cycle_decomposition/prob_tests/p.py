import itertools
import copy
permutations = itertools.permutations([1,2,3,4,5])


def f_index(l):
    c = 10
    return l[0]*c**2+l[1]*c+l[2]
permutations_t = itertools.permutations([2,3,4,5])
groups = []
# for i in range(1,5):
#     groups.append([i,i+1,i+2])
for i in range(1,3):
    groups.append([i])

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
    for i in groups[first_group]:
        p_l.remove(i)
    # print(p_l)

    permutations_tt = groups_t = copy.deepcopy(permutations_t)
    for pp in permutations_tt:
        # print(pp)
        t = True
        for i in p_l:
            if (i not in pp):
                # print(i)
                t = False
        if t:
            # print(1)
            cc = f_index(p_l)
            if cc not in disct:
                # print(f_index(p_l))
                disct[f_index(p_l)] = 1
                # print(1)
            else:
                disct[f_index(p_l)] += 1

print(disct)
    # print(p)
