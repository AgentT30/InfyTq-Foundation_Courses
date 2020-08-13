import random


def find_it(num, element_list):
    total_guess = 0
    low = 0
    high = len(element_list) - 1
    mid = 0

    while low <= high:
        total_guess += 1
        mid = (high + low) // 2
        if element_list[mid] < num:
            low = mid + 1
        elif element_list[mid] > num:
            high = mid - 1
        else:
            return total_guess
    return -1

# Initializes a list with values 1 to n in ascending order and returns it


def initialize_list_of_elements(n):
    list_of_elements = []
    for i in range(1, n+1):
        list_of_elements.append(i)
    return list_of_elements


def play(n):
    elems = initialize_list_of_elements(n)
    rand_num = random.randrange(1, n)
    print(find_it(rand_num, elems))


# Pass different values to play() and observe the output
play(400)
