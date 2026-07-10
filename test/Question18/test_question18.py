from src.Question18.util import find_probability


def test_case1():
    letters = ['a', 'a', 'c', 'd']
    assert round(find_probability(letters, 2), 4) == 0.8333


def test_case2():
    letters = ['a', 'b', 'c']
    assert round(find_probability(letters, 2), 4) == 0.6667


def test_case3():
    letters = ['b', 'c', 'd']
    assert find_probability(letters, 2) == 0.0


def test_case4():
    letters = ['a', 'b']
    assert find_probability(letters, 1) == 0.5


def test_case5():
    letters = ['a', 'a', 'a']
    assert find_probability(letters, 2) == 1.0