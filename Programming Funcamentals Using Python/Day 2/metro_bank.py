def calculate_loan(account_number, salary, account_balance, loan_type, loan_amount_expected, customer_emi_expected):
    eligible_loan_amount = 0
    bank_emi_expected = 0
    eligible_loan_amount = 0
    account_number = str(account_number)
    if (account_number[0] == "1" and len(account_number) == 4):
        if account_balance > 100000:
            if salary > 25000 and loan_type == "Car" and loan_amount_expected <= 500000 and customer_emi_expected <= 36:
                eligible_loan_amount = 500000
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.",
                      eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:", customer_emi_expected)
            elif salary > 50000 and loan_type == "House" and loan_amount_expected <= 6000000 and customer_emi_expected <= 60:
                eligible_loan_amount = 6000000
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.",
                      eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:", customer_emi_expected)
            elif salary > 75000 and loan_type == "Business" and loan_amount_expected <= 7500000 and customer_emi_expected <= 84:
                eligible_loan_amount = 7500000
                print("Account number:", account_number)
                print("The customer can avail the amount of Rs.",
                      eligible_loan_amount)
                print("Eligible EMIs :", bank_emi_expected)
                print("Requested loan amount:", loan_amount_expected)
                print("Requested EMI's:", customer_emi_expected)
            else:
                print("The customer is not eligible for the loan")
        else:
            print("Insufficient account balance")

    else:
        print("Invalid account number")


calculate_loan(1001, 40000, 250000, "Car", 300000, 30)
