menu = ('Veg Roll', 'Noodles', 'Fried Rice', 'Soup')
quantity_available = [2, 200, 3, 0]


def place_order(*item_tuple):
    j = 0
    for i in range(0, len(item_tuple), 2):
        if item_tuple[i] in menu:
            if check_quantity_available(j, item_tuple[i+1]):
                print(f"{item_tuple[i]} is available")
            else:
                print(f"{item_tuple[i]} stock is over")
            j += 1
        else:
            print(f"{item_tuple[i]} is not available")


def check_quantity_available(index, quantity_requested):
    if quantity_available[index] <= quantity_requested:
        quantity_available[index] -= quantity_requested
        return True
    else:
        return False


place_order("Veg Roll", 2, "Noodles", 2)
place_order("Soup", 1, "Veg Roll", 2, "Fried Rice1", 1)
place_order("Fried Rice", 2, "Soup", 1)
