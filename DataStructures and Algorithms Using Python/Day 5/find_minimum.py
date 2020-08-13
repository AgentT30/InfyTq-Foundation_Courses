def find_next_min(num_list, start_index):
    next_min = start_index
    temp = num_list[start_index]
    for i in range(start_index, len(num_list)):
        if num_list[i] < temp:
            next_min = i
            temp = num_list[i]
    return next_min


# Pass different values to the function and test your program
num_list = [10, 2, 100, 67]
start_index = 1
print("Index of the next minimum element is",
      find_next_min(num_list, start_index))
