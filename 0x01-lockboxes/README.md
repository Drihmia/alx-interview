# Lockbox Problem Solution

## Overview

This repository contains solutions to the lockbox problem implemented in both recursive and iterative approaches. The task is to determine if all boxes can be unlocked given a list of boxes, where each box contains keys to other boxes.

### Task Description

The primary objective of this task is to verify if it's possible to unlock all boxes starting from the first box. Each box may contain keys to other boxes, and the goal is to traverse these keys to unlock all the boxes.

## Approaches

### Recursive Method

In the recursive method, I implemented a helper function to traverse through the boxes recursively. This method involves a depth-first search (DFS) approach to explore all possible keys from the current box.

```python
def canUnlockAll(box: List[List[int]]) -> bool:
    """A Function that returns true if all boxes are unlockable."""
    if not isinstance(box, list) or not all(isinstance(inner_box, list) for inner_box in box):
        return False

    size = len(box)
    if not size:
        return False
    if not len(box[0]):
        return True

    unLockedBoxes = {box: False if box else True for box in range(size)}

    def helper_function(innerBox: List[int]):
        for item in innerBox:
            if item > size - 1 or unLockedBoxes[(item)]:
                continue
            unLockedBoxes[item] = True
            helper_function(box[item])
        return unLockedBoxes

    helper_function(box[0])

    return all(unLockedBoxes.values())
```

#### Pros and Cons of Recursive Method

- **Pros:**
  - Easy to understand and implement.
  - Mimics the natural problem structure (DFS).

- **Cons:**
  - May hit the maximum recursion depth for large inputs.
  - Slower due to repeated function calls and stack management.
  - Higher space complexity due to call stack.

### Iterative Method

The iterative method uses a queue (implemented with a list) and a set to track unlocked boxes. This approach avoids the maximum recursion depth issue by using a breadth-first search (BFS) approach.

```python
def canUnlockAll(box) -> bool:
    """A Function that returns true if all boxes are unlockable."""
    if type(box) is not list or any(type(inner_box) is not list for inner_box in box):
        return False

    size = len(box)
    if not size:
        return False
    if not len(box[0]):
        return True

    Unlockedboxes_list = [0]
    Unlockedboxes_set = {0}

    for inner in Unlockedboxes_list:
        for key in box[inner]:
            if key < size and key not in Unlockedboxes_set:
                Unlockedboxes_set.add(key)
                Unlockedboxes_list.append(key)

    return len(Unlockedboxes_set) == size
```

#### Pros and Cons of Iterative Method

- **Pros:**
  - More efficient in terms of space as it avoids deep recursion.
  - Handles larger inputs without risk of hitting recursion limits.
  - Faster due to reduced overhead from function calls.

- **Cons:**
  - Slightly more complex to implement compared to recursion.
  - May use more memory if the list grows very large.

### Performance Comparison

#### Time Complexity

- **Recursive Method:** \(O(n + e)\), where \(n\) is the number of boxes and \(e\) is the number of keys.
- **Iterative Method:** \(O(n + e)\), with similar performance characteristics.

#### Space Complexity

- **Recursive Method:** \(O(n)\) due to the call stack and the dictionary storing the unlocked state.
- **Iterative Method:** \(O(n)\) due to the list and set used to track unlocked boxes.

### Performance Output

Using `timeit` to measure performance:

```bash
python3 main_0.py
------------------------ iterative method -------------------------
True box's length: 51
Case 1: box's is 5 :  0.06776266699307598
Case 2: box's is 7 :  0.09825541701866314
Case 3: box's is 7 :  0.06554408400552347
Case 4: box's is 0 :  0.9147539589903317
Case 5: box's is 2 :  1.400100625003688
Case 6: box's is 3 :  1.5798860419890843
---------------------------------------
Case 7: box's is 5 :  True
Case 8: box's is 7 :  True
Case 9: box's is 7 :  False
------------------------ recursive method -------------------------
True box's length: 51
Case 1: box's is 5 :  0.1537537499971222
Case 2: box's is 7 :  0.21754250000230968
Case 3: box's is 7 :  0.1654585830110591
Case 4: box's is 0 :  2.576279832981527
Case 5: box's is 2 :  3.372410834010225
Case 6: box's is 3 :  3.6739290000114124
---------------------------------------
Case 7: box's is 5 :  True
```

### Conclusion

I initially chose the recursive method for its simplicity and direct approach to solving the problem. However, due to limitations with the maximum recursion depth and performance issues, I opted for the iterative method. The iterative approach proved to be more efficient and scalable for larger inputs, making it the preferred solution for the lockbox problem.
