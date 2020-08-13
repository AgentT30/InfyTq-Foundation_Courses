def find_number_of_platforms(arrival_time_list, departure_time_list):
    arrival_time_list.sort()
    departure_time_list.sort()
    n = len(arrival_time_list)
    plat_needed = 1
    result = 1
    i = 1
    j = 0

    while (i < n and j < n):
        if (arrival_time_list[i] <= departure_time_list[j]):
            plat_needed += 1
            i += 1
        elif (arrival_time_list[i] > departure_time_list[j]):
            plat_needed -= 1
            j += 1

        if (plat_needed > result):
            result = plat_needed

    return result


# Pass different values to the function and test your program
arrival_time_list = [800, 810, 900, 740, 1200, 1400]
departure_time_list = [2300, 2000, 1200, 1349, 1500, 2120]
print("The arrival time of the trains:", arrival_time_list)
print("The departure time of the trains:", departure_time_list)
print("Minimum number of platforms required :",
      find_number_of_platforms(arrival_time_list, departure_time_list))
