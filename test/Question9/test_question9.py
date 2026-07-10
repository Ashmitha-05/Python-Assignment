from src.Question8.util import calculate_average

def test_case1():
    data = [
        ["1", "97", "Raymond", "7"],
        ["2", "50", "Steven", "4"],
        ["3", "91", "Adrian", "9"],
        ["4", "72", "Stewart", "5"],
        ["5", "80", "Peter", "6"]
    ]
    assert calculate_average(5, ["ID", "MARKS", "NAME", "CLASS"], data) == 78.0


def test_case2():
    data = [
        ["92", "2", "Calum", "1"],
        ["82", "5", "Scott", "2"],
        ["94", "2", "Jason", "3"],
        ["55", "8", "Glenn", "4"],
        ["82", "2", "Fergus", "5"]
    ]
    assert calculate_average(5, ["MARKS", "CLASS", "NAME", "ID"], data) == 81.0


def test_case3():
    data = [
        ["1", "100", "Alice", "10"]
    ]
    assert calculate_average(1, ["ID", "MARKS", "NAME", "CLASS"], data) == 100.0