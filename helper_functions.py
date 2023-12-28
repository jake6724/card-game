import random
import copy
from game_classes.card import Card 


def shuffle_card_list(card_list): 
    random.shuffle(card_list)

    """
    Starting hand MUST have two 1's and two 2's 
    """

# name: str, mana: int, health: int, start_turn: int, end_turn: int, repeat_card_target: str, 
# repeat_card_damage: int, repeat_player_damage: int, repeat_swap_direction: str, 
# repeat_swap_duration: int, finale_card_target: str, finale_card_damage: int, 
# finale_player_damage: int, finale_swap_direction: str
    
def create_new_card(card_data_list):
    new_card = Card(card_data_list[0], card_data_list[1], card_data_list[2], card_data_list[3], card_data_list[4], card_data_list[5], 
                    card_data_list[6], card_data_list[7], card_data_list[8], card_data_list[9], card_data_list[10], card_data_list[11], 
                    card_data_list[12], card_data_list[13])    
    return new_card

def duplicate_cards(card_list): 
    duplicated_cards = [] 
    for card in card_list:
        if int(card.mana) <= 2: 
            card_copy = copy.deepcopy(card)
            duplicated_cards.append(card_copy)
    return duplicated_cards

def append_card_list(card_list_1, card_list_2):
    for card in card_list_2:
        card_list_1.append(card)

    

