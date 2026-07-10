import numpy

def find_determinant(matrix):
    determinant = numpy.linalg.det(matrix)
    return round(determinant, 2)