# https://leetcode.com/problems/shortest-path-in-binary-matrix
# O(N^2) T | O(N) S


def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    size = len(grid)
    queue = []
    if grid and grid[0][0] == 0:
        queue = [(0, 0, 1)]
        grid[0][0] = 1

    while queue:
        row, col, path_length = queue.pop(0)

        if (row, col) == (size - 1, size - 1):
            return path_length

        adjacent_vertices = get_adjacent_vertices(grid, size, row, col, path_length + 1)
        if adjacent_vertices:
            queue += adjacent_vertices

    return -1


def get_adjacent_vertices(
    grid: list[list[int]],
    size: int,
    row: int,
    col: int,
    path_length: int,
) -> list[tuple[int, int, int]]:
    adjacent_vertices = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for direction_row, direction_col in directions:
        adjacent_row = row + direction_row
        adjacent_col = col + direction_col

        if adjacent_row < 0 or adjacent_row >= size or adjacent_col < 0 or adjacent_col >= size:
            continue

        if grid[adjacent_row][adjacent_col] == 1:
            continue

        grid[adjacent_row][adjacent_col] = 1

        adjacent_vertices.append((adjacent_row, adjacent_col, path_length))

    return adjacent_vertices
