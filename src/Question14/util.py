import numpy

def find_mean_var_std(array):
    mean = numpy.mean(array, axis=1)
    var = numpy.var(array, axis=0)
    std = numpy.std(array)

    return mean, var, std