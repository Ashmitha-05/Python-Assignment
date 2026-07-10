from src.Question16.util import count_words


def test_case1():
    words = ["bcdef", "abcdefg", "bcde", "bcdef"]

    assert count_words(words) == {
        "bcdef": 2,
        "abcdefg": 1,
        "bcde": 1
    }


def test_case2():
    words = ["apple", "apple", "apple"]

    assert count_words(words) == {
        "apple": 3
    }


def test_case3():
    words = ["cat", "dog", "cat", "dog", "cat"]

    assert count_words(words) == {
        "cat": 3,
        "dog": 2
    }


def test_case4():
    words = ["a", "b", "c"]

    assert count_words(words) == {
        "a": 1,
        "b": 1,
        "c": 1
    }


def test_case5():
    words = []

    assert count_words(words) == {}