def remove_duplicates(value):
    # start writing your code here
    value = list(value)
    # print(value)
    for i in range(len(value)):
        for j in range(i+1, len(value)):
            if value[i] == value[j]:
                value[j] = 0

    for i in value:
        value.remove(0)
    value = value[:-2]
    value = "".join(value)
    return value


print(remove_duplicates("1122334455ababzzz@@@123#*#*"))
