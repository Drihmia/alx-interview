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
    list_of_1 = [row.count(1) for row in grid if row.count(1) > 0]
    return (len(list_of_1) + max(list_of_1)) * 2
