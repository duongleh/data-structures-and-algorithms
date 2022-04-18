# https://leetcode.com/problems/min-cost-to-connect-all-points

import math

from disjoint_set import UnionFind


# O(Elog(E)) T | O(E) S (E is the number of edges, E = N*(N-1)/2 ≈ N^2)
def min_cost_connect_points_kruskal_algorithm(points: list[list[int]]) -> int:
    size = len(points)
    edges = []
    for vertex1, (x1, y1) in enumerate(points):
        for vertex2 in range(vertex1 + 1, size):
            x2, y2 = points[vertex2]
            distance = get_manhattan_distance(x1, y1, x2, y2)
            edges.append((vertex1, vertex2, distance))

    edges.sort(key=lambda element: element[2])

    disjoint_set = UnionFind(size)
    cost = 0
    connected_edges = 0
    for vertex1, vertex2, distance in edges:
        if disjoint_set.union(vertex1, vertex2) is None:
            continue

        cost += distance
        connected_edges += 1
        if connected_edges == (size - 1):
            break

    return cost


# O(E) T | O(N) S
def min_cost_connect_points_prim_algorithm(points: list[list[int]]) -> int:
    if not points:
        return 0

    size = len(points)
    visited = [False] * size
    min_distances = [math.inf] * size

    current_vertex = 0
    min_distances[0] = 0
    visited[0] = True

    cost = 0
    added_edges = 0
    while added_edges < size - 1:
        min_distance = math.inf
        x1, y1 = points[current_vertex]

        for vertex, (x2, y2) in enumerate(points):
            if visited[vertex]:
                continue
            distance = get_manhattan_distance(x1, y1, x2, y2)
            if distance < min_distances[vertex]:
                min_distances[vertex] = distance
            if min_distances[vertex] < min_distance:
                min_distance = min_distances[vertex]
                current_vertex = vertex

        visited[current_vertex] = True
        added_edges += 1
        cost += min_distance

    return cost


def get_manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)
