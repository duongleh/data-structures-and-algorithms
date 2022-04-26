# https://leetcode.com/problems/network-delay-time

from math import inf

from dijkstra_algorithm import dijkstra_algorithm
from graph import AdjacencyListGraph


# O(N*E) TS
def network_delay_time_spfa(times: list[list[int]], start: int) -> int:
    graph = AdjacencyListGraph(is_directed=True, is_weighted=True)
    for source, destination, weight in times:
        graph.add_edge(source, destination, weight)

    distances = {vertex: inf for vertex in graph.vertices()}
    distances[start] = 0
    queue = [start]
    visited = {start}
    while queue:
        vertex = queue.pop(0)
        visited.remove(vertex)

        for adjacent_vertex, weight in graph.get_adjacent_vertices(vertex):
            if distances[vertex] + weight >= distances[adjacent_vertex]:
                continue
            distances[adjacent_vertex] = distances[vertex] + weight

            if adjacent_vertex in visited:
                continue
            queue.append(adjacent_vertex)
            visited.add(adjacent_vertex)
    return get_max_distance(distances)


# O((V + E) * log(V)) T | O(V) S
def network_delay_time_dijkstra(times: list[list[int]], start: int) -> int:
    graph = AdjacencyListGraph(is_directed=True, is_weighted=True)
    for source, destination, weight in times:
        graph.add_edge(source, destination, weight)

    distances, _ = dijkstra_algorithm(graph, start)
    return get_max_distance(distances)


def get_max_distance(distances: list[int]) -> int:
    max_distance = -inf
    for distance in distances.values():
        if distance == inf:
            return -1
        max_distance = max(distance, max_distance)
    return max_distance
