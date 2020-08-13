def find_factors(num):
    factors = []
    for i in range(2, (num+1)):
        if(num % i == 0):
            factors.append(i)
    return factors


def find_smallest_number(num):
    i = num
    while True:
        if len(find_factors(i))+1 == num:
            return i
        else:
            i += 1


num = 16
print("The number of divisors :", num)
result = find_smallest_number(num)
print("The smallest number having", num, " divisors:", result)
