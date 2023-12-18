from card import Card 

class Deck: 
    # Deck starts empty. Cards are added in gen_deck func in game_engine 
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

    
    
