#!/usr/bin/python3

import timeit

canUnlockAlls = [
    __import__('0-lockboxes').canUnlockAll,
    __import__('0-lockboxes_recursive').canUnlockAll
]
for canUnlockAll in canUnlockAlls:
    # Create a dictionary to map each function to its type
    method_types = {
        '0-lockboxes': 'iterative method',
        '0-lockboxes_recursive': 'recursive method'
    }
    print(f'------------------------ {method_types[canUnlockAll.__module__]} -------------------------')
    boxes = [
        [1, 3, 4],  # Box 0: Contains keys for boxes 1, 3, 4
        [2, 5],     # Box 1: Contains keys for boxes 2, 5
        [6],        # Box 2: Contains key for box 6
        [7, 8],     # Box 3: Contains keys for boxes 7, 8
        [9, 10],    # Box 4: Contains keys for boxes 9, 10
        [11, 12],   # Box 5: Contains keys for boxes 11, 12
        [13, 14],   # Box 6: Contains keys for boxes 13, 14
        [15, 16],   # Box 7: Contains keys for boxes 15, 16
        [17, 18],   # Box 8: Contains keys for boxes 17, 18
        [19, 20],   # Box 9: Contains keys for boxes 19, 20
        [21, 22],   # Box 10: Contains keys for boxes 21, 22
        [23, 24],   # Box 11: Contains keys for boxes 23, 24
        [25, 26],   # Box 12: Contains keys for boxes 25, 26
        [27, 28],   # Box 13: Contains keys for boxes 27, 28
        [29, 30],   # Box 14: Contains keys for boxes 29, 30
        [31, 32],   # Box 15: Contains keys for boxes 31, 32
        [33, 34],   # Box 16: Contains keys for boxes 33, 34
        [35, 36],   # Box 17: Contains keys for boxes 35, 36
        [37, 38],   # Box 18: Contains keys for boxes 37, 38
        [39, 40],   # Box 19: Contains keys for boxes 39, 40
        [41, 42],   # Box 20: Contains keys for boxes 41, 42
        [43, 44],   # Box 21: Contains keys for boxes 43, 44
        [45, 46],   # Box 22: Contains keys for boxes 45, 46
        [47, 48],   # Box 23: Contains keys for boxes 47, 48
        [49, 50],   # Box 24: Contains keys for boxes 49, 50
        [51, 52],   # Box 25: Contains keys for boxes 51, 52
        [53, 54],   # Box 26: Contains keys for boxes 53, 54
        [55, 56],   # Box 27: Contains keys for boxes 55, 56
        [57, 58],   # Box 28: Contains keys for boxes 57, 58
        [59, 60],   # Box 29: Contains keys for boxes 59, 60
        [61, 62],   # Box 30: Contains keys for boxes 61, 62
        [63, 64],   # Box 31: Contains keys for boxes 63, 64
        [65, 66],   # Box 32: Contains keys for boxes 65, 66
        [67, 68],   # Box 33: Contains keys for boxes 67, 68
        [69, 70],   # Box 34: Contains keys for boxes 69, 70
        [71, 72],   # Box 35: Contains keys for boxes 71, 72
        [73, 74],   # Box 36: Contains keys for boxes 73, 74
        [75, 76],   # Box 37: Contains keys for boxes 75, 76
        [77, 78],   # Box 38: Contains keys for boxes 77, 78
        [79, 80],   # Box 39: Contains keys for boxes 79, 80
        [81, 82],   # Box 40: Contains keys for boxes 81, 82
        [83, 84],   # Box 41: Contains keys for boxes 83, 84
        [85, 86],   # Box 42: Contains keys for boxes 85, 86
        [87, 88],   # Box 43: Contains keys for boxes 87, 88
        [89, 90],   # Box 44: Contains keys for boxes 89, 90
        [91, 92],   # Box 45: Contains keys for boxes 91, 92
        [93, 94],   # Box 46: Contains keys for boxes 93, 94
        [95, 96],   # Box 47: Contains keys for boxes 95, 96
        [97, 98],   # Box 48: Contains keys for boxes 97, 98
        [99],       # Box 49: Contains key for box 99
        [],         # Box 50: Empty box
        # ... Continue this pattern up to box 99
    ]


    print(canUnlockAll(boxes), f"box's length: {len(boxes)}")


    boxes = [[1], [2], [3], [4], []]
    print(f'Case 1: box\'s is {len(boxes)} : ', end=' ')
    print(timeit.timeit("canUnlockAll(boxes)",
                        globals=globals(), number=100000))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(f'Case 2: box\'s is {len(boxes)} : ', end=' ')
    print(timeit.timeit("canUnlockAll(boxes)",
                        globals=globals(), number=100000))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(f'Case 3: box\'s is {len(boxes)} : ', end=' ')
    print(timeit.timeit("canUnlockAll(boxes)",
                        globals=globals(), number=100000))

    try:
        boxes = []
        print(f'Case 4: box\'s is {len(boxes)} : ', end=' ')
        print(timeit.timeit("canUnlockAll(boxes)",
                            globals=globals(),
                            number=10000000))
    except Exception as e:
        print(e)

    boxes = [[], []]
    print(f'Case 5: box\'s is {len(boxes)} : ', end=' ')
    print(timeit.timeit("canUnlockAll(boxes)",
                        globals=globals(), number=10000000))

    boxes = [[], [], []]
    print(f'Case 6: box\'s is {len(boxes)} : ', end=' ')
    print(timeit.timeit("canUnlockAll(boxes)",
                        globals=globals(), number=10000000))

    print('---------------------------------------')
    boxes = [[1], [2], [3], [4], []]
    print(f'Case 7: box\'s is {len(boxes)} : ', end=' ')
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(f'Case 8: box\'s is {len(boxes)} : ', end=' ')
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(f'Case 9: box\'s is {len(boxes)} : ', end=' ')
    print(canUnlockAll(boxes))
