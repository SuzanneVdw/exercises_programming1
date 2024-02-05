def fix_date(string):
    month = string[:2]
    day = string[3:5]
    year = string[6:]
    return f'{year}/{month}/{day}'