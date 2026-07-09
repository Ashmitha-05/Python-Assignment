from util import *

n = int(input())

student_dict = {}

for i in range(n):
    student_details = input().split(" ")
    student_name = student_details[0]
    student_mark = list(map(float, student_details[1:]))

    add_student(student_dict, student_name, student_mark)

name = input()

average = calculate_average(student_dict, name)

if average is not None:
    print(f"{average:.2f}")
