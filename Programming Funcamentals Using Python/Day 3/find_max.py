def find_max(num1, num2):
    max_num = -1
    # Write your logic here.
    num_list = []
    if num1 >= num2:
        return max_num
    for i in range(num1, num2+1):
        i = str(i)
        if len(i) == 2:
            if (int(i[0]) + int(i[1])) % 3 == 0:
                if int(i) % 5 == 0:
                    num_list.append(i)
    if len(max_num) > 0:
        max_num = int(num_list[-1])
    return max_num


# Provide different values for num1 and num2 and test your program.
max_num = find_max(2, 14)
print(max_num)
