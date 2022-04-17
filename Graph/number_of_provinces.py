# https://leetcode.com/problems/number-of-provinces

from disjoint_set import UnionFind


class DisjointSet(UnionFind):
    def __init__(self, size: int):
        super().__init__(size)
        self.components_count = size

    def union(self, vertex_1: int, vertex_2: int):
        if super().union(vertex_1, vertex_2) is not None:
            self.components_count -= 1


# O(N^2) T (average) | O(N) S
def number_of_provinces_union_find(grid: list[list[int]]) -> int:
    number_of_cities = len(grid)
    disjoint_set = DisjointSet(number_of_cities)
    for row in range(number_of_cities):
        for col in range(number_of_cities):
            if grid[row][col]:
                disjoint_set.union(row, col)

    return disjoint_set.components_count


# O(N^2) T | O(N) S
def number_of_provinces_dfs(grid: list[list[int]]) -> int:
    number_of_cities = len(grid)
    visited = set()
    number_of_provinces = 0

    def dfs(grid, vertex, visited):
        if vertex in visited:
            return

        visited.add(vertex)

        for adjacent_vertex, is_connected in enumerate(grid[vertex]):
            if is_connected and vertex != adjacent_vertex:
                dfs(grid, adjacent_vertex, visited)

    for vertex in range(number_of_cities):
        if vertex in visited:
            continue
        dfs(grid, vertex, visited)
        number_of_provinces += 1

    return number_of_provinces
