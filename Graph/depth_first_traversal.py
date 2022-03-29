# https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
# O(V+E) T | O(V) S

from graph import AdjacencyListGraph


def depth_first_traversal(
    graph: AdjacencyListGraph,
    vertex: int = 0,
    visited_vertices: set = None,
    traversed_vertices: list = None,
):
    if visited_vertices is None:
        visited_vertices = set()
    if traversed_vertices is None:
        traversed_vertices = []

    visited_vertices.add(vertex)
    traversed_vertices.append(vertex)

    for adjacency_vertex in graph.get_adjacent_vertices(vertex):
        if adjacency_vertex in visited_vertices:
            continue

        depth_first_traversal(
            graph,
            adjacency_vertex,
            visited_vertices,
            traversed_vertices,
        )

    return traversed_vertices
