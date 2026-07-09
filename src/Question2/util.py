def add_student(student_dict, student_name, student_mark):
    student_dict[student_name] = student_mark


def calculate_average(student_dict, name):
    total = 0
    count = 0

    if name in student_dict:
        for marks in student_dict[name]:
            count += 1
            total += marks

        return total / count

    return None
