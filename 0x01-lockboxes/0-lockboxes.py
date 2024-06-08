#!/usr/bin/python3
"""
trying to implement a solution for the lockbox problem using recursion
"""


def canUnlockAll(box) -> bool:
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

    Unlockedboxes_list = [0]
    Unlockedboxes_set = {0}

    for inner in Unlockedboxes_list:
        for key in box[inner]:
            if key < size and key not in Unlockedboxes_set:
                Unlockedboxes_set.add(key)
                Unlockedboxes_list.append(key)

    if len(Unlockedboxes_set) == size:
        return True
    return False
