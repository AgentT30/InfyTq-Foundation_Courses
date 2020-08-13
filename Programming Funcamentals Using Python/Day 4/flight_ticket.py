def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    # Write your logic here
    number = 101
    for i in range(no_of_passengers):
        ticket_number = f'{airline}:{source[:3]}:{destination[:3]}:{number}'
        number += 1
        ticket_number_list.append(ticket_number)

    if len(ticket_number_list) < 5:
        return ticket_number_list
    else:
        return ticket_number_list[-5:]


# Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI", "Bangalore", "London", 7))
