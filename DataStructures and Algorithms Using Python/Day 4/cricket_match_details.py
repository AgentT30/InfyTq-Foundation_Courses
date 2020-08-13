def find_matches(country_name):
    details = []
    for i in match_list:
        if i.startswith(country_name):
            details.append(i)
    return details


def max_wins():
    output = {
        "CHAM": [],
        "WOR": [],
        "T20": []
    }
    cham_list = []
    t20_list = []
    wor_list = []
    for i in match_list:
        temp_string = i.split(':')
        if "CHAM" in temp_string:
            cham_list.append(i)
        elif "WOR" in temp_string:
            wor_list.append(i)
        else:
            t20_list.append(i)
    print(cham_list)
    print(wor_list)
    print(t20_list)

    print(output)


def find_winner(country1, country2):
    # Remove pass and write your logic here
    pass


# Consider match_list to be a global variable
match_list = ["AUS:CHAM:5:2", "AUS:WOR:2:1", "ENG:WOR:2:0", "IND:T20:5:3",
              "IND:WOR:2:1", "PAK:WOR:2:0", "PAK:T20:5:1", "SA:WOR:2:0", "SA:CHAM:5:1", "SA:T20:5:0"]

# Pass different values to each function and test your program
# print("The match status list details are:")
# print(match_list)
# print()

# print(find_matches("AUS"))
print(max_wins())
