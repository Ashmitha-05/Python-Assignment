from src.Question4.util import mutate_string


def test_case1():
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"


def test_case2():
    assert mutate_string("hello", 0, "H") == "Hello"


def test_case3():
    assert mutate_string("python", 5, "N") == "pythoN"


def test_case4():
    assert mutate_string("apple", 2, "X") == "apXle"


def test_case5():
    assert mutate_string("cat", 1, "o") == "cot"