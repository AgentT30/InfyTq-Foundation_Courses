
def create_largest_number(number_list):
    number_list = sorted(number_list, reverse=True)
    large_number = ""
    for i in number_list:
        large_number += str(i)
    return int(large_number)


number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)
