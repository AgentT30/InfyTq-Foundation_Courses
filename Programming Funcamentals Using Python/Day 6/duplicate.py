def find_duplicates(list_of_numbers):
    duplicate_numbers = set
    for i in range(len(list_of_numbers)):
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[i] == list_of_numbers[j]:
                duplicate_numbers.add(list_of_numbers[i])

    return list(duplicate_numbers)


list_of_numbers = [12, 54, 68, 759, 24, 15, 12, 68, 987, 758, 25, 69]
list_of_duplicates = find_duplicates(list_of_numbers)
print(list_of_duplicates)
