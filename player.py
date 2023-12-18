class Player: 
    def __init__(self, name: str): 
        self.name = name 
        self.health = 20
        self.mana = 0 

    def add_deck(self, new_deck):
        self.deck = new_deck

    def print_deck(self):
        self.deck.print_card_list()

    def add_hand(self, new_hand):
        self.hand = new_hand
    
    def print_hand(self): 
        self.hand.print_card_list()

    def draw_card(self):
        self.hand.add_card_to_hand(self.deck.get_top_card())

    def print_deck(self):
        print(f"{self.name}'s Deck:")
        for card in self.deck.card_list:
            print(card)

    def print_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand.card_list:
            print(card)