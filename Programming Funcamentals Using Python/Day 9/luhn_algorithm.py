def validate_credit_card_number(card_number):
    # start writing your code here
    double = []
    card_number = str(card_number)
    for i in range(0, len(card_number), 2):
        number_double = int(card_number[i]) * 2
        if number_double > 9:
            number_double = str(number_double)
            double.append(int(number_double[0]) + int(number_double[1]))
        else:
            double.append(int(card_number[i]) * 2)
    double.reverse()
    # print(double)

    num_sum = sum(double)
    # print(num_sum)
    step_2 = []
    for i in range(1, len(card_number), 2):
        step_2.append(int(card_number[i]))
    total_sum = sum(step_2) + num_sum
    if total_sum % 10 == 0:
        return True
    else:
        return False

    # 4539869650133101  #1456734512345698 # #5239512608615007
card_number = 1456734512345698
result = validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
