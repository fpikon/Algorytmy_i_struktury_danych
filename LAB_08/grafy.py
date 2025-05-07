import polska

class Vertex:
    def __init__(self, key):
        self.__key = key

    def __hash__(self):
        return hash(self.__key)

    def __eq__(self, other):
        return self.__key == other.__key

    def __repr__(self):
        return str(self.__key)

class GraphMatrix:
    def __init__(self, init_val = 0):
        self.__vertices = []
        self.__graph = [[]]
        self.__init_val = init_val

    def is_empty(self):
        return self.__graph == [[]]

    def insert_vertex(self, vertex):
        for row in self.__graph:
            row.append(self.__init_val)
        if self.order() != 0:
            self.__graph.append([self.__init_val] * (self.order() + 1))
        self.__vertices.append(vertex)

    def insert_edge(self, vertex1, vertex2, edge = 1):
        id_1 = self.get_vertex_id(vertex1)
        id_2 = self.get_vertex_id(vertex2)

        self.__graph[id_1][id_2] = edge
        self.__graph[id_2][id_1] = edge

    def delete_vertex(self, vertex):
        vertex_id = self.get_vertex_id(vertex)

        for row in self.__graph:
            row.pop(vertex_id)
        self.__graph.pop(vertex_id)

        self.__vertices.pop(vertex_id)

    def delete_edge(self, vertex1, vertex2):
        id_1 = self.get_vertex_id(vertex1)
        id_2 = self.get_vertex_id(vertex2)

        self.__graph[id_1][id_2] = 0
        self.__graph[id_2][id_1] = 0

    def neighbours(self, vertex_idx):
        neigh_list = []
        for idx, neigh in enumerate(self.__graph[vertex_idx]):
            if neigh != 0:
                neigh_list.append((idx, neigh))
        return neigh_list

    def vertices(self):
        vertex_list = []
        for vertex in self.__vertices:
            vertex_list.append(self.get_vertex_id(vertex))
        return vertex_list

    def order(self):
        return len(self.__vertices)

    def get_vertex_id(self, vertex):
        vertex_id = 0
        while self.__vertices[vertex_id] != vertex:
            vertex_id += 1
        return  vertex_id

    def get_vertex(self, vertex_idx):
        return self.__vertices[vertex_idx]

    def __str__(self):
        return str(self.__graph)

class GraphList:
    def __init__(self, init_val = 0):
        self.__graph = {}
        self.__init_val = init_val

    def is_empty(self):
        return len(self.__graph) == 0

    def insert_vertex(self, vertex):
        for key in self.__graph.keys():
            self.__graph[key][vertex] = self.__init_val
        self.__graph[vertex] = {key: self.__init_val for key in self.__graph.keys()}

    def insert_edge(self, vertex1, vertex2, edge = 1):
        self.__graph[vertex1][vertex2] = edge
        self.__graph[vertex2][vertex1] = edge

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
                neigh_list.append((neigh, neigh))
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


def main():
    vertices = [Vertex(miasto[-1]) for miasto in polska.polska]
    edges = polska.graf

    # graf na macierzy
    graph = GraphMatrix()
    for vertex in vertices:
        graph.insert_vertex(vertex)
    for edge in edges:
        graph.insert_edge(Vertex(str(edge[0])), Vertex(str(edge[1])))
    graph.delete_vertex(Vertex('K'))
    graph.delete_edge(Vertex('W'), Vertex('E'))
    polska.draw_map(graph)

    # graf na liście
    graph = GraphList(None)
    for vertex in vertices:
        graph.insert_vertex(vertex)
    for edge in edges:
        graph.insert_edge(Vertex(str(edge[0])), Vertex(str(edge[1])))
    graph.delete_vertex(Vertex('K'))
    graph.delete_edge(Vertex('W'), Vertex('E'))
    polska.draw_map(graph)

if __name__ == '__main__':
    main()