def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continuously
        connected vertically or horizontally  by '1's.
    It's also preferred to check/mark the visited islands:
    - e.g. using the helper function - mark_islands().
    """
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                islands += 1
                mark_islands(i, j, grid)
    return islands


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visited islands as in-place operation.
    """
    if (
            (i >= 0)
            and (i < len(grid))
            and (j >= 0)
            and (j < len(grid[i]))
            and grid[i][j] == 1
    ):
        grid[i][j] = '#'
        mark_islands(i - 1, j, grid)
        mark_islands(i + 1, j, grid)
        mark_islands(i, j - 1, grid)
        mark_islands(i, j + 1, grid)
