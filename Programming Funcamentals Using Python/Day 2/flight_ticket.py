def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost = 0

    total = 37550.0 * no_of_adults + (37550.0 / 3) * no_of_children
    total += (total * 0.07)
    return (total - (total * 0.1))


total_ticket_cost = calculate_total_ticket_cost(3, 1)
print("Total Ticket Cost:", total_ticket_cost)
