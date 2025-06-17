import numpy as np
from copy import deepcopy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self):
        return f'({self.x}, {self.y})'

def triangle_perimeter(a, b, c):
    return a.distance(b) + b.distance(c) + c.distance(a)

def triangulation_rek(point_list):
    n = len(point_list)
    if n < 3:
        return 0
    if n == 3:
        return triangle_perimeter(point_list[0], point_list[1], point_list[2])

    i = point_list[0]
    j = point_list[-1]

    min_cost = float('inf')
    for k_idx in range(1, n-1):
        cost_tr = triangle_perimeter(i, j, point_list[k_idx])
        cost_r = triangulation_rek(point_list[k_idx:])
        cost_l = triangulation_rek(point_list[:k_idx+1])

        cost = cost_tr + cost_r + cost_l

        if cost < min_cost:
            min_cost = cost
    return min_cost



def main():
    p_list = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]

    point_list = []
    for x, y in p_list:
        point_list.append(Point(x, y))
    cost = triangulation_rek(point_list)
    print(cost)

    p_list = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]

    point_list = []
    for x, y in p_list:
        point_list.append(Point(x, y))
    cost = triangulation_rek(point_list)
    print(cost)

if __name__ == '__main__':
    main()