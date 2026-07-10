from util import count_words

n = int(input())

words = []

for i in range(n):
    word = input()
    words.append(word)

word_dict = count_words(words)

print(len(word_dict))
print(*word_dict.values())