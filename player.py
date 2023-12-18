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
        c1n = self.hand.card1.name
        c1m = self.hand.card1.mana
        c1hp = self.hand.card1.health
        c1de = self.hand.card1.desc_each
        c1dc = self.hand.card1.desc_card_damage
        c1dp = self.hand.card1.desc_player_damage
        c1dfc = self.hand.card1.desc_finale_card_damage
        c1ds = self.hand.card1.desc_swap
        c1dsd = self.hand.card1.desc_swap_duration

        c2n = self.hand.card2.name
        c2m = self.hand.card2.mana
        c2hp = self.hand.card2.health
        c2de = self.hand.card2.desc_each
        c2dc = self.hand.card2.desc_card_damage
        c2dp = self.hand.card2.desc_player_damage
        c2dfc = self.hand.card2.desc_finale_card_damage
        c2ds = self.hand.card2.desc_swap
        c2dsd = self.hand.card2.desc_swap_duration

        c3n = self.hand.card3.name
        c3m = self.hand.card3.mana
        c3hp = self.hand.card3.health
        c3de = self.hand.card3.desc_each
        c3dc = self.hand.card3.desc_card_damage
        c3dp = self.hand.card3.desc_player_damage
        c3dfc = self.hand.card3.desc_finale_card_damage
        c3ds = self.hand.card3.desc_swap
        c3dsd = self.hand.card3.desc_swap_duration

        c4n = self.hand.card4.name
        c4m = self.hand.card4.mana
        c4hp = self.hand.card4.health
        c4de = self.hand.card4.desc_each
        c4dc = self.hand.card4.desc_card_damage
        c4dp = self.hand.card4.desc_player_damage
        c4dfc = self.hand.card4.desc_finale_card_damage
        c4ds = self.hand.card4.desc_swap
        c4dsd = self.hand.card4.desc_swap_duration
        
        print(textwrap.dedent(f"""   
            {self.name}'s hand:                   
            X===================================X   X===================================X   X===================================X   X===================================X
            |{self.hand.card1.name:^35}|   |{c2n:^35}|   |{c3n:^35}|   |{c4n:^35}|
            |                                   |   |                                   |   |                                   |   |                                   |    
            |MP:{c1m:<32}|   |MP:{c2m:<32}|   |MP:{c3m:<32}|   |MP:{c4m:<32}|
            |HP:{c1hp:<32}|   |HP:{c2hp:<32}|   |HP:{c3hp:<32}|   |HP:{c4hp:<32}|         
            |                                   |   |                                   |   |                                   |   |                                   |         
            |{c1de:^35}|   |{c2de:^35}|   |{c3de:^35}|   |{c4de:^35}|         
            |{c1dc:^35}|   |{c2dc:^35}|   |{c3dc:^35}|   |{c4dc:^35}|         
            |{c1dp:^35}|   |{c2dp:^35}|   |{c3dp:^35}|   |{c4dp:^35}|         
            |{c1dfc:^35}|   |{c2dfc:^35}|   |{c3dfc:^35}|   |{c4dfc:^35}|         
            |                                   |   |                                   |   |                                   |   |                                   |         
            |{c1ds:^35}|   |{c2ds:^35}|   |{c3ds:^35}|   |{c4ds:^35}|         
            |{c1dsd:^35}|   |{c2dsd:^35}|   |{c3dsd:^35}|   |{c4dsd:^35}|         
            |                                   |   |                                   |   |                                   |   |                                   |         
            |                                   |   |                                   |   |                                   |   |                                   |         
            X===================================X   X===================================X   X===================================X   X===================================X


            """))

