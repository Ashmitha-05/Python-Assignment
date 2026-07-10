from src.Question5.util import merge_the_tools


def test_case1(capsys):
    merge_the_tools("AABCAAADA", 3)
    captured = capsys.readouterr()
    assert captured.out == "AB\nCA\nAD\n"


def test_case2(capsys):
    merge_the_tools("AAAAAA", 2)
    captured = capsys.readouterr()
    assert captured.out == "A\nA\nA\n"


def test_case3(capsys):
    merge_the_tools("ABCDEFGH", 2)
    captured = capsys.readouterr()
    assert captured.out == "AB\nCD\nEF\nGH\n"


def test_case4(capsys):
    merge_the_tools("BBBB", 4)
    captured = capsys.readouterr()
    assert captured.out == "B\n"


def test_case5(capsys):
    merge_the_tools("ABCABC", 3)
    captured = capsys.readouterr()
    assert captured.out == "ABC\nABC\n"