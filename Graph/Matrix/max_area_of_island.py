# https://leetcode.com/problems/max-area-of-island
# # O(W*H) T | O(1) S


def max_area_of_island(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    height = len(grid)
    width = len(grid[0])
    max_area = 0
    for row in range(height):
        for col in range(width):
            area = dfs(grid, row, col, height, width)
            max_area = max(max_area, area)
    return max_area


def dfs(
    grid: list[list[int]],
    row: int,
    col: int,
    height: int,
    width: int,
    area: int = 0,
):
    if grid[row][col] == 0:
        return area
    area += 1
    grid[row][col] = 0
    for adjacent_row, adjacent_col in get_adjacent_lands(grid, row, col, height, width):
        area += dfs(grid, adjacent_row, adjacent_col, height, width)
    return area


def get_adjacent_lands(
    grid: list[list[int]],
    row: int,
    col: int,
    height: int,
    width: int,
) -> list[tuple[int, int]]:
    directions = [
        (0, 1),
        (0, -1),
        (-1, 0),
        (1, 0),
    ]
    adjacent_lands = []
    for row_direction, col_direction in directions:
        adjacent_row = row + row_direction
        adjacent_col = col + col_direction
        if adjacent_row < 0 or adjacent_row >= height or adjacent_col < 0 or adjacent_col >= width:
            continue

        if grid[adjacent_row][adjacent_col] == 0:
            continue

        adjacent_lands.append((adjacent_row, adjacent_col))

    return adjacent_lands
