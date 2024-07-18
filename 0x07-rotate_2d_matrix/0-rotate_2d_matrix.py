#!/usr/bin/python3
"""Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    Example: matrix 5 x 5                 Rotate the matrix in place:
             1,  2,  3,  4,  5            21, 16, 11,  6,  1

             6,  7,  8,  9, 10            22, 17, 12,  7,  2

            11, 12, 13, 14, 15            23, 18, 13,  8,  3

            16, 17, 18, 19, 20            24, 19, 14,  9,  4

            21, 22, 23, 24, 25            25, 20, 15, 10,  5
    Args:

    matrix: List[List[int]]: 2D matrix

    Returns:

    None
    """
    length = len(matrix)

    for box in range(length // 2):
        for i in range(box, length - box - 1):
            max_index = length - 1

            # Save the value of the 1st element (value of 1)
            temp = matrix[box][i]

            # 1st switch: 1st loop: put 12 in place of previous positionof 1
            matrix[box][i] = matrix[max_index - i][box]

            # 2nd switch: 1st loop: put 25 in place of previous position of 21
            matrix[max_index - i][box] = matrix[max_index - box][max_index - i]

            # 3rd switch: 1st loop: put 5 in place of previous position of 25
            matrix[max_index - box][max_index - i] = matrix[i][max_index - box]

            # 4th switch: put saved value of 1st element on the last element
            matrix[i][max_index - box] = temp
