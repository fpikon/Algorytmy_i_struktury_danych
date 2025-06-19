import numpy as np
from time import perf_counter

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

def triangulation_it(point_list):
    n = len(point_list)
    if n < 3:
        return 0
    if n == 3:
        return triangle_perimeter(point_list[0], point_list[1], point_list[2])

    table = [[float("inf") for i in range(len(point_list))] for j in range(len(point_list))]

    for i in range(0, n-1):
        table[i][i+1] = 0

    for m in range(3, n + 1):
        for i in range(n-m+1):
            j = i + m - 1
            table[i][j] = float("inf")
            for k in range(i + 1, j):
                cost = triangle_perimeter(point_list[i], point_list[j], point_list[k])
                cost += table[i][k]
                cost += table[k][j]
                if cost < table[i][j]:
                    table[i][j] = cost

    return table[0][-1], table

def main():
    p_list = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]

    point_list = []
    for x, y in p_list:
        point_list.append(Point(x, y))
    start_time = perf_counter()
    cost = triangulation_rek(point_list)
    end_time = perf_counter()
    time_taken = end_time - start_time
    print(f"{cost:.04f}, {time_taken:.07f}")

    p_list = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]

    point_list = []
    for x, y in p_list:
        point_list.append(Point(x, y))

    start_time = perf_counter()
    cost = triangulation_rek(point_list)
    end_time = perf_counter()
    time_taken = end_time - start_time
    print(f"{cost:.04f}, {time_taken:.07f}")

    p_list = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]

    point_list = []
    for x, y in p_list:
        point_list.append(Point(x, y))

    start_time = perf_counter()
    cost, table = triangulation_it(point_list)
    end_time = perf_counter()
    time_taken = end_time - start_time
    print(f"{cost:.04f}, {time_taken:.07f}")

    p_list = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]

    point_list = []
    for x, y in p_list:
        point_list.append(Point(x, y))

    start_time = perf_counter()
    cost, table = triangulation_it(point_list)
    end_time = perf_counter()
    time_taken = end_time - start_time
    print(f"{cost:.04f}, {time_taken:.07f}")


if __name__ == '__main__':
    main()