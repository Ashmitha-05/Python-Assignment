from util import calculate_average

n = int(input())

columns = input().split()

average = calculate_average(n, columns)

print(f"{average:.2f}")