# Ocena 5/5

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'({self.x}, {self.y})'


def orientation(p1, p2, p3):
    val = (p2.y - p1.y)*(p3.x - p1.x) - (p3.y - p2.y)*(p2.x - p1.x)

    if val > 0:
        return 1 # prawoskrętne
    elif val < 0:
        return -1 # lewoskrętne
    else:
        return 0 # współliniowe


def jarvis_v1(point_list):
    start_point = point_list[0]

    for point in point_list:
        if point.x < start_point.x:
            start_point = point
        elif point.x == start_point.x and point.y < start_point.y:
            start_point = point

    p = start_point
    return_list = []
    while True:
        return_list.append(p)
        q_idx = point_list.index(p) + 1 if point_list.index(p) < len(point_list) - 1 else 0
        q = point_list[q_idx]

        for r in point_list:
            if r == q or r == p:
                continue
            if orientation(p, q, r) == 1:
                q = r
        p = q
        if p == start_point:
            break

    return return_list

def jarvis_v2(point_list):
    start_point = point_list[0]

    for point in point_list:
        if point.x < start_point.x:
            start_point = point
        elif point.x == start_point.x and point.y < start_point.y:
            start_point = point

    p = start_point
    return_list = []
    while True:
        return_list.append(p)
        q_idx = point_list.index(p) + 1 if point_list.index(p) < len(point_list) - 1 else 0
        q = point_list[q_idx]

        for r in point_list:
            if r == q or r == p:
                continue
            if orientation(p, q, r) == 1:
                q = r
            if orientation(p, r, q) == 0:
                if p.x < q.x < r.x or r.x < q.x < p.x or p.y < q.y < r.y or r.y < q.y < p.y:
                    q = r

        p = q
        if p == start_point:
            break

    return return_list

def main():
    lista_1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    lista_2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]

    point_list_1= []
    for x, y in lista_1:
        point_list_1.append(Point(x, y))
    point_list_2 = []
    for x, y in lista_2:
        point_list_2.append(Point(x, y))

    print(jarvis_v1(point_list_1))
    print(jarvis_v1(point_list_2))

    print(jarvis_v2(point_list_1))
    print(jarvis_v2(point_list_2))

    lista_3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]


    point_list_3 = []
    for x, y in lista_3:
        point_list_3.append(Point(x, y))

    print(jarvis_v1(point_list_3))
    print(jarvis_v2(point_list_3))

if __name__ == '__main__':
    main()



