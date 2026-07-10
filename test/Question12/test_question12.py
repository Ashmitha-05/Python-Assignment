import numpy
from src.Question12.util import find_min_max


def test_case1():
    array = numpy.array([
        [2, 5],
        [3, 7],
        [1, 3],
        [4, 0]
    ])

    assert find_min_max(array) == 3


def test_case2():
    array = numpy.array([
        [1, 2],
        [3, 4]
    ])

    assert find_min_max(array) == 3


def test_case3():
    array = numpy.array([
        [5, 5],
        [5, 5]
    ])

    assert find_min_max(array) == 5


def test_case4():
    array = numpy.array([
        [10, 20, 30],
        [40, 50, 60]
    ])

    assert find_min_max(array) == 40


def test_case5():
    array = numpy.array([
        [8, 6],
        [7, 9],
        [5, 4]
    ])

    assert find_min_max(array) == 7