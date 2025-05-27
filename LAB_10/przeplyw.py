# OCENA 4.5/5

"""
Miało być True dla resztowej a nie rzeczywistej
"""

from graf import *

def BFS(graph, start_vertex):
    visited = []
    parent = {}
    queue = [start_vertex]

    while queue:
        vertex = queue.pop()

        for n_idx, egde in graph.neighbours(vertex):
            n = graph.get_vertex(n_idx)
            egde = graph.get_edge(graph.get_vertex_id(vertex), n_idx)
            if n not in visited and egde.res_capacity > 0:
                queue.append(n)
                parent[n] = vertex

        if vertex not in visited:
            visited.append(vertex)

    return parent

def find_lowest_capacity(graph, start_vertex, end_vertex, parent):
    try:
        if not parent[end_vertex]:
            return None
    except KeyError:
        return None

    current = end_vertex
    lowest_capacity = float('inf')
    while current != start_vertex:
        curr_parent = parent[current]
        curr_edge = graph.get_edge(curr_parent, current)
        if curr_edge.res_capacity < lowest_capacity:
            lowest_capacity = curr_edge.res_capacity

        current = curr_parent

    return lowest_capacity

def augmentation(graph, start_vertex, end_vertex, parent, lowest_cap):
    try:
        if not parent[end_vertex]:
            return None
    except KeyError:
        return None

    current = end_vertex
    while current != start_vertex:
        curr_parent = parent[current]
        edge = graph.get_edge(curr_parent, current)
        edge_reverse = graph.get_edge(current, curr_parent)

        edge.res_capacity -= lowest_cap
        edge_reverse.res_capacity += lowest_cap

        if edge.real:
            edge.flow += lowest_cap
        else:
            edge_reverse.flow -= lowest_cap
        current = curr_parent

def ford_fulkerson(graph, start_vertex, end_vertex):
    path_exist = True

    while path_exist:
        parent = BFS(graph, start_vertex)
        try:
            if not parent[end_vertex]:
                path_exist = False
                break
            else:
                path_exist = True
        except KeyError:
            path_exist = False
            break
        low_cap = find_lowest_capacity(graph, start_vertex, end_vertex, parent)
        augmentation(graph, start_vertex, end_vertex, parent, low_cap)


    flow_sum = 0
    for n, edge in graph.neighbours(end_vertex):
        edge_reverse = graph.get_edge(n, end_vertex)
        flow_sum += edge_reverse.flow

    return flow_sum

def main():
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3), ('s', 'v', 1), ('v', 't', 2)]
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20),
              ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6),
              ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 3), ('s', 'd', 2), ('a', 'b', 4), ('b', 'c', 5), ('c', 't', 6), ('a', 'f', 3),  ('f', 't', 3),
              ('d', 'e', 2), ('e','f',2)]

    graph = Graph()

    for v1, v2, edge_len in graf_0:
        graph.insert_edge(Vertex(v1), Vertex(v2), edge_len)
        graph.insert_edge(Vertex(v2), Vertex(v1), edge_len, False)

    flow_sum = ford_fulkerson(graph, Vertex('s'), Vertex('t'))
    print(flow_sum)
    printGraph(graph)
    flow_from_a = 0
    for n, edge in graph.neighbours(Vertex('u')):
        if edge.real:
            flow_from_a += edge.flow
    print(flow_from_a)

    graph = Graph()

    for v1, v2, edge_len in graf_1:
        graph.insert_edge(Vertex(v1), Vertex(v2), edge_len)
        graph.insert_edge(Vertex(v2), Vertex(v1), edge_len, False)

    flow_sum = ford_fulkerson(graph, Vertex('s'), Vertex('t'))
    print(flow_sum)
    printGraph(graph)
    flow_from_a = 0
    for n, edge in graph.neighbours(Vertex('a')):
        if edge.real:
            flow_from_a += edge.flow
    print(flow_from_a)

    graph = Graph()

    for v1, v2, edge_len in graf_2:
        graph.insert_edge(Vertex(v1), Vertex(v2), edge_len)
        graph.insert_edge(Vertex(v2), Vertex(v1), edge_len, False)

    flow_sum = ford_fulkerson(graph, Vertex('s'), Vertex('t'))
    print(flow_sum)
    printGraph(graph)
    flow_from_a = 0
    for n, edge in graph.neighbours(Vertex('a')):
        if edge.real:
            flow_from_a += edge.flow
    print(flow_from_a)

    graph = Graph()

    for v1, v2, edge_len in graf_3:
        graph.insert_edge(Vertex(v1), Vertex(v2), edge_len)
        graph.insert_edge(Vertex(v2), Vertex(v1), edge_len, False)

    flow_sum = ford_fulkerson(graph, Vertex('s'), Vertex('t'))
    print(flow_sum)
    printGraph(graph)
    flow_from_a = 0
    for n, edge in graph.neighbours(Vertex('a')):
        if edge.real:
            flow_from_a += edge.flow
    print(flow_from_a)

if __name__ == "__main__":
    main()