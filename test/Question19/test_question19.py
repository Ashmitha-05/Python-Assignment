from src.Question19.util import filter_mail


def test_case1():
    emails = [
        "lara@hackerrank.com",
        "brian-23@hackerrank.com",
        "britts_54@hackerrank.com"
    ]

    assert filter_mail(emails) == [
        "lara@hackerrank.com",
        "brian-23@hackerrank.com",
        "britts_54@hackerrank.com"
    ]


def test_case2():
    emails = [
        "abc@xyz.com",
        "abc#xyz.com",
        "john@123.com"
    ]

    assert filter_mail(emails) == [
        "abc@xyz.com",
        "john@123.com"
    ]


def test_case3():
    emails = [
        "user@gmail.c",
        "user@gmail.co",
        "user@gmail.com"
    ]

    assert filter_mail(emails) == [
        "user@gmail.c",
        "user@gmail.co",
        "user@gmail.com"
    ]


def test_case4():
    emails = [
        "abc@abc.123",
        "abc@abc.comm",
        "abc@abc.co"
    ]

    assert filter_mail(emails) == [
        "abc@abc.co"
    ]


def test_case5():
    emails = [
        "abc@gmail.com",
        "@gmail.com",
        "abc@gmail"
    ]

    assert filter_mail(emails) == [
        "abc@gmail.com"
    ]