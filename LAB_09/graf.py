class Vertex:
    def __init__(self, key):
        self.__key = key

    def get_key(self):
        return self.__key

    def __hash__(self):
        return hash(self.__key)

    def __index__(self):
        return self.__key

    def __eq__(self, other):
        return self.__key == other.__key

    def __lt__(self, other):
        return self.__key < other.__key

    def __repr__(self):
        return str(self.__key)

    def __str__(self):
        return str(self.__key)

class Edge:
    def __init__(self, v1, v2, edge_len):
        self.v1 = v1
        self.v2 = v2
        self.edge_len = edge_len

    def __eq__(self, other):
        return self.edge_len == other.edge_len

    def __lt__(self, other):
        return self.edge_len < other.edge_len

    def __str__(self):
        return f"{self.v1} -> {self.v2} : {self.edge_len}"

    def __repr__(self):
        return f"{self.v1} -> {self.v2} : {self.edge_len}"

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
        if vertex1 == vertex2:
            return
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
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

    def edges(self):
        edge_list = []

        for vertex in self.__graph.keys():
            for neigh in self.__graph[vertex].keys():
                edge_list.append(Edge(vertex, neigh, self.__graph[vertex][neigh]))

        return edge_list

    def get_vertex(self, vertex_idx):
        return vertex_idx

    def get_vertex_id(self, vertex):
        return vertex

    def order(self):
        return len(self.__graph)

    def __str__(self):
        return str(self.__graph)

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")