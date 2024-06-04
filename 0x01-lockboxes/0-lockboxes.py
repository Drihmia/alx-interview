#!/usr/bin/python3

"""
trying to implement a solution for the lockbox problem using recursion
"""
from typing import List, Dict


def canUnlockAll(box: List[List[int]]) -> bool:
    """A Function that return true if all boxed are unlockable."""
    if type(box) is not list:
        return False

    for inner_box in box:
        if type(inner_box) is not list:
            return False

    size = len(box)

    # If the length of the box is zero, is empty.
    if not size:
        return False

    # If the first unlocked box is empty, no need to check the whole list.
    if not len(box[0]):
        return True

    unLockedBoxes = {box: True if not box else False
                     for box in range(size)}

    helper_function(box, box[0], size - 1, unLockedBoxes)

    if False in unLockedBoxes.values():
        return False
    else:
        return True


def helper_function(box: List[List[int]],
                    innerBox: List[int], Last_Index: int,
                    unLockedBoxes: Dict[int, bool]) -> Dict[int, bool]:
    """
    A recursive helper function that return a dictionary of
    unlocked and locked boxes, the keys are the boxes's index and the values,
    are either, True for unlocked boxes or False for locked boxes.
    """

    for item in innerBox:
        if item > Last_Index or unLockedBoxes.get(item):
            continue
        unLockedBoxes[item] = True

        helper_function(box, box[item], Last_Index, unLockedBoxes)

    return unLockedBoxes
