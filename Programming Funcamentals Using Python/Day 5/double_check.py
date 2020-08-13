def check_double(number):
    if (len(str(number)) == (len(str(number*2)))) and len(set(str(number)) - set(str(number * 2))) == 0:
        return True
    else:
        return False


# Provide different values for number and test your program
print(check_double(125874))
