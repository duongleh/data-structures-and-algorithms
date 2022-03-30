# https://leetcode.com/problems/find-if-path-exists-in-graph
# O(V+E) T | O(V+E) S

from graph import AdjacencyListGraph


def valid_path_dfs(edges: list[list[int]], source: int, destination: int) -> bool:
    graph = AdjacencyListGraph()
    for start_vertex, end_vertex in edges:
        graph.add_edge(start_vertex, end_vertex)

    visited_vertices = set()
    stack = [source]

    while stack:
        vertex = stack.pop()

        if vertex in visited_vertices:
            continue

        if vertex == destination:
            return True

        visited_vertices.add(vertex)
        stack += graph.get_adjacent_vertices(vertex)

    return False


def valid_path_bfs(edges: list[list[int]], source: int, destination: int) -> bool:
    graph = AdjacencyListGraph()
    for start_vertex, end_vertex in edges:
        graph.add_edge(start_vertex, end_vertex)

    queue = [source]
    visited_vertices = set()

    while queue:
        vertex = queue.pop(0)

        if vertex in visited_vertices:
            continue

        if vertex == destination:
            return True

        visited_vertices.add(vertex)
        queue += graph.get_adjacent_vertices(vertex)

    return False
