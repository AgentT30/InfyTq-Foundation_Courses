def max_sum_is(num_list):
    sublist = [[]]
    ans = []
    for i in range(len(num_list) + 1):
        for j in range(i + 1, len(num_list) + 1):
            sub = num_list[i:j]
            sublist.append(sub)
    count = 0
    print(sublist)
    for x in sublist:
        res = all(i < j for i, j in zip(x, x[1:]))
        if res == False:
            sublist[count] = [0]
        count += 1

    for i in sublist:
        ans.append(sum(i))
    return max(ans)


# Pass different values to the function and test your program
num_list = [1, 100, 4, 3, 101, 6, 5]
print("Sum of the maximum sum increasing subsequence is :", max_sum_is(num_list))
