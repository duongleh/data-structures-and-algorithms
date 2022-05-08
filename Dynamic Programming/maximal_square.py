# https://leetcode.com/problems/maximal-square
# O(N*M) TS (N, M is the height, width of matrix respectively)


def maximal_square(matrix: list[list[str]]) -> int:
    def dfs(
        matrix: list[list[str]],
        squares: list[list[int]],
        height: int,
        width: int,
        row: int,
        col: int,
    ):
        if row >= height or col >= width:
            return 0

        if squares[row][col] is None:
            if matrix[row][col] == "0":
                squares[row][col] = 0
            else:
                args = (matrix, squares, height, width)
                squares[row][col] = 1 + min(
                    dfs(*args, row, col + 1),
                    dfs(*args, row + 1, col + 1),
                    dfs(*args, row + 1, col),
                )
                nonlocal max_area
                max_area = max(max_area, squares[row][col] * squares[row][col])
        return squares[row][col]

    height = len(matrix)
    width = len(matrix[0])
    squares = [[None] * width for _ in range(height)]
    max_area = 0

    for row in range(height):
        for col in range(width):
            dfs(matrix, squares, height, width, row, col)

    return max_area
