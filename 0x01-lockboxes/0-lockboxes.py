#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    # Initialize a set to keep track of opened boxes
    opened_boxes = set()
    opened_boxes.add(0)  # Start with the first box unlocked

    # Initialize a set to keep track of keys
    keys = set(boxes[0])

    # Iterate through the keys and boxes until no new keys or boxes are found
    while keys:
        # Get a key from the set of keys
        key = keys.pop()

        # If the key corresponds to a box that hasn't been opened yet
        if key < len(boxes) and key not in opened_boxes:
            # Add the box to the set of opened boxes
            opened_boxes.add(key)
            # Add any new keys found in the opened box to the set of keys
            keys.update(boxes[key])

    # If all boxes are opened, return True; otherwise, return False
    return len(opened_boxes) == len(boxes)
