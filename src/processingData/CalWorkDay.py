import pandas
import holidays
import calendar
from datetime import date, datetime

# Take a date and return a list containing all off-days in that month.

# Given a date, return if its business day
def isWorkDay(date):
    is_work_day = False

    if date.weekday() <= 4:
        is_work_day = True

    us_holidays = holidays.UnitedStates()

    if date in us_holidays:
        is_work_day = False

    return is_work_day


# Given a date and return a list containing all off-day in that month in datetime.date format.
def offDayInMonth(_date):
    month = _date.month
    year = _date.year

    if calendar.isleap(year):
        last_day_list = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        last_day_list = [31,28,31,30,31,30,31,31,30,31,30,31]

    off_day_list = []

    for day in range(1,last_day_list[month-1]+1):
        one_date = date(year=year, month=month, day=day)
        if not isWorkDay(one_date):
            off_day_list.append(one_date)

    return off_day_list


if __name__ == "__main__":

    today = date.today()
    print offDayInMonth(today)