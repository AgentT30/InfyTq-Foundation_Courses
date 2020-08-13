def make_change(denomination_list, amount):
    '''Remove pass and implement the Greedy approach to make the change for the amount using the currencies in the denomination list.
    The function should return the total number of notes needed to make the change. If change cannot be obtained for the given amount, then return -1. Return 1 if the amount is equal to one of the currencies available in the denomination list.  '''
    if amount in denomination_list:
        return 1

    ans = []
    i = len(denomination_list) - 1
    while (i >= 0):
        while(amount >= denomination_list[i]):
            amount -= denomination_list[i]
            ans.append(denomination_list[i])
            denomination_list.remove(denomination_list[i])
            break

        i -= 1
    if len(ans) == 0 or not sum(ans) == amount:
        return -1
    else:
        return len(ans)


# Pass different values to the function and test your program
amount = 20
denomination_list = [15, 10, 1]
print(make_change(denomination_list, amount))
