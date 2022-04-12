# https://www.algoexpert.io/questions/Topological%20Sort
# O(V+E) TS

from graph import AdjacencyListGraph


def topological_sort(vertices: list[int], edges: list[list[int]]) -> list[int]:
    graph = AdjacencyListGraph(is_directed=True)
    in_degree = {vertex: 0 for vertex in vertices}

    for start_vertex, end_vertex in edges:
        graph.add_edge(start_vertex, end_vertex)
        in_degree[end_vertex] += 1

    zero_indegree_queue = []
    for vertex, degree in in_degree.items():
        if degree == 0:
            zero_indegree_queue.append(vertex)

    topological_order = []
    while zero_indegree_queue:
        vertex = zero_indegree_queue.pop(0)
        topological_order.append(vertex)

        for adjacent_vertex in graph.get_adjacent_vertices(vertex):
            in_degree[adjacent_vertex] -= 1
            if in_degree[adjacent_vertex] == 0:
                zero_indegree_queue.append(adjacent_vertex)

    return topological_order if len(topological_order) == len(vertices) else []
