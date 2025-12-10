# My solution to p10_paint_fill.py


def fill(grid, row, col, new_color):
    def dfs(grid, row, col, old_color, new_color):
        vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if not (0 <= row < len(grid) and 0 <= col < len(grid)):
            return
        if grid[row][col] != old_color:
            return
        grid[row][col] = new_color
        for drow, dcol in vectors:
            dfs(grid, row + drow, col + dcol, old_color, new_color)

    old_color = grid[row][col]
    dfs(grid, row, col, old_color, new_color)


grid = [[1, 2, 4, 3], [1, 2, 2, 3], [1, 2, 2, 3], [1, 6, 2, 3]]

fill(grid, 0, 1, 9)

print(grid)
