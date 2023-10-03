#!/usr/bin/python3
'''
The function that recive boxes and determines if
all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    Check if all the boxes can be opened
    '''
    
    # size of boxes
    boxesLen = len(boxes)

    # based on question the first box boxes[0] is unlocked
    currentKeys = set(boxes[0])
    openenBoxes = set([0])

    while len(currentKeys) > 0:
        # pick key from avilabe key we have
        key = currentKeys.pop()

        # if the key is out (higher or lower) of our boxes
        if key >= boxesLen or key < 0:
            continue

        if key not in openenBoxes:
            currentKeys = currentKeys.union(boxes[key])
            openenBoxes.add(key)

    return boxesLen == len(openenBoxes)