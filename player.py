class Player: 
    def __init__(self, name: str): 
        self.name = name 
        self.health = 20
        self.mana = 0 
        # Additional self.vars that are added below:
        #self.deck
        #self.hand
        #self.lane_list

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

    def add_lane_list(self, new_lane_list):
        self.lane_list = new_lane_list
        self.lane1 = self.lane_list[0]
        self.lane2 = self.lane_list[1]
        self.lane3 = self.lane_list[2]
        self.lane4 = self.lane_list[3]

    def print_lane_list(self):
        print(f"{self.name}'s Lanes:")
        for lane in self.lane_list:
            print(lane)

    def print_deck(self):
        print(f"{self.name}'s Deck:")
        for card in self.deck.card_list:
            print(card)

    def print_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand.card_list:
            print(card)
