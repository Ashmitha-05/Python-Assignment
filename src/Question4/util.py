def mutate_string(word, position, character):
    new_word = list(word)
    new_word[position] = character
    return "".join(new_word)