import datetime


def solution(a, b):
    date = datetime.date(2016, a, b)
    weekdays = ["MON","TUE","WED","THU","FRI","SAT", "SUN"]
    return weekdays[date.weekday()]

