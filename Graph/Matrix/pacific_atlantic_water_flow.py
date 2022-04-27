# https://leetcode.com/problems/pacific-atlantic-water-flow
# O(M*N) TS


def pacific_atlantic_water_flow(matrix: list[list[int]]) -> list[list[int]]:
    height = len(matrix)
    width = len(matrix[0]) if height else 0
    reached_pacific_ocean = set()
    reached_atlantic_ocean = set()

    for col in range(width):
        traverse_island(matrix, reached_pacific_ocean, 0, col, height, width)
        traverse_island(matrix, reached_atlantic_ocean, height - 1, col, height, width)

    for row in range(height):
        traverse_island(matrix, reached_pacific_ocean, row, 0, height, width)
        traverse_island(matrix, reached_atlantic_ocean, row, width - 1, height, width)

    return list(reached_pacific_ocean & reached_atlantic_ocean)


def traverse_island(
    matrix: list[list[int]],
    reached_ocean: set[tuple[int, int]],
    row: int,
    col: int,
    height: int,
    width: int,
) -> None:
    if (row, col) in reached_ocean:
        return

    reached_ocean.add((row, col))

    for adjacent_row, adjacent_col in get_adjacent_vertices(matrix, row, col, height, width):
        traverse_island(matrix, reached_ocean, adjacent_row, adjacent_col, height, width)


def get_adjacent_vertices(
    matrix: list[list[int]],
    row: int,
    col: int,
    height: int,
    width: int,
) -> list[tuple[int, int]]:
    directions = [
        (0, -1),
        (-1, 0),
        (0, 1),
        (1, 0),
    ]
    adjacent_vertices = []
    for row_direction, col_direction in directions:
        adjacent_row = row + row_direction
        adjacent_col = col + col_direction

        if is_ocean(adjacent_row, adjacent_col, height, width):
            continue

        if matrix[row][col] <= matrix[adjacent_row][adjacent_col]:
            adjacent_vertices.append((adjacent_row, adjacent_col))

    return adjacent_vertices


def is_ocean(
    row: int,
    col: int,
    height: int,
    width: int,
) -> bool:
    return row < 0 or col < 0 or row >= height or col >= width
