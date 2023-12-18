from card import Card 

class Deck: 
    # Deck starts with no card list, a complete one is given to it by game_engine -> gen_player_decks 
    def __init__(self):
        pass 

    def get_top_card(self):
        top_card = self.card_list[0]
        self.card_list.remove(top_card)
        return top_card

    def add_card_list(self, new_card_list):
        self.card_list = new_card_list

    def print_card_list(self):
        for card in self.card_list:
            print(card)

    def __str__(self):
        return f"{self.card_list}"

    
    
