#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
from pprint import pprint
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrixx = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

#     for row in matrix:
        # print(row)
    # print("*" * 10)
    # rotate_2d_matrix(matrix)
    # for row in matrix:
        # print(row)
    # print("*" * 10)
    # matrix = [[7, 4, 1],
              # [8, 5, 2],
              # [9, 6, 3]]
    # for row in matrix:
        # print(row)
    # print("*" * 30)


    matrix = [['01', '02', '03', '04'],
              ['05', '06', '07', '08'],
              ['09', '10', '11', '12'],
              ['13', '14', '15', '16']]
    for row in matrix:
        print(*row)
    print("*" * 10)
    rotate_2d_matrix(matrix)
    for row in matrix:
        print(*row)
    print("*" * 10)

    matrix = [['01', '02', '03', '04', '05'],
              ['06', '07', '08', '09', '10'],
              ['11', '12', '13', '14', '15'],
              ['16', '17', '18', '19', '20'],
              ['21', '22', '23', '24', '25']]
    for row in matrix:
        print(*row)
    print("*" * 10)
    rotate_2d_matrix(matrix)
    for row in matrix:
        print(*row)
    print("*" * 10)

