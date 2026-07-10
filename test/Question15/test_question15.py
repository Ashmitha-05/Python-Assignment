from src.Question15.util import find_happiness


def test_case1():
    array = [1, 5, 3]
    like_set = {3, 1}
    dislike_set = {5, 7}

    assert find_happiness(array, like_set, dislike_set) == 1


def test_case2():
    array = [1, 2, 3]
    like_set = {1, 2, 3}
    dislike_set = {4, 5}

    assert find_happiness(array, like_set, dislike_set) == 3


def test_case3():
    array = [4, 5, 6]
    like_set = {1, 2}
    dislike_set = {4, 5}

    assert find_happiness(array, like_set, dislike_set) == -2


def test_case4():
    array = [1, 2, 3, 4]
    like_set = {1, 4}
    dislike_set = {2, 3}

    assert find_happiness(array, like_set, dislike_set) == 0


def test_case5():
    array = [7, 8, 9]
    like_set = {1, 2}
    dislike_set = {3, 4}

    assert find_happiness(array, like_set, dislike_set) == 0