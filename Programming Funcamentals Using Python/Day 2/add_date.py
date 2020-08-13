# PF-Tryout

def generate_next_date(day, month, year):
    # Start writing your code here
    months30 = [4, 6, 9, 11]
    months31 = [1, 3, 5, 7, 8, 10, 12]

    if day
    if day == 30:
        if month in months31:
            next_day = day + 1
            next_month = month
            next_year = year
        elif month not in months31:
            next_day = 1
            next_month = month + 1
            next_year = year
        else:

    print(next_day, "-", next_month, "-", next_year)


generate_next_date(30, 6, 2015)
