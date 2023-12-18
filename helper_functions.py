import random
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