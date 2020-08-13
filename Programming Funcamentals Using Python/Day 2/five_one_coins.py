
def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    five_needed = no_of_five
    total_five = 5 * no_of_five
    one_needed = rupees_to_make - total_five
    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    print("No. of Five needed :", five_needed)
    print("No. of One needed  :", one_needed)
    # print(-1)


make_amount(11, 2, 11)
