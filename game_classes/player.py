from game_classes.card import Card

class Player: 
    def __init__(self, name: str): 
        self.name = name 
        self.health = 20
        self.mana = int(0) 
        # Additional self.vars that are added below:
        #self.deck
        #self.hand
        #self.lane_list

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    def add_deck(self, new_deck):
        self.deck = new_deck

    def print_deck(self):
        self.deck.print_card_list()

    def draw_card(self):
        self.hand.add_card_to_hand(self.deck.get_top_card())

    def add_mana(self, mana_amount):
        self.mana += mana_amount

    def remove_mana(self, mana_amount):
        self.mana = self.mana - mana_amount

    def clear_mana(self):
        self.mana = 0

    def take_damage(self, damage_amount):
        self.health -= damage_amount

    def print_deck(self):
        self.deck.print_card_list()

    def add_hand(self, new_hand):
        self.hand = new_hand
    
    def print_hand(self): 
        self.hand.print_card_list()

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
        return str(lane_string)
    
    def print_lane_list(self):
        print(f"{self.name}'s Lanes:")
        lane_string = ""
        for lane in self.lane_list:
            lane_string += f"{lane.number} "
        print(lane_string)

    def is_card_in_hand(self, c):
        if self.hand.check_if_card_in_hand(c):
            return True 
        else:
            return False

    def has_enough_mana(self, card):
        if card.mana <= self.mana:
            return True
        else:
            return False

    def is_lane_valid(self, l):
        for lane in self.lane_list:
            if lane.number == l:
                return True 
        return False 

    def update_card_priority(self, c, round_num, card_priority):
        c.add_priority(round_num, card_priority)

    def remove_card_from_hand(self, card_to_remove: Card):
        self.hand.remove_card_from_hand(card_to_remove)

    def get_card_placement_data(self):
        # Wrapper function for get_card_by_name and get_valid_lane_number. 
        # Checks that both return something other than None, before returning both values as a list 
        # Remove mana for card placement if it is valid 

        found_card = self.get_card_by_name()
        # Check that player has enough mana to play card
        if found_card != None:
            if found_card.mana <= self.mana:
                lane_number = self.get_valid_lane_number()
                if lane_number != None:
                    self.remove_mana(found_card.mana)
                    return [found_card, lane_number]
            else:
                print("Not enough mana to play this card!")
        else: 
            print("Invalid card!")

    def get_card_by_name(self, card_name):
        # Input validation handled in Hand class
        return self.hand.get_card_by_name(card_name)
        
    def get_card_by_number(self, card_num):
        return self.hand.get_card_by_number(card_num)
    
    def get_valid_lane_number(self):
        # Get a valid lane number for current player to use in card placement  
        is_lane_valid = False 
        # while is_lane_valid == False:
        lane_to_place_card = input(f"Select Lane (Your lanes: {self.get_lane_list_string()}): ")
        for lane in self.lane_list:
            if str(lane.number) == lane_to_place_card:
                # Check if lane already has a card in it
                if lane.active_card.name == "empty":
                    lane_number = int(lane.number)
                    is_lane_valid = True 
                else: 
                    print("Lane occupied!")
                    return None 
        if is_lane_valid:
            return lane_number
        else:
            print("Lane invalid!") 
            return None

    def get_lane_by_number(self, lane_number_to_get):
        # Assumes input validation has been done by player.get_valid_lane_number
        for lane in self.lane_list:
            if lane.number == lane_number_to_get:
                return lane
            
    def is_lane_occupied(self, lane):
        if lane.active_card.name == "empty":
            return False
        else:
            return True 

    def display_hand(self):
        print(f"""                 ( 1 )                                     ( 2 )                                     ( 3 )                                     ( 4 )
                X===================================X   X===================================X   X===================================X   X===================================X
                |{self.hand.card1.name:^35}|   |{self.hand.card2.name:^35}|   |{self.hand.card3.name:^35}|   |{self.hand.card4.name:^35}|
                |                                   |   |                                   |   |                                   |   |                                   |    
                |{self.hand.card1.desc_mana:^35}|   |{self.hand.card2.desc_mana:^35}|   |{self.hand.card3.desc_mana:^35}|   |{self.hand.card4.desc_mana:^35}|
                |{self.hand.card1.desc_health:^35}|   |{self.hand.card2.desc_health:^35}|   |{self.hand.card3.desc_health:^35}|   |{self.hand.card4.desc_health:^35}|
                |{self.hand.card1.desc_start_end:^35}|   |{self.hand.card2.desc_start_end:^35}|   |{self.hand.card3.desc_start_end:^35}|   |{self.hand.card4.desc_start_end:^35}|         
                |                                   |   |                                   |   |                                   |   |                                   |         
                |{self.hand.card1.desc_each:^35}|   |{self.hand.card2.desc_each:^35}|   |{self.hand.card3.desc_each:^35}|   |{self.hand.card4.desc_each:^35}|         
                |{self.hand.card1.desc_repeat_card_damage:^35}|   |{self.hand.card2.desc_repeat_card_damage:^35}|   |{self.hand.card3.desc_repeat_card_damage:^35}|   |{self.hand.card4.desc_repeat_card_damage:^35}|         
                |{self.hand.card1.desc_repeat_player_damage:^35}|   |{self.hand.card2.desc_repeat_player_damage:^35}|   |{self.hand.card3.desc_repeat_player_damage:^35}|   |{self.hand.card4.desc_repeat_player_damage:^35}|         
                |{self.hand.card1.desc_repeat_swap:^35}|   |{self.hand.card2.desc_repeat_swap:^35}|   |{self.hand.card3.desc_repeat_swap:^35}|   |{self.hand.card4.desc_repeat_swap:^35}|         
                |                                   |   |                                   |   |                                   |   |                                   |         
                |{self.hand.card1.desc_finale:^35}|   |{self.hand.card2.desc_finale:^35}|   |{self.hand.card3.desc_finale:^35}|   |{self.hand.card4.desc_finale:^35}|         
                |{self.hand.card1.desc_finale_card_damage:^35}|   |{self.hand.card2.desc_finale_card_damage:^35}|   |{self.hand.card3.desc_finale_card_damage:^35}|   |{self.hand.card4.desc_finale_card_damage:^35}|         
                |{self.hand.card1.desc_finale_player_damage:^35}|   |{self.hand.card2.desc_finale_player_damage:^35}|   |{self.hand.card3.desc_finale_player_damage:^35}|   |{self.hand.card4.desc_finale_player_damage:^35}|         
                |{self.hand.card1.desc_finale_swap:^35}|   |{self.hand.card2.desc_finale_swap:^35}|   |{self.hand.card3.desc_finale_swap:^35}|   |{self.hand.card4.desc_finale_swap:^35}|         
                X===================================X   X===================================X   X===================================X   X===================================X
            """)
   
        # print(textwrap.dedent(f"""   
        #     """))

