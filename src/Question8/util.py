import calendar

def find_day(month, day, year):
    day_number = calendar.weekday(year, month, day)

    days = [
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
        "SUNDAY"
    ]

    return days[day_number]