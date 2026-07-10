from collections import namedtuple


def calculate_average(n, columns):
    Student = namedtuple("Student", columns)

    total = 0

    for i in range(n):
        student = Student(*input().split())
        total += int(student.MARKS)

    return total / n