from itertools import combinations


def find_probability(letters, k):
    all_combinations = list(combinations(letters, k))

    count = 0

    for combination in all_combinations:
        if 'a' in combination:
            count += 1

    probability = count / len(all_combinations)

    return probability