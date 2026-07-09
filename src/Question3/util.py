def second_large(nums):
    large = float('-inf')
    second = float('-inf')

    for i in nums:
        if i > large:
            second = large
            large = i
        elif i != large and i > second:
            second = i

    return second