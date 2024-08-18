#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = boxes[0]

    queue = keys

    while queue:
        key = queue.pop(0)
        if key < n and not unlocked[key]:
            unlocked[key] = True
            queue.extend(boxes[key])

    return all(unlocked)
