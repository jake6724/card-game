from game_classes.card import Card

class Hand():
    # Unlike deck hand starts with an empty card list. Use player -> draw_card func to add cards 
    def __init__(self):
        self.card_list = []
        self.empty_card = Card("empty",0,0,0,0,"c",0,0,"c",0,0,"l",0)
        self.empty_card.create_description()

    def add_card_to_hand(self, new_card):
        self.card_list.append(new_card)
        self.create_card_vars()

    def check_if_card_in_hand(self, cname):
        # Check if card name matches any card names in hand
        for card in self.card_list:
            if card.name == cname:
                return True 
        return False 

    def remove_card_from_hand(self, card_to_remove: Card):
        # Find and remove card. Add an empty card back to the end of the card list to replace
        for card in self.card_list:
            if card == card_to_remove:
                self.card_list.remove(card)
                self.add_card_to_hand(self.empty_card)
        self.create_card_vars()
    
    def create_card_vars(self):
        if len(self.card_list) == 4:
            self.card1 = self.card_list[0]
            self.card2 = self.card_list[1]
            self.card3 = self.card_list[2]
            self.card4 = self.card_list[3]

    def get_card_by_name(self, card_name):
        for card in self.card_list:
            if card.name == card_name:
                return card

    def print_card_list(self):
        for card in self.card_list:
            print(card)
