# https://leetcode.com/problems/max-area-of-island
# # O(W*H) T | O(1) S


def max_area_of_island(grid: list[list[int]]) -> int:
    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            area = dfs(grid, i, j)
            max_area = max(max_area, area)
    return max_area

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
        return 0

    grid[i][j] = 0

    return 1 + dfs(grid, i+1, j) + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1)
