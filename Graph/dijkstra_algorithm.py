# https://www.algoexpert.io/questions/Dijkstra%27s%20Algorithm
# O((V + E) * log(V)) T | O(V) S

import heapq
from math import inf

from graph import AdjacencyListGraph


def dijkstra_algorithm(
    graph: AdjacencyListGraph,
    start: int,
) -> tuple[dict[int, int], dict[int, int]]:
    distances = {}
    previous = {}
    for vertex in graph.vertices():
        distances[vertex] = inf
        previous[vertex] = None
    distances[start] = 0
    heap = [(0, start)]
    heapq.heapify(heap)
    visited = set()

    while heap:
        distance, vertex = heapq.heappop(heap)
        if vertex in visited:
            continue
        visited.add(vertex)

        for adjacent_vertex, weight in graph.get_adjacent_vertices(vertex):
            if distances[vertex] + weight >= distances[adjacent_vertex]:
                continue
            distances[adjacent_vertex] = distances[vertex] + weight
            heapq.heappush(heap, (distance + weight, adjacent_vertex))
            previous[adjacent_vertex] = vertex

    return distances, previous
