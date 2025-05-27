from copy import deepcopy

class Matrix:
    def __init__(self, matrix, value=0):
        if isinstance(matrix, tuple):
            a = [[value] * matrix[1] for i in range(matrix[0])]
            self.__matrix = a
        else:
            self.__matrix = matrix

    def __getitem__(self, item):
        return self.__matrix[item]

    def __setitem__(self, item, value):
        self.__matrix[item] = value

    def size(self):
        return len(self.__matrix), len(self.__matrix[0])

    def __add__(self, other):
        if self.size() != other.size():
            raise Exception("Złe wymiary macierzy")
        else:
            row_s, col_s = self.size()
            new_matrix = Matrix((row_s, col_s))

            for i in range(row_s):
                for j in range(col_s):
                    new_matrix[i][j] = self[i][j] + other[i][j]
            return new_matrix

    def __mul__(self, other):
        if self.size()[1] != other.size()[0]:
            raise Exception("Złe wymiary macierzy")
        else:
            row_s, col_s = self.size()
            row_o, col_o = other.size()
            new_matrix = Matrix((row_s, col_o))

            for i in range(row_s):
                for j in range(col_o):
                    for k in range(col_s):
                        new_matrix[i][j] += self[i][k] * other[k][j]

            return new_matrix

    def __eq__(self, other):
        if self.size() != other.size():
            return False

        row_s, col_s = self.size()
        for i in range(row_s):
            for j in range(col_s):
                if self[i][j] != other[i][j]:
                    return False

        return True

    def __str__(self):
        a = []
        for i in range(self.size()[0]):
            a.append("\n|")
            for j in range(self.size()[1]):
                a.append(str(self.__matrix[i][j]))
            a.append("|")
        return " ".join(a)

    def __repr__(self):
        a = []
        for i in range(self.size()[0]):
            a.append("\n|")
            for j in range(self.size()[1]):
                a.append(str(self.__matrix[i][j]))
            a.append("|")
        return " ".join(a)


def transpose(matrix):
    new_matrix = Matrix((matrix.size()[1], matrix.size()[0]))

    for i in range(matrix.size()[0]):
        for j in range(matrix.size()[1]):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix

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
        if vertex in self.__vertices:
            return

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

    def get_matrix(self):
        return self.__graph

    def __str__(self):
        return str(self.__graph)

def ullman(mac_M, graf_G, graf_P, current_row = 0, used_columns = None, correct_izo = None, calls = 0):
    calls += 1
    if used_columns is None:
        used_columns = [False] * mac_M.size()[1]
    if correct_izo is None:
        correct_izo = []

    if current_row == mac_M.size()[0]:
        mac_G = Matrix(graf_G.get_matrix())
        mac_P = Matrix(graf_P.get_matrix())
        if mac_P == mac_M * transpose(mac_M * mac_G):
            correct_izo.append(mac_M)
        return correct_izo, calls

    for idx, column in enumerate(used_columns):
        if column is False:
            used_columns[idx] = True
            mac_M[current_row] = [0] * mac_M.size()[1]
            mac_M[current_row][idx] = 1
            a, calls = ullman(mac_M, graf_G, graf_P, current_row + 1, used_columns, correct_izo, calls)
            used_columns[idx] = False
    return correct_izo, calls

def matrix_M_0(graf_G, graf_P):
    mac_M_0 = Matrix((len(graf_P.vertices()), len(graf_G.vertices())))

    for idx_P, vertex_P_idx in enumerate(graf_P.vertices()):
        for idx_G, vertex_G_idx in enumerate(graf_G.vertices()):
            order_P = len(graf_P.neighbours(vertex_P_idx))
            order_G = len(graf_G.neighbours(vertex_G_idx))
            if order_P <= order_G:
                mac_M_0[idx_P][idx_G] = 1
    return mac_M_0

def ullman_v2(mac_M, graf_G, graf_P, current_row = 0, used_columns = None, correct_izo = None, calls = 0):
    calls += 1
    if used_columns is None:
        used_columns = [False] * mac_M.size()[1]
    if correct_izo is None:
        correct_izo = []

    if current_row == mac_M.size()[0]:
        mac_G = Matrix(graf_G.get_matrix())
        mac_P = Matrix(graf_P.get_matrix())
        if mac_P == mac_M * transpose(mac_M * mac_G):
            correct_izo.append(mac_M)
        return correct_izo, calls

    mac_M_copy = deepcopy(mac_M)
    for idx, column in enumerate(used_columns):
        if column is False and mac_M[current_row][idx] != 0:
            used_columns[idx] = True
            mac_M_copy[current_row] = [0] * mac_M.size()[1]
            mac_M_copy[current_row][idx] = 1
            a, calls = ullman_v2(mac_M_copy, graf_G, graf_P, current_row + 1, used_columns, correct_izo, calls)
            used_columns[idx] = False
    return correct_izo, calls

def ullman_v3(mac_M, graf_G, graf_P, current_row = 0, used_columns = None, correct_izo = None, calls = 0):
    calls += 1
    if used_columns is None:
        used_columns = [False] * mac_M.size()[1]
    if correct_izo is None:
        correct_izo = []

    if current_row == mac_M.size()[0]:
        mac_G = Matrix(graf_G.get_matrix())
        mac_P = Matrix(graf_P.get_matrix())
        if mac_P == mac_M * transpose(mac_M * mac_G):
            correct_izo.append(mac_M)
        return correct_izo, calls

    mac_M_copy = deepcopy(mac_M)
    mac_M_copy = prune(mac_M_copy, graf_G, graf_P)
    for idx, column in enumerate(used_columns):
        if column is False and mac_M[current_row][idx] != 0:
            used_columns[idx] = True
            mac_M_copy[current_row] = [0] * mac_M.size()[1]
            mac_M_copy[current_row][idx] = 1
            a, calls = ullman_v3(mac_M_copy, graf_G, graf_P, current_row + 1, used_columns, correct_izo, calls)
            used_columns[idx] = False
    return correct_izo, calls

def prune(mac_M, graf_G, graf_P):
    row_s, col_s = mac_M.size()
    for i in range(row_s):
        for j in range(col_s):
            if mac_M[i][j] != 0:
                for x, _ in graf_P.neighbours(i):
                    y_list = graf_G.neighbours(j)
                    M_x_y_list = [mac_M[x][y] for y, _ in y_list]
                    if M_x_y_list == [0] * len(M_x_y_list):
                        mac_M[i][j] = 0
    return mac_M

def main():
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]

    graf_G = GraphMatrix()
    for v1, v2, edge in graph_G:
        graf_G.insert_vertex(Vertex(v1))
        graf_G.insert_vertex(Vertex(v2))
        graf_G.insert_edge(Vertex(v1), Vertex(v2), edge)

    graf_P = GraphMatrix()
    for v1, v2, edge in graph_P:
        graf_P.insert_vertex(Vertex(v1))
        graf_P.insert_vertex(Vertex(v2))
        graf_P.insert_edge(Vertex(v1), Vertex(v2), edge)

    mac_M = Matrix((len(graph_P), len(graph_G)))

    correct_izo, calls = ullman(mac_M, graf_G, graf_P)
    print(len(correct_izo), calls)

    mac_M_0 = matrix_M_0(graf_G, graf_P)
    correct_izo, calls = ullman_v2(mac_M_0, graf_G, graf_P)
    print(len(correct_izo), calls)

    mac_M_0 = matrix_M_0(graf_G, graf_P)
    correct_izo, calls = ullman_v3(mac_M_0, graf_G, graf_P)
    print(len(correct_izo), calls)

if __name__ == "__main__":
    main()