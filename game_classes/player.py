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

    def add_mana(self, mana_amount):
        self.mana += mana_amount

    def print_deck(self):
        self.deck.print_card_list()

    def add_hand(self, new_hand):
        self.hand = new_hand
    
    def print_hand(self): 
        self.hand.print_card_list()

    def draw_card(self):
        self.hand.add_card_to_hand(self.deck.get_top_card())

    def get_card_placement_data(self):
        # Wrapper function for get_card_by_name and get_valid_lane_number. 
        # Checks that both return something other than None, before returning both values
        card_name = self.get_card_by_name()
        lane_number = self.get_valid_lane_number()

        if card_name != None:
            if lane_number != None:
                return [card_name, lane_number]

    def get_card_by_name(self):
        # Input validation handled in Hand class
        return self.hand.get_card_by_name()
        
    def get_valid_lane_number(self):
        # is_lane_valid = False 
        # # Check that lane is valid for current player 
        # while is_lane_valid == False:
        lane_to_place_card = input(f"Select Lane (Your lanes: {self.get_lane_list_string()}): ")
        for lane in self.lane_list:
            if str(lane.number) == lane_to_place_card:
                lane_number = int(lane.number)
                is_lane_valid = True 
        if is_lane_valid:
            return lane_number
        else:
         print("Lane invalid!") 
         return None

    def add_lane_list(self, new_lane_list):
        self.lane_list = new_lane_list
        self.lane1 = self.lane_list[0]
        self.lane2 = self.lane_list[1]
        self.lane3 = self.lane_list[2]
        self.lane4 = self.lane_list[3]

    def get_lane_list_string(self):
        lane_string = ""
        for lane in self.lane_list:
            lane_string += f"{lane.number} "
        return lane_string
    
    def print_lane_list(self):
        print(f"{self.name}'s Lanes:")
        lane_string = ""
        for lane in self.lane_list:
            lane_string += f"{lane.number} "
        print(lane_string)

    def print_deck(self):
        print(f"{self.name}'s Deck:")
        for card in self.deck.card_list:
            print(card)

    def print_hand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand.card_list:
            print(card)

    def display_hand(self):
        print(f"""   
                {self.name}'s Hand:                   
                X===================================X   X===================================X   X===================================X   X===================================X
                |{self.hand.card1.name:^35}|   |{self.hand.card2.name:^35}|   |{self.hand.card3.name:^35}|   |{self.hand.card4.name:^35}|
                |                                   |   |                                   |   |                                   |   |                                   |    
                |MP:{self.hand.card1.desc_mana:<32}|   |MP:{self.hand.card2.desc_mana:<32}|   |MP:{self.hand.card3.desc_mana:<32}|   |MP:{self.hand.card4.desc_mana:<32}|
                |HP:{self.hand.card1.desc_health:<32}|   |HP:{self.hand.card2.desc_health:<32}|   |HP:{self.hand.card3.desc_health:<32}|   |HP:{self.hand.card4.desc_health:<32}|         
                |                                   |   |                                   |   |                                   |   |                                   |         
                |{self.hand.card1.desc_each:^35}|   |{self.hand.card2.desc_each:^35}|   |{self.hand.card3.desc_each:^35}|   |{self.hand.card4.desc_each:^35}|         
                |{self.hand.card1.desc_card_damage:^35}|   |{self.hand.card2.desc_card_damage:^35}|   |{self.hand.card3.desc_card_damage:^35}|   |{self.hand.card4.desc_card_damage:^35}|         
                |{self.hand.card1.desc_player_damage:^35}|   |{self.hand.card2.desc_player_damage:^35}|   |{self.hand.card3.desc_player_damage:^35}|   |{self.hand.card4.desc_player_damage:^35}|         
                |{self.hand.card1.desc_finale_card_damage:^35}|   |{self.hand.card2.desc_finale_card_damage:^35}|   |{self.hand.card3.desc_finale_card_damage:^35}|   |{self.hand.card4.desc_finale_card_damage:^35}|         
                |                                   |   |                                   |   |                                   |   |                                   |         
                |{self.hand.card1.desc_swap:^35}|   |{self.hand.card2.desc_swap:^35}|   |{self.hand.card3.desc_swap:^35}|   |{self.hand.card4.desc_swap:^35}|         
                |{self.hand.card1.desc_swap_duration:^35}|   |{self.hand.card2.desc_swap_duration:^35}|   |{self.hand.card3.desc_swap_duration:^35}|   |{self.hand.card4.desc_swap_duration:^35}|         
                |                                   |   |                                   |   |                                   |   |                                   |         
                |                                   |   |                                   |   |                                   |   |                                   |         
                X===================================X   X===================================X   X===================================X   X===================================X
            """)
   
        # print(textwrap.dedent(f"""   
        #     """))

