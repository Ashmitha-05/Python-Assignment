from src.Question17.util import can_stack


def test_case1():
    blocks = [4, 3, 2, 1, 3, 4]
    assert can_stack(blocks) == "Yes"


def test_case2():
    blocks = [1, 3, 2]
    assert can_stack(blocks) == "No"


def test_case3():
    blocks = [5, 4, 3, 2, 1]
    assert can_stack(blocks) == "Yes"


def test_case4():
    blocks = [1, 2, 3, 4, 5]
    assert can_stack(blocks) == "Yes"


def test_case5():
    blocks = [2, 2, 2, 2]
    assert can_stack(blocks) == "Yes"