#!/usr/bin/python3

"""
trying to implement a solution for the lockbox problem using recursion
"""
from typing import List


def canUnlockAll(box: List[List[int]]) -> bool:
    """A Function that return true if all boxed are unlockable."""
    if not isinstance(box, list) or not all(isinstance(inner_box, list)
                                            for inner_box in box):
        return False

    size = len(box)

    # If the length of the box is zero, is empty.
    if not size:
        return False

    # If the first unlocked box is empty, no need to check the whole list.
    if not len(box[0]):
        return True

    unLockedBoxes = {box: False if box else True for box in range(size)}

    def helper_function(innerBox: List[int]):
        """
        A recursive helper function that return a dictionary of
        unlocked and locked boxes, the keys are the boxes's index and the
        values, are either, True for unlocked boxes or False for locked boxes.
        """

        for item in innerBox:
            if item > size - 1 or unLockedBoxes[(item)]:
                continue
            unLockedBoxes[item] = True

            helper_function(box[item])

        return unLockedBoxes

    # Call the helper_function:
    helper_function(box[0])

    if all(unLockedBoxes.values()):
        return True
    return False
