#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    if type(grid) != list:
        return 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 1
                if r < rows - 1 and grid[r+1][c] == 1:
                    perimeter -= 1
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 1
                if c < cols - 1 and grid[r][c+1] == 1:
                    perimeter -= 1

    return perimeter
