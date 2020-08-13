
def find_leap_years(given_year):
    list_of_leap_years = [given_year]

    for i in range(15):
        list_of_leap_years.append(list_of_leap_years[i] + 4)

    return list_of_leap_years


list_of_leap_years = find_leap_years(2000)
print(list_of_leap_years)
