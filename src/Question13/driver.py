import numpy
from util import find_determinant

n = int(input())

matrix = []

for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

matrix = numpy.array(matrix)

print(find_determinant(matrix))