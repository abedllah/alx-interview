def canUnlockAll(boxes):
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
