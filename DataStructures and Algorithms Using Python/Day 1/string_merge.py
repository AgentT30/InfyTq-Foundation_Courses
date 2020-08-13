def merge_list(list1, list2):
    merged_data = ""
    # write your logic here
    list2.reverse()
    resultant_data = []
    for i in list1:
        if i == None:
            merged_data = list2[0]
        elif list2[0] == None:
            merged_data = i
        else:
            merged_data = i + list2[0]
        list2 = list2[1:]
        resultant_data.append(merged_data)
    resultant_data = " ".join(resultant_data)
    return resultant_data


# Provide different values for the variables and test your program
list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']
merged_data = merge_list(list1, list2)
print(merged_data)


#['n', 'le', None, 'ay', 'eps', 'e', 'tor', 'y']
