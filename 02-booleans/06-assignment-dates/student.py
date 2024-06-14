def is_valid_month(month):
    return 0 < month < 13

def is_leap_year(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)

def has_30_days(month):
    return month == 4 or month == 6 or month == 9 or month == 11

def has_31_days(month):
    return not has_30_days(month) and month != 2

def has_28_days(month, year):
    return month == 2 and not is_leap_year(year)

def has_29_days(month, year):
    return month == 2 and is_leap_year(year)

def is_valid_date(day, month, year):
    return (has_31_days(month) and 1 <= day <= 31) or (has_30_days(month) and 1 <= day <= 30) or (has_29_days(month,year) and 1 <= day <= 29) or (has_28_days(month,year) and 1 <= day <= 28) 