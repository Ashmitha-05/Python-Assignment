import numpy
from src.Question14.util import find_mean_var_std


def test_case1():
    array = numpy.array([
        [1, 2],
        [3, 4]
    ])

    mean, var, std = find_mean_var_std(array)

    assert (mean == numpy.array([1.5, 3.5])).all()
    assert (var == numpy.array([1., 1.])).all()
    assert round(std, 11) == 1.11803398875


def test_case2():
    array = numpy.array([
        [2, 2],
        [2, 2]
    ])

    mean, var, std = find_mean_var_std(array)

    assert (mean == numpy.array([2., 2.])).all()
    assert (var == numpy.array([0., 0.])).all()
    assert std == 0.0


def test_case3():
    array = numpy.array([
        [1, 3],
        [5, 7]
    ])

    mean, var, std = find_mean_var_std(array)

    assert (mean == numpy.array([2., 6.])).all()
    assert (var == numpy.array([4., 4.])).all()
    assert round(std, 2) == 2.24


def test_case4():
    array = numpy.array([
        [10, 20],
        [30, 40]
    ])

    mean, var, std = find_mean_var_std(array)

    assert (mean == numpy.array([15., 35.])).all()
    assert (var == numpy.array([100., 100.])).all()
    assert round(std, 2) == 11.18


def test_case5():
    array = numpy.array([
        [5, 5],
        [10, 10]
    ])

    mean, var, std = find_mean_var_std(array)

    assert (mean == numpy.array([5., 10.])).all()
    assert (var == numpy.array([6.25, 6.25])).all()
    assert round(std, 2) == 2.50