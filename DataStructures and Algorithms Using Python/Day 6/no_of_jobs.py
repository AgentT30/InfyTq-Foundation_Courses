def find_maximum_activities(activity_list, start_time_list, finish_time_list):

    for i in range(len(start_time_list)):
        for j in range(0, len(start_time_list)-i-1):
            if start_time_list[j] > start_time_list[j+1]:
                start_time_list[j], start_time_list[j +
                                                    1] = start_time_list[j+1], start_time_list[j]
                activity_list[j], activity_list[j +
                                                1] = activity_list[j+1], activity_list[j]
                finish_time_list[j], finish_time_list[j +
                                                      1] = finish_time_list[j+1], finish_time_list[j]
    print(activity_list)
    print(start_time_list)
    print(finish_time_list)
    i = 0
    ans = []
    ans.append(activity_list[i])
    for j in range(len(finish_time_list)):
        if start_time_list[j] > finish_time_list[i]:
            ans.append(activity_list[j])
            i = j

    return ans


# Pass different values to the function and test your program
activity_list = [11, 12, 32, 44, 53, 62]
start_time_list = [12, 14, 21, 31, 16, 18]
finish_time_list = [20, 16, 25, 35, 17, 20]

print("Activities:", activity_list)
print("Start time of the activities:", start_time_list)
print("Finishing time of the activities:", finish_time_list)

result = find_maximum_activities(
    activity_list, start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:", result)
