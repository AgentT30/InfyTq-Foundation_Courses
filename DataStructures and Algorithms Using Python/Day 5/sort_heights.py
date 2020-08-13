def order_heights(student_list, height_list):
    n = len(student_list)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if height_list[j] > height_list[j+1]:
                height_list[j], height_list[j +
                                            1] = height_list[j+1], height_list[j]
                student_list[j], student_list[j +
                                              1] = student_list[j+1], student_list[j]

    return student_list, height_list


# Pass different values to the function and test your program
student_list = ["Santa", "Tris", "Arun", "Rachel", "John"]
height_list = [132.7, 129.2, 135, 130.6, 140]
print("Initial student details :")
print("The students:", student_list)
print("Their heights:", height_list)
print()
result = order_heights(student_list, height_list)
print("After arranging the students in the order of their height:")
print("The students :", result[0])
print("Their heights:", result[1])
