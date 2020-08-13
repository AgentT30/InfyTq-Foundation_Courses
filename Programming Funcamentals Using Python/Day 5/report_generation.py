
list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)


def find_more_than_average():
    average = sum(list_of_marks) / len(list_of_marks)
    students_with_more_than_avg = []
    for i in list_of_marks:
        if i > average:
            students_with_more_than_avg.append(i)
    percentage = (len(students_with_more_than_avg)/len(list_of_marks)) * 100
    return percentage


def sort_marks():
    return sorted(list(list_of_marks))


def generate_frequency():
    frequency_of_marks = [0] * 26
    for i in list_of_marks:
        frequency_of_marks[i] += 1
    return frequency_of_marks


print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
