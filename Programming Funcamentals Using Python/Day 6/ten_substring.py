def find_ten_substring(num_str):
    try:
        substring = []
        base_value = 0
        for i in range(len(num_str)):
            base_value = int(num_str[i])
            numbers = num_str[i]
            for j in range(i+1, len(num_str)):
                base_value += int(num_str[j])
                numbers += num_str[j]
                if base_value == 10:
                    substring.append(numbers)
        return substring
    except:
        return -1


num_str = "3523014"
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)
