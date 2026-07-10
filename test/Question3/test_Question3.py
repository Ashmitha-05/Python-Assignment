from src.Question3 import util

def test_find_second_large():
    nums = [2, 3, 6, 6, 5]
    assert util.find_second_large(nums) == 5


def test_find_second_large_negative():
    nums = [-2, -1, -5]
    assert util.find_second_large(nums) == -2


def test_find_second_large_duplicates():
    nums = [10, 10, 8, 7]
    assert util.find_second_large(nums) == 8