from util import find_probability

n = int(input())

letters = input().split()

k = int(input())

print(find_probability(letters, k))