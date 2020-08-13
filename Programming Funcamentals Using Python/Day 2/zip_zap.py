def display(num):
    message = ""
    if num % 3 == 0 and num % 5 == 0:
        message += "Zoom"
    elif num % 3 == 0:
        message += "Zip"
    elif num % 5 == 0:
        message += "Zap"
    elif not (num % 3 == 0 and num % 5):
        message += "Invalid"
    else:
        pass
    return message


# Provide different values for num and test your program
message = display(13)
print(message)
