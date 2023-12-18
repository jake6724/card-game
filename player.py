import textwrap

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

    def pretty_print_hand(self):
        # Create shorter var names for card info so it can be formatted. 
        c1n = self.hand.card_list[0].name
        c1pc = self.hand.card_list[0].placement_cost
        c1hp = self.hand.card_list[0].health
        c1desc1 = "Card info here"
        c1desc2 = "on multiple lines"

        c2n = self.hand.card_list[1].name
        c2pc = self.hand.card_list[1].placement_cost
        c2hp = self.hand.card_list[1].health
        c2desc1 = "Card info here"
        c2desc2 = "on multiple lines"

        c3n = self.hand.card_list[2].name
        c3pc = self.hand.card_list[2].placement_cost
        c3hp = self.hand.card_list[2].health
        c3desc1 = "Card info here"
        c3desc2 = "on multiple lines"

        c4n = self.hand.card_list[3].name
        c4pc = self.hand.card_list[3].placement_cost
        c4hp = self.hand.card_list[3].health
        c4desc1 = "Card info here"
        c4desc2 = "on multiple lines"

        print(textwrap.dedent(f"""   
            {self.name}'s hand:                   
            +---------------------+   +---------------------+   +---------------------+   +---------------------+
            |{c1n:^21}|   |{c2n:^21}|   |{c3n:^21}|   |{c4n:^21}|                                     
            |                     |   |                     |   |                     |   |                     |
            |PC:{c1pc:<18}|   |PC:{c2pc:<18}|   |PC:{c3pc:<18}|   |PC:{c4pc:<18}|
            |HP:{c1hp:<18}|   |HP:{c2hp:<18}|   |HP:{c3hp:<18}|   |HP:{c4hp:<18}|
            |                     |   |                     |   |                     |   |                     |
            |                     |   |                     |   |                     |   |                     |
            |{c1desc1:^21}|   |{c2desc1:^21}|   |{c3desc1:^21}|   |{c4desc1:^21}|
            |{c1desc2:^21}|   |{c2desc2:^21}|   |{c3desc2:^21}|   |{c4desc2:^21}|
            |                     |   |                     |   |                     |   |                     |
            +---------------------+   +---------------------+   +---------------------+   +---------------------+
            """))