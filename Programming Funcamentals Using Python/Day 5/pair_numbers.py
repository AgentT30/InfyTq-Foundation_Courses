def find_pairs_of_numbers(num_list, n):
    pairs = 0
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if (num_list[i] + num_list[j]) == n:
                pairs += 1
    return pairs


num_list = [1, 2, 7, 4, 5, 6, 0, 3]
n = 6
print(find_pairs_of_numbers(num_list, n))
