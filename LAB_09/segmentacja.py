from graf import *
import cv2
import numpy as np

class MST:
    def __init__(self, graph):
        self.mst_graph = Graph(None)

        self.intree = {i:0 for i in graph.vertices()}
        self.distance = {i:float("inf") for i in graph.vertices()}
        self.parent = {}

def mst_prim(graph, v):
    mst_g = MST(graph)
    mst_g.mst_graph.insert_vertex(v)

    tree_len = 0
    while mst_g.intree[v] == 0:
        mst_g.intree[v] = 1
        # update listy distance
        for neigh, neigh_dist in graph.neighbours(v):
            if mst_g.intree[neigh] == 0:
                if neigh_dist < mst_g.distance[neigh]:
                    mst_g.distance[neigh] = neigh_dist
                    mst_g.parent[neigh] = v

        # znajdywanie najbliższego sąsiada
        min_cost = float("inf")
        for vertex in graph.vertices():
            if mst_g.intree[vertex] == 0:
                if mst_g.distance[vertex] < min_cost:
                    min_cost = mst_g.distance[vertex]
                    v = vertex

        # dodawanie do grafu
        mst_g.mst_graph.insert_vertex(v)
        mst_g.mst_graph.insert_edge(v, mst_g.parent[v], edge_len = mst_g.distance[v])
        tree_len += mst_g.distance[v]

    tree_len -= mst_g.distance[v] # usunięcie ostatniej wartości edge_len bo jest dodawana 2 razy
    return mst_g.mst_graph, tree_len

def kolorowanie_obrazu(graph, start_vertex, image, kolor):
    visited = []
    queue = [start_vertex]
    y_size, x_size = image.shape

    while queue:
        vertex = queue.pop()

        for n_idx, _ in graph.neighbours(graph.get_vertex_id(vertex)):
            n = graph.get_vertex(n_idx)
            if n not in visited:
                queue.append(n)

        if vertex not in visited:
            visited.append(vertex)
            klucz = vertex.get_key()
            y = klucz // x_size
            x = klucz % x_size
            image[x, y] = kolor

def main():
    image = cv2.imread("sample.png", cv2.IMREAD_GRAYSCALE)
    y_size, x_size = image.shape

    graf = Graph(None)

    # pętla po obrazie
    for i in range(1, y_size-1):
        for j in range(1, x_size-1):
            vertex_id = x_size * j + i
            vertex = Vertex(vertex_id)

            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    vertex_id_2 = x_size * jj + ii
                    vertex_2 = Vertex(vertex_id_2)
                    distance = abs(image[ii, jj].astype(np.int32) - image[i, j].astype(np.int32))

                    graf.insert_edge(vertex, vertex_2, distance)

    mst_graph, tree_len = mst_prim(graf, Vertex(0))
    longest_edge = max(mst_graph.edges())

    root_1 = longest_edge.v1
    root_2 = longest_edge.v2

    mst_graph.delete_edge(root_1, root_2)

    image_segmented = np.zeros((y_size, x_size), dtype=np.uint8)

    kolorowanie_obrazu(mst_graph, root_1, image_segmented, 200)
    kolorowanie_obrazu(mst_graph, root_2, image_segmented, 100)

    cv2.imshow("Wynik", image_segmented)
    cv2.waitKey()

if __name__ == "__main__":
    main()