def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = -1
    # write your logic here
    delivery_rate = 0

    if quantity_ordered > 0:
        if distance_in_kms <= 3:
            delivery_rate = 0
        elif distance_in_kms > 3 and distance_in_kms <= 6:
            delivery_rate = distance_in_kms * 3
        else:
            delivery_rate = distance_in_kms * 6

        if food_type == "N":
            bill_amount = 150 * quantity_ordered + delivery_rate
        else:
            bill_amount = 120 * quantity_ordered + delivery_rate

        return bill_amount
    else:
        return -1


bill_amount = calculate_bill_amount("N", 2, 3)
print(bill_amount)
