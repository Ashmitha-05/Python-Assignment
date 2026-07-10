import util
import py

def test_insert_element():
    lst = [1, 2, 3]
    util.insert_no(lst, 1, 5)
    assert lst == [1, 5, 2, 3]


def test_append_element():
    lst = [1, 2]
    util.append_no(lst, 3)
    assert lst == [1, 2, 3]


def test_remove_element():
    lst = [1, 2, 3]
    util.remove_no(lst, 2)
    assert lst == [1, 3]


def test_sort_list():
    lst = [3, 1, 2]
    util.sort_list(lst)
    assert lst == [1, 2, 3]


def test_pop_element():
    lst = [1, 2, 3]
    util.pop_element(lst)
    assert lst == [1, 2]


def test_reverse_list():
    lst = [1, 2, 3]
    util.reverse_list(lst)
    assert lst == [3, 2, 1]