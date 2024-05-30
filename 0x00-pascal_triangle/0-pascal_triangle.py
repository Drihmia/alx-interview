#!/usr/bin/python3
"""
Module contain a function called pascal_triangle
"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers representing
        the Pascal’s triangle of n.
    """
    if n <= 0:
        return []
    mat = [[1]]
    for i in range(1, n):
        row = []
        for j in range(i+1):
            jl = 0 if j - 1 < 0 else mat[i - 1][j - 1]
            jr = 0 if j >= len(mat[i - 1]) else mat[i - 1][j]
            row.append(jl + jr)
        mat.append(row)
    return mat
