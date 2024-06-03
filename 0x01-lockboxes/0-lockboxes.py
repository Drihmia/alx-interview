#!/usr/bin/python3

"""
trying to implement a solution for the lockbox problem using recursion
"""
from typing import List, Dict


def canUnlockAll(box: List[List[int]]) -> bool:

    size = len(box) - 1

    unLockedBoxes = {box: True if not box else False
                     for box in range(size + 1)}
    # print(unLockedBoxes)

    helper_function(box, box[0], size, unLockedBoxes)
    # print(unLockedBoxes)

    if False in unLockedBoxes.values():
        return False
    else:
        return True


def helper_function(box: List[List[int]],
                    innerBox: List[int], size: int,
                    unLockedBoxes: Dict[int, bool]) -> Dict[int, bool]:
    for item in innerBox:
        if item > size or unLockedBoxes.get(item):
            continue
        unLockedBoxes[item] = True

        helper_function(box, box[item], size, unLockedBoxes)

    return unLockedBoxes
