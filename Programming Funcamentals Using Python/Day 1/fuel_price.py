mileage = 12
amount_per_litre = 65
distance_one_way = 96
per_head_cost = 0
divisible_by_five = False

distance = distance_one_way * 2
total_liters = distance / mileage
amount_total = total_liters * amount_per_litre
per_head_cost = amount_total / 4


if per_head_cost % 5 == 0:
    divisible_by_five = True
else:
    divisible_by_five = False

print(per_head_cost)
print(divisible_by_five)
