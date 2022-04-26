# https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
# O(V+E) T | O(V) S

from Graph.graph import AdjacencyListGraph


def breadth_first_traversal(
    graph: AdjacencyListGraph,
    vertex: int = 0,
):
    queue = [vertex] if graph.vertex_count() > 0 else []
    visited_vertices = set()
    traversed_vertices = []

    while queue:
        vertex = queue.pop(0)
        if vertex in visited_vertices:
            continue

        visited_vertices.add(vertex)
        traversed_vertices.append(vertex)
        queue += graph.get_adjacent_vertices(vertex)

    return traversed_vertices
