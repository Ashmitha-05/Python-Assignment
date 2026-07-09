from util import mutate_string
word = input()
position, character = input().split()
position = int(position)
result = mutate_string(word, position, character)
print(result)