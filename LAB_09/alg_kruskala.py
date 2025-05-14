from graf import *

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.size = [1] * n
        self.p = list(range(n))

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(self.p[v])
        return self.p[v]

    def union_sets(self, s1, s2):
        root_s1 = self.find(s1)
        root_s2 = self.find(s2)

        if root_s1 == root_s2:
            return

        if self.size[root_s1] < self.size[root_s2]:
            root_s1, root_s2 = root_s2, root_s1

        self.p[root_s2] = root_s1
        self.size[root_s1] += self.size[root_s2]
        return

    def same_component(self, s1, s2):
        root_s1 = self.find(s1)
        root_s2 = self.find(s2)

        return root_s1 == root_s2

    def __str__(self):
        return f"{self.p} \n{self.size}"

def kruskal(graph):
    edge_list = sorted(graph.edges())
    v_list = graph.vertices()
    v_enum = {v: i for i, v in enumerate(v_list)}
    uf = UnionFind(len(v_list))

    edges_in_tree = []
    for edge in edge_list:
        v1 = v_enum[edge.v1]
        v2 = v_enum[edge.v2]
        if not uf.same_component(v1, v2):
            uf.union_sets(v1, v2)
            edges_in_tree.append(edge)

    return edges_in_tree

def main():
    graf_testowy = [('A', 'B', 4), ('A', 'C', 1), ('A', 'D', 4),
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
    for v1, v2, edge_len in graf_testowy:
        v1 = Vertex(v1)
        v2 = Vertex(v2)
        my_graph.insert_vertex(v1)
        my_graph.insert_vertex(v2)
        my_graph.insert_edge(v1, v2, edge_len=edge_len)

    mst = kruskal(my_graph)

    mst_graph = Graph()
    for edge in mst:
        v1 = edge.v1
        v2 = edge.v2
        edge_len = edge.edge_len
        v1 = Vertex(v1)
        v2 = Vertex(v2)
        mst_graph.insert_vertex(v1)
        mst_graph.insert_vertex(v2)
        mst_graph.insert_edge(v1, v2, edge_len=edge_len)

        edge = Edge(v1, v2, edge_len)
        print(edge)
    printGraph(mst_graph)

if __name__ == '__main__':
    main()