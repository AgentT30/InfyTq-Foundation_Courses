def find_common_characters(msg1, msg2):
    s1 = set(msg1.replace(" ", ""))
    s2 = set(msg2.replace(" ", ""))

    common_letters = ""
    for i in s1.intersection(s2):
        common_letters += i
    if len(common_letters) > 0:
        return common_letters
    else:
        return -1


# Provide different values for msg1,msg2 and test your program
msg1 = "Python"
msg2 = "python"
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
