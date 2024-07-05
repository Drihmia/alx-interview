#!/usr/bin/python3
"""Module for N queens problem."""


def queen(N):
    output = []
    pos = []

    def helper_function(x: int):
        if x == N:
            output.append(pos[:])
            return

        for y in range(N):
            if is_valid(pos, x, y):
                pos.append([x, y])
                helper_function(x + 1)
                pos.pop()  # Backtrack

    def is_valid(board, x, y):
        for row in board:

            # check rows
            if x == row[0]:
                return False

            # check columns
            if y == row[1]:
                return False

            # diagonale top-right
            if x + y == sum(row):
                return False

            # diagonale top-left
            x_1, y_1 = x, y
            y_x_sum = x + y
            row_sum = sum(row)

            if ((y_x_sum % 2 == 0 and row_sum % 2 == 0)) or (
                    y_x_sum % 2 == 1 and row_sum % 2 == 1):

                diff = y_x_sum - row_sum
                # path 1
                if diff < 0:
                    for i in range((-diff) // 2):
                        x_1 += 1
                        y_1 += 1
                        if [x_1, y_1] == row:
                            return False
                # path 2
                else:
                    for i in range(diff // 2):
                        x_1 -= 1
                        y_1 -= 1
                        if [x_1, y_1] == row:
                            return False
        return True

    helper_function(0)
    return output


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = queen(N)
    for solution in solutions:
        print(solution)
