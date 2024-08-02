#!/usr/bin/python3
"""
This file contain a funtion called :
    island_perimeter
"""


def island_perimeter(grid):
    """ a funtion that returns the perimeter of the
    island described in grid
    """
    if not grid:
        return 0

    max_idx_x = len(grid[0]) - 1
    max_idx_y = len(grid) - 1
    island_per = 0
    visited = set()

    def recursive_island_perimeter(x, y):
        """Recursive function to compute the perimeter of an island if exist.
        """
        if x < 0 or x > max_idx_x or y < 0 or y > max_idx_y:
            return

        if grid[y][x] == 0:
            return

        if (x, y) not in visited:
            visited.add((x, y))
        else:
            return

        nonlocal island_per

        if x == max_idx_x or not grid[y][x + 1]:
            island_per += 1

        if y == max_idx_y or not grid[y + 1][x]:
            island_per += 1

        if not x or not grid[y][x - 1]:
            island_per += 1

        if not y or not grid[y - 1][x]:
            island_per += 1

        recursive_island_perimeter(x + 1, y)
        recursive_island_perimeter(x, y - 1)
        recursive_island_perimeter(x - 1, y)
        recursive_island_perimeter(x, y + 1)

    for y in range(max_idx_y + 1):
        for x in range(max_idx_x + 1):
            if grid[y][x]:
                recursive_island_perimeter(x, y)
                return island_per
