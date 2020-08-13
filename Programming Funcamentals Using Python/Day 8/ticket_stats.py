# Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
# Note: flight_no has the following format - "airline_name followed by three digit number
import re
# Global variable
ticket_list = ["AI567:MUM:LON:014", "AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145", "AI077:MUM:CAN:060",
               "SI267:BLR:MUM:148", "AI567:CHE:SIN:015", "AI077:MUM:SIN:050", "AI077:MUM:LON:051", "SI267:MUM:SIN:146"]


def find_passengers_flight(airline_name="AI"):
    # This function finds and returns the number of passengers travelling in the specified airline.
    count = 0
    for i in ticket_list:
        string_list = i.split(":")
        if(string_list[0].startswith(airline_name)):
            count += 1
    return count


def find_passengers_destination(destination):
    # Write the logic to find and return the number of passengers traveling to the specified destination
    count = 0
    for i in ticket_list:
        if (re.search(destination, i)):
            count += 1
    return count


def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    count = {}
    for i in ticket_list:
        string_list = i.split(":")
        count.setdefault(string_list[0], 0)
        count[string_list[0]] = count[string_list[0]]+1

    sort_orders = sorted(count.items(), key=lambda x: x[1], reverse=True)

    passengers_per_flight = []
    for i in count:
        data = str(i) + ":" + str(count.get(i))
        passengers_per_flight.append(data)
    return passengers_per_flight


def sort_passenger_list():
    # Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    per_flight = find_passengers_per_flight()
    empty_list = {}
    for i in per_flight:
        string_list = i.split(":")
        empty_list[string_list[0]] = string_list[1]
    sort_orders = sorted(empty_list.items(), key=lambda x: x[1], reverse=True)
    sorted_list = []
    for i in sort_orders:
        sorted_list.append(str(i[0]) + ":" + str(i[1]))
    return sorted_list


Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())
