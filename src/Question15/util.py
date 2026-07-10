def find_happiness(array, like_set, dislike_set):
    happiness = 0

    for number in array:
        if number in like_set:
            happiness += 1
        elif number in dislike_set:
            happiness -= 1

    return happiness