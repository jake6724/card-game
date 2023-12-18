import random
import copy
from card import Card 


def shuffle_card_list(card_list): 
    random.shuffle(card_list)

    """
    Starting hand MUST have two 1's and two 2's 
    """


def create_new_card(card_data_list):
    new_card = Card(card_data_list[0],card_data_list[1],card_data_list[2],card_data_list[3],
                        card_data_list[4],card_data_list[5],card_data_list[6],card_data_list[7],
                        card_data_list[8],card_data_list[9],card_data_list[10])    
    return new_card

def duplicate_cards(card_list):
    duplicated_cards = [] 
    for card in card_list:
        if int(card.placement_cost) <= 3: 
            card_copy = copy.deepcopy(card)
            duplicated_cards.append(card_copy)
    return duplicated_cards

def append_card_list(card_list_1, card_list_2):
    for card in card_list_2:
        card_list_1.append(card)

    

