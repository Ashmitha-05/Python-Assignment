from collections import deque


def can_stack(blocks):
    blocks = deque(blocks)

    top = float("inf")

    while blocks:
        if blocks[0] >= blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.pop()

        if current > top:
            return "No"

        top = current

    return "Yes"