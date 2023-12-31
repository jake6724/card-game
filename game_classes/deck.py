from game_classes.card import Card 

class Deck: 
    # Deck starts with no card list, a complete one is given to it by game_engine -> gen_player_decks 
    def __init__(self, card_list):
        self.card_list = card_list 

    def peak_top_card(self):
        return self.card_list[0]

    def get_top_card(self):
        top_card = self.card_list[0]
        self.card_list.remove(top_card)
        return top_card
    
    def remove_card(self, card):
        self.card_list.remove(card)
    
    def top_card_to_bottom(self):
        # Move the first card item to end of list  
        top_card = self.card_list[0]
        self.card_list.append(self.card_list.pop(self.card_list.index(top_card)))

    def add_card_list(self, new_card_list):
        self.card_list = new_card_list

    def get_card_by_number(self, index):
        return self.card_list[index]

    def print_card_list(self):
        for card in self.card_list:
            print(card)

    def __str__(self):
        return f"{self.card_list}"

    
    
