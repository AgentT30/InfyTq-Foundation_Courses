import math


def factorial2(number):
    number = int(number)
    return math.factorial(number)


def find_strong_numbers(num_list):

    strong_num = []
    for i in num_list:
        strong = 0
        i_str = str(i)
        for j in i_str:
            strong += factorial2(j)
        if strong == i:
            strong_num.append(i)
    return strong_num


num_list = [145, 375, 100, 2, 10]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)
