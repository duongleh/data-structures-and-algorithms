# O(V+E) T | O(V) S

from Graph.graph import AdjacencyListGraph


def detect_cycle_in_undirected_graph(
    graph: AdjacencyListGraph,
    vertex: int = 0,
    parent: int = 0,
    visited: set = None,
) -> bool:
    if visited is None:
        visited = set()

    if vertex in visited:
        return vertex != parent

    visited.add(vertex)

    for adjacent_vertex in graph.get_adjacent_vertices(vertex):
        if detect_cycle_in_undirected_graph(graph, adjacent_vertex, vertex, visited):
            return True

    return False
