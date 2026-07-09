from util import *
n = int(input())
nums = list(map(int, input().split()))
second = second_large(nums)
print(second)