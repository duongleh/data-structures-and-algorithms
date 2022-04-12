# https://www.algoexpert.io/questions/Cycle%20In%20Graph
# O(V+E) T | O(V) S

from graph import AdjacencyListGraph


def dfs_with_processing_stack(
    graph: AdjacencyListGraph,
    vertex: int = 0,
    visited: set[int] = None,
    processing_stack: list[int] = None,
) -> bool:
    """
    DFS with a stack storing all decendants being processed
    While visiting a descendant of a vertex, if we found it in the stack it means a cycle appears.
    """
    if visited is None:
        visited = set()

    if processing_stack is None:
        processing_stack = []

    if vertex in visited:
        return vertex in processing_stack

    visited.add(vertex)
    processing_stack.append(vertex)

    for adjacent_vertex in graph.get_adjacent_vertices(vertex):
        if dfs_with_processing_stack(graph, adjacent_vertex, visited, processing_stack):
            return True

    processing_stack.pop()
    return False


UNVISITED, PROCESSING, VISITED = 0, 1, 2


def dfs_with_three_states(graph: AdjacencyListGraph) -> bool:
    """
    DFS with an array storing 3 different states of a vertex.
    Each vertex can have 3 different states:
        state 0   : Vertex is not visited. It's a default state.
        state 1   : Vertex is being processed. Either all of its
                    descendants are not processed or it's still in the function call stack.
        state 2   : vertex and all its descendants are processed.
    """

    vertex_states = len(graph) * [UNVISITED]

    def has_cycle(graph: AdjacencyListGraph, vertex_states: list[int], vertex: int) -> bool:
        if vertex_states[vertex] == PROCESSING:
            return True

        if vertex_states[vertex] == VISITED:
            return False

        vertex_states[vertex] = PROCESSING

        for adjacent_vertex in graph.get_adjacent_vertices(vertex):
            if has_cycle(graph, vertex_states, adjacent_vertex):
                return True

        vertex_states[vertex] = VISITED

        return False

    for vertex in graph.vertices:
        if has_cycle(graph, vertex_states, vertex):
            return True
    return False
