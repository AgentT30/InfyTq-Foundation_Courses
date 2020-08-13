def divisors_of_number(n):
    i = 1
    div_list = []
    while i < n:
        if (n % i == 0):
            div_list.append(i)
        i = i + 1
    return div_list


def check_perfect_number(number):
    # start writing your code here
    divisors = divisors_of_number(number)
    if sum(divisors) == number:
        return True
    else:
        return False


def check_perfectno_from_list(no_list):
    # start writing your code here
    perfect_numbers = []
    for i in no_list:
        if i == 0:
            continue
        if check_perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers


perfectno_list = check_perfectno_from_list([0])
print(perfectno_list)
# divisors(6)
