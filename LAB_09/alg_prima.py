from copy import deepcopy

from pygments.lexers import graph


class Vertex:
    def __init__(self, key):
        self.__key = key

    def __hash__(self):
        return hash(self.__key)

    def __eq__(self, other):
        return self.__key == other.__key

    def __repr__(self):
        return str(self.__key)

class Graph:
    def __init__(self, init_val = 0):
        self.__graph = {}
        self.__init_val = init_val

    def is_empty(self):
        return len(self.__graph) == 0

    def insert_vertex(self, vertex):
        if vertex in self.__graph.keys():
            return
        self.__graph[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge_len = 1.):
        self.__graph[vertex1][vertex2] = edge_len
        self.__graph[vertex2][vertex1] = edge_len

    def delete_vertex(self, vertex):
        for key in self.__graph.keys():
            if vertex in self.__graph[key]:
                self.__graph[key].pop(vertex)
        self.__graph.pop(vertex)

    def delete_edge(self, vertex1, vertex2):
        self.__graph[vertex1][vertex2] = self.__init_val
        self.__graph[vertex2][vertex1] = self.__init_val

    def neighbours(self, vertex_id):
        neigh_list = []
        for neigh in self.__graph[vertex_id].keys():
            if self.__graph[vertex_id][neigh] != self.__init_val:
                neigh_list.append((neigh, self.__graph[vertex_id][neigh]))
        return neigh_list

    def vertices(self):
        return self.__graph.keys()

    def get_vertex(self, vertex_idx):
        return vertex_idx

    def get_vertex_id(self, vertex):
        return vertex

    def order(self):
        return len(self.__graph)

    def __str__(self):
        return str(self.__graph)

class MST:
    def __init__(self, graph):
        self.mst_graph = Graph()

        self.intree = {i:0 for i in graph.vertices()}
        self.distance = {i:float("inf") for i in graph.vertices()}
        self.parent = {}


def mst_prim(graph, v):
    mst_g = MST(graph)
    mst_g.mst_graph.insert_vertex(v)

    tree_len = 0
    while mst_g.intree[v] == 0:
        mst_g.intree[v] = 1
        for neigh, neigh_dist in graph.neighbours(v):
            if mst_g.intree[neigh] == 0:
                if neigh_dist < mst_g.distance[neigh]:
                    mst_g.distance[neigh] = neigh_dist
                    mst_g.parent[neigh] = v

        min_cost = float("inf")
        for vertex in graph.vertices():
            if mst_g.intree[vertex] == 0:
                if mst_g.distance[vertex] < min_cost:
                    min_cost = mst_g.distance[vertex]
                    v = vertex

        mst_g.mst_graph.insert_vertex(v)
        mst_g.mst_graph.insert_edge(v, mst_g.parent[v], edge_len = mst_g.distance[v])
        tree_len += mst_g.distance[v]

    return mst_g.mst_graph, tree_len - mst_g.distance[v]

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def main():
    graf = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
            ('B', 'E', 9), ('B', 'F', 9), ('B', 'G', 7), ('B', 'C', 5),
            ('C', 'G', 9), ('C', 'D', 3),
            ('D', 'G', 10), ('D', 'J', 18),
            ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
            ('F', 'H', 2), ('F', 'G', 8),
            ('G', 'H', 9), ('G', 'J', 8),
            ('H', 'I', 3), ('H', 'J', 9),
            ('I', 'J', 9)
            ]

    my_graph = Graph()
    for v1, v2, edge_len in graf:
        v1 = Vertex(v1)
        v2 = Vertex(v2)
        my_graph.insert_vertex(v1)
        my_graph.insert_vertex(v2)
        my_graph.insert_edge(v1, v2, edge_len = edge_len)

    mst, mst_len = mst_prim(my_graph, Vertex('A'))

    printGraph(mst)
    print(mst_len)

if __name__ == '__main__':
    main()