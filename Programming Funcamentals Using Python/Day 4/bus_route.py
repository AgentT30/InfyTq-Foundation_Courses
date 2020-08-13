def calculate(distance, no_of_passengers):
    price_of_fuel = 70
    milage_of_bus = 10
    ticket_price = 80

    money_from_ticket = ticket_price * no_of_passengers
    fuel_required = distance / milage_of_bus
    money_for_fuel = fuel_required * price_of_fuel
    if money_from_ticket > money_for_fuel:
        return (money_from_ticket-money_for_fuel)
    else:
        return -1


# Provide different values for distance, no_of_passenger and test your program
distance = 20
no_of_passengers = 50
print(calculate(distance, no_of_passengers))
