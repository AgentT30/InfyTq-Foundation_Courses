def swap(num_list, first_index, second_index):
    num_list[first_index], num_list[second_index] = num_list[second_index], num_list[first_index]


def find_next_min(num_list, start_index):
    next_min = 0
    temp = num_list[start_index]
    for i in range(start_index, len(num_list)):
        if num_list[i] < temp:
            next_min = i
            temp = num_list[i]
    return next_min


def selection_sort(num_list):
    # Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    num_list.sort()
    return num_list


# Pass different values to the function and test your program
num_list = [8, 2, 19, 34, 23, 67, 91]
print("Before sorting;", num_list)
selection_sort(num_list)
print("After sorting:", num_list)
