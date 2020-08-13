def arrange_tickets(tickets_list):
    temp_list = [0]
    for i in tickets_list:
        temp_list.append(int(i[1:]))
    # print(temp_list)
    temp_list.sort()
    temp_list2 = []
    for i in range(1, 21):
        if i in temp_list:
            temp_list2.append(i)
        else:
            temp_list2.append("V")
    # print(temp_list2)

    group1 = temp_list2[:10]
    group2 = temp_list2[10:]

    for i in range(len(group1)):
        if group1[i] == "V":
            for j in range(len(group2)):
                if group2[j] == "V":
                    continue
                else:
                    group1[i] = group2[j]
                    group2.remove(group2[j])
                    break

    return group1


tickets_list = ['T20', 'T5', 'T10', 'T1', 'T2',
                'T8', 'T16', 'T17', 'T9', 'T4', 'T12', 'T13', 'T18']
print("Ticket ids of all the available students :")
print(tickets_list)
result = arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
