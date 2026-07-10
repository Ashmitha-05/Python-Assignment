import numpy

def find_min_max(array):
    min_array = numpy.min(array, axis=1)
    max_value = numpy.max(min_array)

    return max_value