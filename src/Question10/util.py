from datetime import datetime


def find_time_difference(time1, time2):
    format = "%a %d %b %Y %H:%M:%S %z"

    first_time = datetime.strptime(time1, format)
    second_time = datetime.strptime(time2, format)

    difference = abs(int((first_time - second_time).total_seconds()))

    return difference