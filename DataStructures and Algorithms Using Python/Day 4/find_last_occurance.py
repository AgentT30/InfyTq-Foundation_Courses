def last_instance(num_list,  start,  end,  key):
    first = -1
    last = -1

    for i in range(len(num_list)):
        if not num_list[i] == key:
            continue

        if first == -1:
            first = i
        last = i
    return last


num_list = [1, 1, 2, 2, 3, 4, 5, 5, 5, 5]
start = 0
end = len(num_list)-1
key = 5  # Number to be searched
# Pass different values for num_list, start,end and key and test your program
result = last_instance(num_list, start, end, key)

if(result != -1):
    print("The index position of the last occurrence of the number:", result)
else:
    print("Number not found")
