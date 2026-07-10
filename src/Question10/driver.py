from util import find_time_difference

t = int(input())

for i in range(t):
    time1 = input()
    time2 = input()

    print(find_time_difference(time1, time2))