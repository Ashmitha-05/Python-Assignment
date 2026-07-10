from util import find_happiness

n, m = map(int, input().split())

array = list(map(int, input().split()))

like_set = set(map(int, input().split()))
dislike_set = set(map(int, input().split()))

print(find_happiness(array, like_set, dislike_set))