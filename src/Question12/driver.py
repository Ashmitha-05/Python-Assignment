import numpy
from util import find_min_max

rows, columns = map(int, input().split())

array = []

for i in range(rows):
    values = list(map(int, input().split()))
    array.append(values)

array = numpy.array(array)

print(find_min_max(array))