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
    if not grid:
        return 0

    height = len(grid)
    width = len(grid[0])
    islands_count = 0

    for row in range(height):
        for col in range(width):
            if grid[row][col] != "1":
                continue

            dfs(grid, row, col, height, width)
            islands_count += 1

    return islands_count


def dfs(grid, row, col, height, width):
    if grid[row][col] != "1":
        return

    grid[row][col] = "-1"

    for adjacent_row, adjacent_col in get_adjacent_vertices(row, col, height, width):
        dfs(grid, adjacent_row, adjacent_col, height, width)


def get_adjacent_vertices(row, col, height, width) -> list[tuple[int, int]]:
    adjacent_vertices = []
    directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]

    for row_direction, col_direction in directions:
        adjacent_row = row + row_direction
        adjacent_col = col + col_direction

        if adjacent_row < 0 or adjacent_row >= height or adjacent_col < 0 or adjacent_col >= width:
            continue

        adjacent_vertices.append((adjacent_row, adjacent_col))
    return adjacent_vertices
