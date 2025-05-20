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
    def __init__(self, v1, v2, capacity, real):
        self.v1 = v1
        self.v2 = v2
        if real:
            self.capacity = capacity
            self.flow = 0
        else:
            self.capacity = 0
            self.flow = 0
        self.real = real
        self.res_capacity = self.capacity - self.flow

    def __str__(self):
        return f"{self.capacity} {self.flow} {self.res_capacity} {self.real}"

    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.res_capacity} {self.real}"


class Graph:
    def __init__(self, init_val=None):
        self.__graph = {}
        self.__init_val = init_val

    def is_empty(self):
        return len(self.__graph) == 0

    def insert_vertex(self, vertex):
        if vertex in self.__graph.keys():
            return
        self.__graph[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge_len=1., real=True):
        if vertex1 == vertex2:
            return
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.__graph[vertex1][vertex2] = Edge(vertex1, vertex2, edge_len, real)
        #self.__graph[vertex2][vertex1] = edge_len

    def delete_vertex(self, vertex):
        for key in self.__graph.keys():
            if vertex in self.__graph[key]:
                self.__graph[key].pop(vertex)
        self.__graph.pop(vertex)

    def delete_edge(self, vertex1, vertex2):
        self.__graph[vertex1][vertex2] = self.__init_val
        #self.__graph[vertex2][vertex1] = self.__init_val

    def neighbours(self, vertex_idx):
        neigh_list = []
        for neigh in self.__graph[vertex_idx].keys():
            if self.__graph[vertex_idx][neigh] != self.__init_val:
                neigh_list.append((neigh, self.__graph[vertex_idx][neigh]))
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

    def get_edge(self, vertex1_idx, vertex2_idx):
        if vertex1_idx in self.__graph and vertex2_idx in self.__graph[vertex1_idx]:
            return self.__graph[vertex1_idx][vertex2_idx]

    def order(self):
        return len(self.__graph)

    def __str__(self):
        return str(self.__graph)


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end=" -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
