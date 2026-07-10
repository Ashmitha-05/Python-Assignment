import numpy
from src.Question13.util import find_determinant


def test_case1():
    matrix = numpy.array([
        [1.1, 1.1],
        [1.1, 1.1]
    ])

    assert find_determinant(matrix) == 0.0


def test_case2():
    matrix = numpy.array([
        [1, 2],
        [3, 4]
    ])

    assert find_determinant(matrix) == -2.0


def test_case3():
    matrix = numpy.array([
        [2, 0],
        [0, 2]
    ])

    assert find_determinant(matrix) == 4.0


def test_case4():
    matrix = numpy.array([
        [5, 0],
        [0, 5]
    ])

    assert find_determinant(matrix) == 25.0


def test_case5():
    matrix = numpy.array([
        [3, 2],
        [1, 4]
    ])

    assert find_determinant(matrix) == 10.0