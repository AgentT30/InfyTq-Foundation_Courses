def merge_sort(num_list):
    l = 0
    r = len(num_list)
    if l == r:
        return num_list
    else:
        mid = (l + r) // 2
        left_list = num_list[:mid]
        right_list = num_list[mid:]

        left_list = merge_sort(left_list)
        right_list = merge_sort(right_list)
        sorted_list = merge(left_list, right_list)

        return sorted_list


def merge(left_list, right_list):
    i = 0
    j = 0
    sorted_list = []

    for i in right_list:
        left_list.append(i)
    return left_list

    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            sorted_list.append(left_list[i])
            i += 1
        else:
            sorted_list.append(right_list[j])
            j += 1

    return sorted_list


num_list = [34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:", num_list)
sorted_list = merge_sort(num_list)
print("After sorting:", sorted_list)
