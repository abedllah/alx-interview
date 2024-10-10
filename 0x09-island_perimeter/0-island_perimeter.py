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
                # Add 4 for each land cell
                perimeter += 4
                
                # Subtract 1 for each neighboring land cell
                if r > 0 and grid[r-1][c] == 1:  # Check the cell above
                    perimeter -= 1
                if r < rows - 1 and grid[r+1][c] == 1:  # Check the cell below
                    perimeter -= 1
                if c > 0 and grid[r][c-1] == 1:  # Check the cell to the left
                    perimeter -= 1
                if c < cols - 1 and grid[r][c+1] == 1:  # Check the cell to the right
                    perimeter -= 1
                    
    return perimeter
