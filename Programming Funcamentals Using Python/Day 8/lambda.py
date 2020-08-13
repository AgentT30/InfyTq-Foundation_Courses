def sum_all(function, data):
    lst = []
    for i in data:
        if function(i):
            lst.append(i)    
    return sum(lst)

list_of_nos=[25,26,27,28,29,30,147,187]

greater = lambda x : x > 10

divide = lambda x : x % 10 == 0 and x <= 100

range_of_values = lambda x: x >= 25 and x <= 50


#Use the below given print statements to display the output

print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))