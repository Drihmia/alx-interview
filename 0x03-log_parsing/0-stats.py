#!/usr/bin/python3
"""
this a script that reads fron stdin line by line and computes metrics.
this a script that reads fron stdin line by line and computes metrics.
"""
import sys


def print_sorted(dic, size):
    """
    A fucntion that sort a dic by keys and print
        the size and the dictionary
    """
    dic = dict(sorted(dic.items()))
    print("File size:", size, flush=True)
    for key, value in dic.items():
        print(str(key) + ":", value, flush=True)


def main():
    """
    main funtion : entry point
    """

    dic = {}
    total_size = 0
    N_lines = 0
    try:
        for lin in sys.stdin:
            try:
                line = lin.split()
                total_size += int(line[-1])
                tmp = line[-2]
                tmp = int(tmp)
                if tmp in dic:
                    dic[tmp] += 1
                else:
                    dic[tmp] = 1
                N_lines += 1
            except (IndexError, ValueError):
                continue
            if N_lines % 10 == 0:
                print_sorted(dic, total_size)
        print_sorted(dic, total_size)
    except KeyboardInterrupt as e:
        print_sorted(dic, total_size)


if __name__ == "__main__":
    main()
