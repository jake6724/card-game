from game_classes.lane import Lane
from game_classes.card import Card
from game_classes.player import Player
import time 

class GameBoard:
    def __init__(self): 
        self.empty_lane_card = Card("empty",0,0,0,0,"n",0,0,"n",0,"n",0,0,"n")
        self.empty_lane_card.create_description()
        self.lane_list = [Lane(1, self.empty_lane_card), Lane(2, self.empty_lane_card), Lane(3, self.empty_lane_card), 
                        Lane(4, self.empty_lane_card), Lane(5, self.empty_lane_card), Lane(6, self.empty_lane_card),
                        Lane(7, self.empty_lane_card), Lane(8, self.empty_lane_card)] 
        # Ease of access vars 
        self.lane1 = self.lane_list[0]
        self.lane2 = self.lane_list[1]
        self.lane3 = self.lane_list[2]
        self.lane4 = self.lane_list[3]
        self.lane5 = self.lane_list[4]
        self.lane6 = self.lane_list[5]
        self.lane7 = self.lane_list[6]
        self.lane8 = self.lane_list[7]

        self.active_card_list = []

    def add_to_active_cards(self, card_to_add):
        self.active_card_list.append(card_to_add)

    def get_card_priority(self, card):
        return card.priority

    def sort_active_cards(self):
        self.active_card_list.sort(key= self.get_card_priority)
        print("Log: Cards sorted")

    def run_card_combat_actions(self, card: Card, p1: Player, p2: Player):
        # Order of operations for attacking 
        # swap
        # card damage
        # player damage 

        # CHECK IF LOWER LANE OR UPPER LANE AND THEN USE THAT TO GET TARGET CARD UGH 
        card_target = self.get_lane_by_number(card.lane_num + 4).active_card
        
        player_target = p1 if card.player == p2 else p2 # double check this 

        # Determine whether to do repeat or finale moves
        if card.counter == card.end_turn:
            # Add checks to see if even needed based on damage/ swap info? 
            if card.finale_card_target == "c":
                


    def update(self):
        for card in self.active_card_list():
            if card.health <= 0:
                self.remove_active_card(card)

            if card.counter > card.end_turn: # Possible problem area 
                self.remove_active_card(card)

    def remove_active_card(self, card):
        # Reset card's lane to empty
        lane = self.get_lane_by_number(card.lane)
        self.reset_lane(lane)
        # Remove card from active cards list
        self.active_card_list.remove(card)
        # Delete the card object?
        # del card 

    def add_card_to_lane(self, new_card: Card):
        for lane in self.lane_list:
            if lane.number == new_card.lane_num:
                lane.set_active_card(new_card)
    
    def reset_lane(self, lane: Lane):
        lane.active_card = self.empty_lane_card

    def get_lane_by_number(self, lane_num: int):
        match lane_num:
            case 1: return self.lane1
            case 2: return self.lane2
            case 3: return self.lane3
            case 4: return self.lane4
            case 5: return self.lane5
            case 6: return self.lane6
            case 7: return self.lane7
            case 8: return self.lane8
    
    def print_active_card_list(self):
        print("Gameboard Active Card List:")
        for card in self.active_card_list:
            print(card)
        time.sleep(2)

    def display_gameboard(self): 
        # TODO: Somehow it cant display card data only when the lane is empty............
        print(f"""   
                Gameboard:
                X===================================X   X===================================X   X===================================X   X===================================X
                |{self.lane5.active_card.name:^35}|   |{self.lane6.active_card.name:^35}|   |{self.lane7.active_card.name:^35}|   |{self.lane8.active_card.name:^35}|
                |                                   |   |                                   |   |                                   |   |                                   |    
                |{self.lane5.active_card.desc_mana:^35}|   |{self.lane6.active_card.desc_mana:^35}|   |{self.lane7.active_card.desc_mana:^35}|   |{self.lane8.active_card.desc_mana:^35}|
                |{self.lane5.active_card.desc_health:^35}|   |{self.lane6.active_card.desc_health:^35}|   |{self.lane7.active_card.desc_health:^35}|   |{self.lane8.active_card.desc_health:^35}|
                |{self.lane5.active_card.desc_counter:^35}|   |{self.lane6.active_card.desc_counter:^35}|   |{self.lane7.active_card.desc_counter:^35}|   |{self.lane8.active_card.desc_counter:^35}|         
                |                                   |   |                                   |   |                                   |   |                                   |         
                |{self.lane5.active_card.desc_each:^35}|   |{self.lane6.active_card.desc_each:^35}|   |{self.lane7.active_card.desc_each:^35}|   |{self.lane8.active_card.desc_each:^35}|         
                |{self.lane5.active_card.desc_repeat_card_damage:^35}|   |{self.lane6.active_card.desc_repeat_card_damage:^35}|   |{self.lane7.active_card.desc_repeat_card_damage:^35}|   |{self.lane8.active_card.desc_repeat_card_damage:^35}|         
                |{self.lane5.active_card.desc_repeat_player_damage:^35}|   |{self.lane6.active_card.desc_repeat_player_damage:^35}|   |{self.lane7.active_card.desc_repeat_player_damage:^35}|   |{self.lane8.active_card.desc_repeat_player_damage:^35}|         
                |{self.lane5.active_card.desc_repeat_swap:^35}|   |{self.lane6.active_card.desc_repeat_swap:^35}|   |{self.lane7.active_card.desc_repeat_swap:^35}|   |{self.lane8.active_card.desc_repeat_swap:^35}|         
                |                                   |   |                                   |   |                                   |   |                                   |         
                |{self.lane5.active_card.desc_finale:^35}|   |{self.lane6.active_card.desc_finale:^35}|   |{self.lane7.active_card.desc_finale:^35}|   |{self.lane8.active_card.desc_finale:^35}|         
                |{self.lane5.active_card.desc_finale_card_damage:^35}|   |{self.lane6.active_card.desc_finale_card_damage:^35}|   |{self.lane7.active_card.desc_finale_card_damage:^35}|   |{self.lane8.active_card.desc_finale_card_damage:^35}|         
                |{self.lane5.active_card.desc_finale_player_damage:^35}|   |{self.lane6.active_card.desc_finale_player_damage:^35}|   |{self.lane7.active_card.desc_finale_player_damage:^35}|   |{self.lane8.active_card.desc_finale_player_damage:^35}|         
                |{self.lane5.active_card.desc_finale_swap:^35}|   |{self.lane6.active_card.desc_finale_swap:^35}|   |{self.lane7.active_card.desc_finale_swap:^35}|   |{self.lane8.active_card.desc_finale_swap:^35}|         
                X===================================X   X===================================X   X===================================X   X===================================X
                                Lane 5                                  Lane 6                                  Lane 7                                Lane 8               
                =============================================================================================================================================================
                                Lane 1                                  Lane 2                                  Lane 3                                Lane 4               
                X===================================X   X===================================X   X===================================X   X===================================X
                |{self.lane1.active_card.name:^35}|   |{self.lane2.active_card.name:^35}|   |{self.lane3.active_card.name:^35}|   |{self.lane4.active_card.name:^35}|
                |                                   |   |                                   |   |                                   |   |                                   |    
                |{self.lane1.active_card.desc_mana:^35}|   |{self.lane2.active_card.desc_mana:^35}|   |{self.lane3.active_card.desc_mana:^35}|   |{self.lane4.active_card.desc_mana:^35}|
                |{self.lane1.active_card.desc_health:^35}|   |{self.lane2.active_card.desc_health:^35}|   |{self.lane3.active_card.desc_health:^35}|   |{self.lane4.active_card.desc_health:^35}|   
                |{self.lane1.active_card.desc_counter:^35}|   |{self.lane2.active_card.desc_counter:^35}|   |{self.lane3.active_card.desc_counter:^35}|   |{self.lane4.active_card.desc_counter:^35}|      
                |                                   |   |                                   |   |                                   |   |                                   |         
                |{self.lane1.active_card.desc_each:^35}|   |{self.lane2.active_card.desc_each:^35}|   |{self.lane3.active_card.desc_each:^35}|   |{self.lane4.active_card.desc_each:^35}|         
                |{self.lane1.active_card.desc_repeat_card_damage:^35}|   |{self.lane2.active_card.desc_repeat_card_damage:^35}|   |{self.lane3.active_card.desc_repeat_card_damage:^35}|   |{self.lane4.active_card.desc_repeat_card_damage:^35}|         
                |{self.lane1.active_card.desc_repeat_player_damage:^35}|   |{self.lane2.active_card.desc_repeat_player_damage:^35}|   |{self.lane3.active_card.desc_repeat_player_damage:^35}|   |{self.lane4.active_card.desc_repeat_player_damage:^35}|         
                |{self.lane1.active_card.desc_repeat_swap:^35}|   |{self.lane2.active_card.desc_repeat_swap:^35}|   |{self.lane3.active_card.desc_repeat_swap:^35}|   |{self.lane4.active_card.desc_repeat_swap:^35}|         
                |                                   |   |                                   |   |                                   |   |                                   |         
                |{self.lane1.active_card.desc_finale:^35}|   |{self.lane2.active_card.desc_finale:^35}|   |{self.lane3.active_card.desc_finale:^35}|   |{self.lane4.active_card.desc_finale:^35}|         
                |{self.lane1.active_card.desc_finale_card_damage:^35}|   |{self.lane2.active_card.desc_finale_card_damage:^35}|   |{self.lane3.active_card.desc_finale_card_damage:^35}|   |{self.lane4.active_card.desc_finale_card_damage:^35}|         
                |{self.lane1.active_card.desc_finale_player_damage:^35}|   |{self.lane2.active_card.desc_finale_player_damage:^35}|   |{self.lane3.active_card.desc_finale_player_damage:^35}|   |{self.lane4.active_card.desc_finale_player_damage:^35}|         
                |{self.lane1.active_card.desc_finale_swap:^35}|   |{self.lane2.active_card.desc_finale_swap:^35}|   |{self.lane3.active_card.desc_finale_swap:^35}|   |{self.lane4.active_card.desc_finale_swap:^35}|         
                X===================================X   X===================================X   X===================================X   X===================================X
        """)