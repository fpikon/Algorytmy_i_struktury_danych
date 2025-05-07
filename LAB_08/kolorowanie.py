import polska
from grafy import *

def color_graph(graph, start_vertex,version = 0):
    visited = []
    queue = [start_vertex]
    color_dic = {}

    while queue:
        if version == 0:
            vertex = queue.pop(0)
        else:
            vertex = queue.pop()
        for n_idx, _ in graph.neighbours(graph.get_vertex_id(vertex)):
            n = graph.get_vertex(n_idx)
            if n not in visited:
                queue.append(n)

        if vertex not in visited:
            visited.append(vertex)
            neigh_colors = []
            for n_idx, neigh in graph.neighbours(graph.get_vertex_id(vertex)):
                neigh = graph.get_vertex(n_idx)
                if neigh in color_dic:
                    neigh_colors.append(color_dic[neigh])
            color_dic[vertex] = available_color(neigh_colors)

    color_list = [(str(vertex), color) for vertex, color in color_dic.items()]
    return color_list

def available_color(colors):
    color = 0
    while color in colors:
        color += 1
    return color


def main():
    vertices = [Vertex(miasto[-1]) for miasto in polska.polska]
    edges = polska.graf

    # graf na macierzy
    graph = GraphMatrix()
    for vertex in vertices:
        graph.insert_vertex(vertex)
    for edge in edges:
        graph.insert_edge(Vertex(str(edge[0])), Vertex(str(edge[1])))
    color_map = color_graph(graph, Vertex("W"), 0)
    polska.draw_map(graph, color_map)
    color_map = color_graph(graph, Vertex("W"), 1)
    polska.draw_map(graph, color_map)

    # graf na liście
    graph = GraphList(None)
    for vertex in vertices:
        graph.insert_vertex(vertex)
    for edge in edges:
        graph.insert_edge(Vertex(str(edge[0])), Vertex(str(edge[1])))
    color_map = color_graph(graph, Vertex("W"), 0)
    polska.draw_map(graph, color_map)
    color_map = color_graph(graph, Vertex("W"), 1)
    polska.draw_map(graph, color_map)

if __name__ == '__main__':
    main()