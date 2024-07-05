#!/usr/bin/python3
"""N queens puzzle
"""
import sys


def queens(N):
    """N queens puzzle
    """


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    queens(N)
