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
        self.combat_data = [["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""], 
                            ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]]

    def add_to_active_cards(self, card_to_add):
        self.active_card_list.append(card_to_add)
        print(f"Card added to GB Active cards. New list: {self.active_card_list}")

    def get_card_priority(self, card):
        return card.priority

    def sort_active_cards(self):
        self.active_card_list.sort(key= self.get_card_priority)

    def reset_card_turns(self):
        for card in self.active_card_list:
            card.taken_turn = False 

    def run_card_combat_actions(self, card: Card, p1: Player, p2: Player):
        # This function is ONLY responsible for dealing damage to cards and players 

        # Order of operations for attacking: 1. Swap, 2. Card Damage, 3. Player Damage 
        card_target = ""
        card_all_targets = ""
        player_target = None

        # Get targets based on card data 
        if card.player == p1:
            card_target = self.get_lane_by_number(int(card.lane_num) + 4).active_card
            card_all_targets = [self.lane5.active_card, self.lane6.active_card, self.lane7.active_card, self.lane8.active_card]
            player_target = p2
        elif card.player == p2:
            card_target = self.get_lane_by_number(int(card.lane_num) - 4).active_card
            card_all_targets = [self.lane1.active_card, self.lane2.active_card, self.lane3.active_card, self.lane4.active_card]
            player_target = p1

        # Determine whether to do repeat or finale moves
        if card.counter == card.end_turn:
            if card_target.name != "empty":
                if card.finale_card_target == "c":
                    card_target.take_damage(card.finale_card_damage)
                    card.log_finale_card = f"{card.name} dealt {card.finale_card_damage} dmg to {card_target.name}"
                elif card.finale_card_target == "a":
                    for target in card_all_targets:
                        target.take_damage(card.finale_card_damage) 
                    card.log_finale_card = f"{card.name} dealt {card.finale_card_damage} dmg to all enemy cards"
            
            if card.finale_player_damage > 0:
                player_target.take_damage(card.finale_player_damage) 
                card.log_finale_player = f"{card.name} dealt {card.finale_player_damage} dmg to {player_target.name}"

        elif card.counter >= card.start_turn: 
            if card_target.name != "empty":
                if card.repeat_card_target == "c":
                    card_target.take_damage(card.repeat_card_damage)
                    card.log_repeat_card = f"{card.name} dealt {card.repeat_card_damage} dmg to {card_target.name}"
                elif card.repeat_card_target == "a":
                    for target in card_all_targets:
                        target.take_damage(card.repeat_card_damage)
                    card.log_repeat_card = f"{card.name} dealt {card.repeat_card_damage} dmg to all enemy cards"
            
            if card.repeat_player_damage > 0:
                player_target.take_damage(card.repeat_player_damage)
                card.log_repeat_player = f"{card.name} dealt {card.repeat_player_damage} dmg to {player_target.name}"

    def create_combat_log(self):
        # Add data from all active cards 
        for i, card in enumerate(self.active_card_list):
            self.combat_data[i] = [card.log_repeat_swap, card.log_repeat_card, card.log_repeat_player,
                                    card.log_finale_swap, card.log_finale_card, card.log_finale_player]
            
        # Fill in blank data until combat data list is filled
        while len(self.combat_data) != 8:
            self.combat_data.append(["", "", "", "", "", ""])

    def update(self):
        for card in self.active_card_list:
            card.create_description()
            if card.health <= 0:
                self.remove_active_card(card)
                continue # Don't check the next if it already been removed 

            if card.counter > card.end_turn: # Possible problem area 
                self.remove_active_card(card)

        print("GB Updated!")

    def remove_active_card(self, card):
        # Reset card's lane to empty
        lane = self.get_lane_by_number(card.lane_num)
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
        return self.lane_list[(int(lane_num) - 1)]
        # match lane_num:
        #     case 1: return self.lane1
        #     case 2: return self.lane2
        #     case 3: return self.lane3
        #     case 4: return self.lane4
        #     case 5: return self.lane5
        #     case 6: return self.lane6
        #     case 7: return self.lane7
        #     case 8: return self.lane8
    
    def print_active_card_list(self):
        print("Gameboard Active Card List:")
        for card in self.active_card_list:
            print(card)
        time.sleep(2)

    def display_gameboard(self): 
        # TODO: Somehow it cant display card data only when the lane is empty............
        print(f"""   
                X===================================X   X===================================X   X===================================X   X===================================X                        Combat Log
                |{self.lane5.active_card.name:^35}|   |{self.lane6.active_card.name:^35}|   |{self.lane7.active_card.name:^35}|   |{self.lane8.active_card.name:^35}|                        {self.combat_data[0][0]}
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