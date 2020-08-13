def sum_of_numbers(list_of_num, filter_func=None):
    if filter_func == None:
        return sum(list_of_num)
    else:
        return sum(filter_func(list_of_num))


def even(data):
    even_numbers = []
    for i in data:
        if i % 2 == 0:
            even_numbers.append(i)
    print(even_numbers)
    return even_numbers


def odd(data):
    odd_numbers = []
    for i in data:
        if not (i % 2 == 0):
            odd_numbers.append(i)
    return odd_numbers


sample_data = range(1, 11)

print(sum_of_numbers(sample_data, even))
