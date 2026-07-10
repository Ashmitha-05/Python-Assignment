from util import find_time_difference


def test_case1():
    assert find_time_difference(
        "Sun 10 May 2015 13:54:36 -0700",
        "Sun 10 May 2015 13:54:36 -0000"
    ) == 25200


def test_case2():
    assert find_time_difference(
        "Sat 02 May 2015 19:54:36 +0530",
        "Fri 01 May 2015 13:54:36 -0000"
    ) == 88200


def test_same_time():
    assert find_time_difference(
        "Mon 01 Jan 2024 10:00:00 +0000",
        "Mon 01 Jan 2024 10:00:00 +0000"
    ) == 0