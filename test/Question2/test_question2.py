import util

def test_calculate_average():
    student_dict = {
        "Krishna": [67.0, 68.0, 69.0],
        "Malika": [52.0, 56.0, 60.0]
    }

    assert util.calculate_average(student_dict, "Malika") == 56.0


def test_calculate_average_single_student():
    student_dict = {
        "Ash": [90.0, 80.0, 70.0]
    }

    assert util.calculate_average(student_dict, "Ash") == 80.0
