import numpy
from util import find_mean_var_std

rows, columns = map(int, input().split())

array = []

for i in range(rows):
    values = list(map(int, input().split()))
    array.append(values)

array = numpy.array(array)

mean, var, std = find_mean_var_std(array)

print(mean)
print(var)
print(std)