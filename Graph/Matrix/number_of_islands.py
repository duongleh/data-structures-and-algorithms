# https://leetcode.com/problems/number-of-islands

from Graph.DisjointSet.disjoint_set import UnionFind


class DisjointSet(UnionFind):
    def __init__(self):
        super().__init__(0)
        self.roots = {}
        self.ranks = {}
        self.components_count = 0

    def union(self, vertex_1: int, vertex_2: int):
        if super().union(vertex_1, vertex_2) is not None:
            self.components_count -= 1

    def find(self, vertex: int) -> int:
        if vertex not in self.roots:
            return 0
        return super().find(vertex)

    def add_vertex(self, vertex):
        if self.find(vertex):
            return

        self.roots[vertex] = vertex
        self.ranks[vertex] = 1
        self.components_count += 1


# O(N^2) T (average) | O(N) S
def number_of_islands_union_find(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    row_count = len(grid)
    column_count = len(grid[0])
    disjoint_set = DisjointSet()

    for row in range(row_count):
        for column in range(column_count):
            if grid[row][column] == "0":
                continue

            vertex = get_vertex_name(row, column, column_count)
            disjoint_set.add_vertex(vertex)

            if row > 0 and grid[row - 1][column] == "1":
                right_vertex = get_vertex_name(row - 1, column, column_count)
                disjoint_set.union(right_vertex, vertex)

            if column > 0 and grid[row][column - 1] == "1":
                up_vertex = get_vertex_name(row, column - 1, column_count)
                disjoint_set.union(up_vertex, vertex)

    return disjoint_set.components_count


def get_vertex_name(row: int, column: int, column_count: int) -> int:
    return row * column_count + column


# O(W*H) T | O(1) S
def number_of_islands_dfs(grid: list[list[str]]) -> int:
    count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                area = dfs(grid, i, j)
                if area > 0:
                    count += 1
        return count

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
        return 0

    grid[i][j] = "0"

    return 1 + dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1)
