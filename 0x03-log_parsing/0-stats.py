#!/usr/bin/python3
"""
    Log parsing
## input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
## Notes:
# if the format is not this one, the line must be skipped.
# After every 10 lines and/or a keyboard interruption (CTRL + C),
the following statistics from the beginning will be printed:
# Total file size: File size: <total size>
# where <total size> is the sum of all previous <file size>
# Number of lines by status code:
# possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
# if a status code doesn’t appear or is not an integer,
don’t print anything for this status status_code_dict
# format: <status code>: <number>
# status codes should be printed in ascending order

"""
from signal import signal, SIGINT
from sys import stdin
from typing import Dict


def print_output(status_code_dict: Dict[int, int], file_size: int) -> None:
    """
    Print the parsing output to stdout

    Args:
        status_code_dict: a dict of status code and number of thier occurrence.
        file_size: an integer that refers to file size
    """
    print("File size:", file_size)
    for k, v in status_code_dict.items():
        if v:
            print(f"{k}: {v}")


def hundler(_, __):
    print_output(dict_count, file_size_total)


if __name__ == "__main__":
    counter = 0
    dict_count = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
    }
    file_size_total = 0

    for line in stdin:
        line_splited = line.split()
        if len(line_splited) == 9:
            try:
                status_code = int(line_splited[-2])
                file_size = int(line_splited[-1])
                counter += 1
            except (TypeError, IndexError) as e:
                continue

            dict_count[status_code] += 1
            file_size_total += file_size

        if not counter % 10:
            print_output(dict_count, file_size_total)
        signal(SIGINT, hundler)
