#!/usr/bin/python3
""" Test case for canUnlockAll, It should return True"""


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
    if __name__ == "__main__":
        boxes = []

        keys: list[int] = []
        for n in range(1, 1000):
            keys = []
            for m in range(1, 1000):
                keys.append(m)
            boxes.append(keys)

        try:
            print(canUnlockAll(boxes))
        except Exception as e:
            print(e)
