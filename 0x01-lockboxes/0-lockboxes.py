#!/usr/bin/python3
""" preparing for interviews"""


def canUnlockAll(boxes):
    ''' checks if all boxes can be opened '''
    unlocked_boxes = []
    keys = [0]
    while True:
        if keys == unlocked_boxes:
            break
        for key in keys:
            if key not in unlocked_boxes:
                unlocked_boxes.append(key)
        for box in unlocked_boxes:
            current_box = boxes[box]
            for _box in current_box:
                if _box not in keys and _box < len(boxes):
                    keys.append(_box)
    return len(unlocked_boxes) == len(boxes)
