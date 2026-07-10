import numpy

def floor_ceil_rint(array):
    floor_array = numpy.floor(array)
    ceil_array = numpy.ceil(array)
    rint_array = numpy.rint(array)

    return floor_array, ceil_array, rint_array