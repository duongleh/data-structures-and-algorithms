# https://leetcode.com/problems/clone-graph/
# O(V+E) T | O(V) S

from typing import Optional


class Vertex:
    def __init__(self, val=0, neighbors: list = None):
        self.val = val
        self.neighbors = neighbors or []


def clone_graph(self, vertex: Optional[Vertex], visited: dict = None) -> Optional[Vertex]:
    if not vertex:
        return None

    if visited is None:
        visited = {}

    if vertex.val in visited:
        return visited[vertex.val]

    cloned_vertex = Vertex(vertex.val)
    visited[vertex.val] = cloned_vertex

    cloned_neighbors = []
    for neighbor in vertex.neighbors:
        cloned_neighbor = self.cloneGraph(neighbor, visited)
        cloned_neighbors.append(cloned_neighbor)

    cloned_vertex.neighbors = cloned_neighbors
    return cloned_vertex
