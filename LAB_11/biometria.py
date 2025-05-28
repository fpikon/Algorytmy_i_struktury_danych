import os
from copy import deepcopy

import cv2
import matplotlib.pyplot as plt
import numpy as np


class Vertex:
    def __init__(self, key):
        key = (float(key[0]), float(key[1]))
        self.key = key

    def get_key(self):
        return self.key

    def __hash__(self):
        return hash(self.key)

    def __index__(self):
        return self.key

    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return str(self.key)

    def __str__(self):
        return str(self.key)

class Edge:
    def __init__(self, v1, v2, length, angle):
        self.v1 = v1
        self.v2 = v2
        self.length = length
        self.angle = angle

    def __eq__(self, other):
        if isinstance(other, Edge):
            return self.length == other.length
        return False

    def __lt__(self, other):
        return self.length < other.length

    def __repr__(self):
        return f"{self.v1} -> {self.v2} : {self.length:.02f} {self.angle:.02f}"

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

    def insert_edge(self, vertex1, vertex2):
        if vertex1 == vertex2:
            return
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        dist = np.sqrt((vertex1.key[0] - vertex2.key[0])**2 + (vertex1.key[1] - vertex2.key[1])**2)
        angle = np.arctan2(vertex2.key[0] - vertex1.key[0], vertex2.key[1] - vertex1.key[1])
        if angle < 0:
            angle += 2 * np.pi
        self.__graph[vertex1][vertex2] = Edge(vertex1, vertex2, dist, angle)

    def delete_vertex(self, vertex):
        if vertex not in self.__graph.keys():
            return
        for key in self.__graph.keys():
            if vertex in self.__graph[key]:
                self.__graph[key].pop(vertex)
        self.__graph.pop(vertex)

    def delete_edge(self, vertex1, vertex2):
        self.__graph[vertex1][vertex2] = self.__init_val

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
            for neigh in self.__graph[vertex]:
                edge_list.append(self.__graph[vertex][neigh])
        return edge_list

    def get_vertex(self, vertex_idx):
        return vertex_idx

    def get_vertex_id(self, vertex):
        return vertex

    def get_edge(self, vertex1, vertex2):
        return self.__graph[vertex1][vertex2]

    def order(self):
        return len(self.__graph)

    def __str__(self):
        return str(self.__graph)

    def plot_graph(self, v_color, e_color):
        for idx, v in enumerate(self.vertices()):
            y, x = v.key
            plt.scatter(x, y, c=v_color)
            for n_idx, _ in self.neighbours(v):
                yn, xn = self.get_vertex(n_idx).key
                plt.plot([x, xn], [y, yn], color=e_color)

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def fill_biometric_graph_from_image(img_bin, graph):
    y_size, x_size = img_bin.shape

    for i in range(y_size):
        for j in range(x_size):
            if img_bin[i, j] != 0:
                v = Vertex((i, j))
                graph.insert_vertex(v)
                n_coords = [(i, j - 1), (i - 1, j), (i - 1, j - 1), (i - 1, j + 1)]
                for n_i, n_j in n_coords:
                    if img_bin[n_i, n_j] != 0:
                        n = Vertex((n_i, n_j))
                        graph.insert_edge(v, n)
                        graph.insert_edge(n, v)

def unclutter_biometric_graph(graph):
    v_to_delete = []
    e_to_add = []
    for vertex in graph.vertices():
        n_list = graph.neighbours(vertex)
        if len(n_list) == 2:
            continue

        for n, edge in n_list:
            current_v = n
            prev_v = current_v
            current_n_list = graph.neighbours(current_v)
            while len(current_n_list) == 2:
                v_to_delete.append(current_v)
                if current_n_list[0][0] != prev_v:
                    current_v, prev_v = current_n_list[0][0], current_v
                else:
                    current_v, prev_v = current_n_list[1][0], current_v
                current_n_list = graph.neighbours(current_v)
            e_to_add.append((vertex, current_v))
    for v in v_to_delete:
        graph.delete_vertex(v)

    for v1, v2 in e_to_add:
        graph.insert_edge(v1, v2)
        graph.insert_edge(v2, v1)

def merge_near_vertices(graph, thr = 5):
    cluster_list = []
    for v_1 in graph.vertices():
        cluster = []
        flag = False
        for cl in cluster_list:
            if v_1 in cl:
                flag = True
        if flag is True:
            continue
        cluster.append(v_1)
        for v_2 in graph.vertices():
            if v_1 == v_2:
                continue

            flag = False
            for cl in cluster_list:
                if v_2 in cl:
                    flag = True
            if flag is True:
                continue

            distance = np.sqrt((v_1.key[0] - v_2.key[0])**2 + (v_1.key[1] - v_2.key[1])**2)
            if distance < thr:
                cluster.append(v_2)
        cluster_list.append(cluster)

    for cluster in cluster_list:
        if len(cluster) < 2:
            continue
        new_v_coord = [0, 0]
        connections = []
        for vertex in cluster:
            new_v_coord[0] += vertex.key[0]
            new_v_coord[1] += vertex.key[1]
            for n, _ in graph.neighbours(vertex):
                if n not in cluster:
                    connections.append(n)

        new_v_coord[0] = new_v_coord[0]/len(cluster)
        new_v_coord[1] = new_v_coord[1]/len(cluster)
        new_vertex = Vertex(tuple(new_v_coord))

        for v_1 in cluster:
            graph.delete_vertex(v_1)

        graph.insert_vertex(new_vertex)
        for connection in connections:
            graph.insert_edge(new_vertex, connection)
            graph.insert_edge(connection, new_vertex)

def translate_and_rotate(graph, vec_dist, angle):
    start_graph = deepcopy(graph)
    ty, tx = vec_dist
    vertex_dic = {}
    for vertex in start_graph.vertices():
        y, x = vertex.key
        x_prim = (x + tx) * np.cos(angle) + (y + ty) * np.sin(angle)
        y_prim = -(x + tx) * np.sin(angle) + (y + ty) * np.cos(angle)
        vertex_dic[vertex] = (y_prim, x_prim)

    for edge in start_graph.edges():
        v1 = edge.v1
        v2 = edge.v2

        graph.delete_vertex(v1)
        graph.delete_vertex(v2)

        new_v1 = Vertex(vertex_dic[v1])
        new_v2 = Vertex(vertex_dic[v2])

        graph.insert_edge(new_v1, new_v2)

def snap_edge_to_x_axis(graph, edge):
    angle = edge.angle
    vec_dist = [-edge.v1.key[0], -edge.v1.key[1]]
    translate_and_rotate(graph, vec_dist, angle)


def biometric_graph_registration(graph1_input, graph2_input, Ni=50, eps=10):
    edge_dist_list = []
    for edge_a in graph1_input.edges():
        l_a = edge_a.length
        theta_a = edge_a.angle
        for edge_b in graph2_input.edges():
            l_b = edge_b.length
            theta_b = edge_b.angle
            s_ab = 1/(0.5*(l_a + l_b)) * np.sqrt((l_a-l_b)**2+(theta_a-theta_b)**2)
            edge_dist_list.append((edge_a, edge_b, s_ab))

    edge_dist_list.sort(key = lambda x: x[2])

    graph1_output = deepcopy(graph1_input)
    graph2_output = deepcopy(graph2_input)
    lowest_dk = float("inf")
    for edge_a, edge_b, s_ab in edge_dist_list[:Ni]:
        graph1_temp = deepcopy(graph1_input)
        graph2_temp = deepcopy(graph2_input)

        snap_edge_to_x_axis(graph1_temp, edge_a)
        snap_edge_to_x_axis(graph2_temp, edge_b)

        v1_list = list(graph1_temp.vertices())
        v2_list = list(graph2_temp.vertices())

        c = 0
        for v1 in v1_list:
            smallest_dist = float("inf")
            closest_v2 = None
            for v2 in v2_list:
                distance = np.sqrt((v1.key[0] - v2.key[0])**2 + (v1.key[1] - v2.key[1])**2)
                if distance < smallest_dist:
                    smallest_dist = distance
                    closest_v2 = v2
            if smallest_dist < eps:
                c += 1
                v2_list.remove(closest_v2)

        dk = 1 - c / np.sqrt(graph1_temp.order() + graph2_temp.order())

        if dk < lowest_dk:
            lowest_dk = dk
            graph1_output = graph1_temp
            graph2_output = graph2_temp

    return graph1_output, graph2_output

def main():
    data_path = "./Images"
    img_level = "easy"
    img_list = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))]

    input_data = []
    for img_name in img_list:
        if img_name[-3:] == "png":
            if img_name.split('_')[-2] == img_level:
                print("Processing ", img_name, "...")

                img = cv2.imread(os.path.join(data_path, img_name))
                img_1ch = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                _, img_bin = cv2.threshold(img_1ch, 127, 255, cv2.THRESH_BINARY)
               
                graph = Graph()
                fill_biometric_graph_from_image(img_bin, graph)
                unclutter_biometric_graph(graph)

                for i in range(5):
                    merge_near_vertices(graph, thr=5)

                input_data.append((img_name, graph))
                print("Saved!")

    for i in range(len(input_data)):
        for j in range(len(input_data)):
            graph1_input = input_data[i][1]
            graph2_input = input_data[j][1]

            graph1, graph2 = biometric_graph_registration(graph1_input, graph2_input, Ni=50, eps=10)

            plt.figure()
            graph1.plot_graph(v_color='red', e_color='green')

            graph2.plot_graph(v_color='gold', e_color='blue')
            plt.title('Graph comparison')
            plt.show()

if __name__ == "__main__":
    main()