from src.Question8 import util


def test_find_day():
    assert util.find_day(8, 5, 2015) == "WEDNESDAY"


def test_find_day_monday():
    assert util.find_day(1, 1, 2024) == "MONDAY"


def test_find_day_sunday():
    assert util.find_day(12, 25, 2022) == "SUNDAY"


def test_find_day_friday():
    assert util.find_day(7, 4, 2025) == "FRIDAY"