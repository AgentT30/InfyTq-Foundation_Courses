def validate_name(name):
    # Start writing your code here
    if len(name) > 0 and len(name) <= 15 and name.isalpha():
        return True
    else:
        return False


def validate_phone_no(phno):
    # Start writing your code here
    count = 1
    if len(phno) == 10 and phno.isdigit():
        for i in range(len(phno)):
            for j in range(i+1, len(phno)):
                if phno[i] == phno[j]:
                    count += 1
            break
        if count < 10:
            return True
        else:
            return False
    else:
        return False


def validate_email_id(email_id):
    # Start writing your code here
    at_symbol = 0
    dot_com = 0
    for i in email_id:
        if i == "@":
            at_symbol += 1
    if email_id.index('.com') > 7:
        if at_symbol == 1:
            if email_id.endswith('gmail.com') or email_id.endswith('yahoo.com') or email_id.endswith('hotmail.com'):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def validate_all(name, phone_no, email_id):
    if not validate_name(name):
        print("Invalid Name")
    elif not validate_email_id(email_id):
        print("Invalid email id")
    elif not validate_phone_no(phone_no):
        print("Invalid phone number")
    else:
        print("All the details are valid")


# Provide different values for name, phone_no and email_id and test your program
# validate_all("Tina", "9994599998", "tina@yahoo.com")
# print(validate_email_id('tina@yahoo.com'))

print(validate_email_id('tom.com@gmail.com'))
