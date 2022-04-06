# O(V+E) T | O(V) S

from graph import AdjacencyListGraph


def detect_cycle_in_directed_graph(
    graph: AdjacencyListGraph,
    vertex: int = 0,
    visited: set = None,
    visited_stack: list = None,
) -> bool:
    if visited is None:
        visited = set()

    if visited_stack is None:
        visited_stack = []

    if vertex in visited:
        return vertex in visited_stack

    visited.add(vertex)
    visited_stack.append(vertex)

    for adjacency_vertex in graph.get_adjacent_vertices(vertex):
        if detect_cycle_in_directed_graph(graph, adjacency_vertex, visited, visited_stack):
            return True

    visited_stack.pop()
    return False
