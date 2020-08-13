def find_factors(num):
    factors = []
    for i in range(2, (num+1)):
        if(num % i == 0):
            factors.append(i)
    return factors


def is_prime(num, i):
    if(i == 1):
        return True
    elif(num % i == 0):
        return False
    else:
        return(is_prime(num, i-1))


def find_largest_prime_factor(list_of_factors):
    list_of_factors = sorted(list_of_factors, reverse=True)
    for i in list_of_factors:
        if is_prime(i, i//2):
            return i


def find_f(num):
    factors = find_factors(num)
    return (find_largest_prime_factor(factors))


def find_g(num):
    g_list = []
    for i in range(num, num+9):
        g_list.append(find_f(i))
    return sum(g_list)


print(find_g(10))
