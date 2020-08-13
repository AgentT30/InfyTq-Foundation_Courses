# DSA-Tryout
import random


def generate_cards_per_type(card_type):
    list_of_cards = []
    for i in range(2, 11):
        list_of_cards.append(card_type+str(i))
    list_of_cards.append(card_type+"J")
    list_of_cards.append(card_type+"Q")
    list_of_cards.append(card_type+"K")
    list_of_cards.append(card_type+"A")

    return list_of_cards


def generate_card_deck():
    card_deck = []
    temp_list = generate_cards_per_type("C")
    for i in temp_list:
        card_deck.append(i)
    temp_list = generate_cards_per_type("D")
    for i in temp_list:
        card_deck.append(i)
    temp_list = generate_cards_per_type("H")
    for i in temp_list:
        card_deck.append(i)
    temp_list = generate_cards_per_type("S")
    for i in temp_list:
        card_deck.append(i)

    return card_deck


def shuffle_card_deck(cards_list):
    index1 = random.randint(0, 51)
    index2 = random.randint(0, 51)

    cards_list[index1], cards_list[index2] = cards_list[index2], cards_list[index1]

    return cards_list


def sort_cards_of_each_player(card_list):
    return card_list


def allocate_cards_to_players(cards_list):
    players_dict = {
        'player1': [],
        'player2': [],
        'player3': [],
        'player4': []
    }

    for j in range(13):
        players_dict["player1"].append(cards_list.pop(0))
        players_dict["player2"].append(cards_list.pop(0))
        players_dict["player3"].append(cards_list.pop(0))
        players_dict["player4"].append(cards_list.pop(0))

    return players_dict


def prepare_cards():
    cards = generate_card_deck()
    shuffled_cards = shuffle_card_deck(cards)
    player_dict = allocate_cards_to_players(shuffled_cards)
    player1 = sort_cards_of_each_player(player_dict["player1"])
    player2 = sort_cards_of_each_player(player_dict["player2"])
    player3 = sort_cards_of_each_player(player_dict["player3"])
    player4 = sort_cards_of_each_player(player_dict["player4"])
    if "CA" in player1:
        return "Player 1"
    elif "CA" in player2:
        return "Player 2"
    elif "CA" in player3:
        return "Player 3"
    else:
        return "Player 4"


first_player = prepare_cards()
print("The first player is:", first_player)
