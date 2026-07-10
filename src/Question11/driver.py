import numpy
from util import floor_ceil_rint

array = numpy.array(list(map(float, input().split())))

floor_array, ceil_array, rint_array = floor_ceil_rint(array)

print(floor_array)
print(ceil_array)
print(rint_array)