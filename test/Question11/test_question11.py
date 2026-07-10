import numpy
from src.Question11.util import floor_ceil_rint


def test_case1():
    array = numpy.array([1.1, 2.2, 3.3])

    floor, ceil, rint = floor_ceil_rint(array)

    assert (floor == numpy.array([1., 2., 3.])).all()
    assert (ceil == numpy.array([2., 3., 4.])).all()
    assert (rint == numpy.array([1., 2., 3.])).all()


def test_case2():
    array = numpy.array([5.5, 6.6, 7.7])

    floor, ceil, rint = floor_ceil_rint(array)

    assert (floor == numpy.array([5., 6., 7.])).all()
    assert (ceil == numpy.array([6., 7., 8.])).all()
    assert (rint == numpy.array([6., 7., 8.])).all()


def test_case3():
    array = numpy.array([0.1, 0.9])

    floor, ceil, rint = floor_ceil_rint(array)

    assert (floor == numpy.array([0., 0.])).all()
    assert (ceil == numpy.array([1., 1.])).all()
    assert (rint == numpy.array([0., 1.])).all()


def test_case4():
    array = numpy.array([2.5, 3.5])

    floor, ceil, rint = floor_ceil_rint(array)

    assert (floor == numpy.array([2., 3.])).all()
    assert (ceil == numpy.array([3., 4.])).all()
    assert (rint == numpy.array([2., 4.])).all()


def test_case5():
    array = numpy.array([9.9])

    floor, ceil, rint = floor_ceil_rint(array)

    assert (floor == numpy.array([9.])).all()
    assert (ceil == numpy.array([10.])).all()
    assert (rint == numpy.array([10.])).all()