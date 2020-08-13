child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]


def calculate_total_chocolates():
    return sum(chocolates_received)


def reward_child(child_id_rewarded, extra_chocolates):
    if child_id_rewarded in child_id:
        if extra_chocolates < 1:
            print("Extra chocolates is less than 1")
        else:
            chocolates_received[child_id.index(
                child_id_rewarded)] += extra_chocolates
            print(chocolates_received)
    else:
        print("Child id is invalid")


print(calculate_total_chocolates())
# Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20, 2)
