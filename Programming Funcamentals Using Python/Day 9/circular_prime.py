def check_prime(number):
    if number == 2:
        return True
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        return True


def rotations(num):
    # remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
    number_list = [num]
    for i in range(len(str(num)) - 1):
        num_to_rotate = str(number_list[-1])
        temp = num_to_rotate[0]
        num_to_rotate = num_to_rotate[1:]
        num_to_rotate += temp
        number_list.append(int(num_to_rotate))
    # print(number_list)
    return number_list
    # Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]


def get_circular_prime_count(limit):
    # remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    count = 0
    num_list = []
    for i in range(limit):
        reverse_list = rotations(i)
        check_if_prime = set()
        for j in reverse_list:
            check_if_prime.add(check_prime(j))
        if len(check_if_prime) == 1 and True in check_if_prime:
            num_list.append(i)
            count += 1
    # print(num_list)
    return count


# Provide different values for limit and test your program
print(get_circular_prime_count(500))
# rotations(17)
# print(check_prime(33))
