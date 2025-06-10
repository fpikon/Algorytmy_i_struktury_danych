import numpy as np
from numpy.testing.print_coercion_tables import print_new_cast_table


def ASM_rek(P, T, i=None, j=None):
    if i is None:
        i = len(P) - 1
    if j is None:
        j = len(T) - 1

    if i == 0:
        return j
    if j == 0:
        return i

    insert_cost = 1 + ASM_rek(P, T, i, j-1)
    del_cost = 1 + ASM_rek(P, T, i-1, j)
    swap_cost = int(P[i] != T[j]) + ASM_rek(P, T, i-1, j - 1)

    return min(insert_cost, del_cost, swap_cost)

def ASM_PD(P, T, substring = False):
    factor = 1
    if substring:
        factor = 9999
    D = [[0 for i in range(len(T))] for j in range(len(P))]
    for k in range(len(T)):
        D[0][k] = k
    for k in range(len(P)):
        D[k][0] = k
    parents = [["X" for i in range(len(T))] for j in range(len(P))]
    for k in range(1, len(T)):
        parents[0][k] = "I"
    for k in range(1, len(P)):
        parents[k][0] = "D"

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            insert_cost = 1 + D[i][j-1]
            del_cost = 1 + D[i-1][j]
            swap_cost = int(P[i]!=T[j])* factor + D[i-1][j-1]

            lowest_cost = min(insert_cost, del_cost, swap_cost)
            D[i][j] = lowest_cost

            if insert_cost == lowest_cost:
                parents[i][j] = "I"
            if del_cost == lowest_cost:
                parents[i][j] = "D"
            if swap_cost == lowest_cost:
                parents[i][j] = "S" if P[i]!=T[j] else "M"

    path = ""
    i = len(P) - 1
    j = len(T) - 1

    while i >= 0 and j >= 0:
        if i == j == 0:
            break
        path = parents[i][j] + path
        if parents[i][j] == "I":
            j -= 1
        elif parents[i][j] == "D":
            i -= 1
        else:
            i -= 1
            j -= 1

    return D[len(P)-1][len(T)-1], path

def ASM_podciag(P, T):
    D = [[0 for i in range(len(T))] for j in range(len(P))]
    for k in range(len(P)):
        D[k][0] = k
    parents = [["X" for i in range(len(T))] for j in range(len(P))]
    for k in range(1, len(P)):
        parents[k][0] = "D"

    for i in range(1, len(P)):
        for j in range(1, len(T)):
            insert_cost = 1 + D[i][j-1]
            del_cost = 1 + D[i-1][j]
            swap_cost = int(P[i]!=T[j]) + D[i-1][j-1]

            lowest_cost = min(insert_cost, del_cost, swap_cost)
            D[i][j] = lowest_cost

            if insert_cost == lowest_cost:
                parents[i][j] = "I"
            if del_cost == lowest_cost:
                parents[i][j] = "D"
            if swap_cost == lowest_cost:
                parents[i][j] = "S" if P[i]!=T[j] else "M"

    lowest_cost = float("inf")
    idx_lowest_cost = 0
    for k in range(len(T)):
        if D[len(P)-1][k] < lowest_cost:
            lowest_cost = D[len(P)-1][k]
            idx_lowest_cost = k


    return lowest_cost, idx_lowest_cost - (len(P)-2)

def main():
    p = " kot"
    t = " koń"
    t = " pies"

    cost = ASM_rek(p, t)
    print(cost)

    p = " kot"
    t = " koń"
    t = " pies"

    p = ' biały autobus'
    t = ' czarny autokar'

    cost, path = ASM_PD(p, t)
    print(cost)

    p = ' thou shalt not'
    t = ' you should not'

    cost, path = ASM_PD(p, t)
    print(path)

    P = ' ban'
    T = ' mokeyssbanana'
    cost, idx_lowest_cost = ASM_podciag(P, T)
    print(idx_lowest_cost)

    p = ' democrat'
    t = ' republican'

    cost, path = ASM_PD(p, t, True)
    str_out = ""
    idx_p = 0
    for i in range(len(path)):
        if path[i] == "D":
            idx_p += 1
        elif path[i] == "M":
            idx_p += 1
            str_out += p[idx_p]
    print(str_out)

    p = ' 123456789'
    t = ' 243517698'

    cost, path = ASM_PD(p, t, True)
    str_out = ""
    idx_p = 0
    for i in range(len(path)):
        if path[i] == "D":
            idx_p += 1
        elif path[i] == "M":
            idx_p += 1
            str_out += p[idx_p]
    print(str_out)

if __name__ == "__main__":
    main()