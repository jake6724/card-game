from game_classes.lane import Lane
from game_classes.card import Card
from game_classes.player import Player
import time 
import copy 

class GameBoard:
    def __init__(self): 
        self.empty_lane_card = Card("empty",0,0,0,0,"n",0,0,"n","n",0,0,"n")
        self.empty_lane_card.create_description() 
        # Maybe dont need deep copies here ..............
        self.lane_list = [Lane(1, copy.deepcopy(self.empty_lane_card)), Lane(2, copy.deepcopy(self.empty_lane_card)), Lane(3, copy.deepcopy(self.empty_lane_card)), 
                        Lane(4, copy.deepcopy(self.empty_lane_card)), Lane(5, copy.deepcopy(self.empty_lane_card)), Lane(6, copy.deepcopy(self.empty_lane_card)),
                        Lane(7, copy.deepcopy(self.empty_lane_card)), Lane(8, copy.deepcopy(self.empty_lane_card))] 
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
        self.cards_to_remove = []
        self.combat_data = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""],
                            ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]
        
        self.create_combat_log()

    def add_to_active_cards(self, card_to_add):
        self.active_card_list.append(card_to_add)

    def get_card_priority(self, card):
        return card.priority

    def sort_active_cards(self):
        self.active_card_list.sort(key= self.get_card_priority, reverse= True)

    def reset_card_turns(self):
        for card in self.active_card_list:
            card.taken_turn = False 

    def run_card_combat_actions(self, card: Card, p1: Player, p2: Player):
        # Check if card name is empty and if so don't waste time doing the rest  
        if card.name == "empty":
            return 

        target_results = self.get_combat_targets(card, p1, p2)
        card_target = target_results[0]
        card_all_targets = target_results[1]
        player_target = target_results[2]
        repeat_swap_target_lane = target_results[3]
        finale_swap_target_lane = target_results[4]

        # # Run card combat 
        # if card.counter == card.end_turn:
        #     self.run_finale_combat(card, finale_swap_target_lane, card_target, card_all_targets, player_target, p1, p2)

        # elif card.counter >= card.start_turn: 
        #     self.run_repeat_combat(card, repeat_swap_target_lane, card_target, card_all_targets, player_target, p1, p2)

          # Run card combat 
        if card.counter == card.end_turn:
            self.run_combat("f", card, finale_swap_target_lane, card_target, card_all_targets, player_target, p1, p2)

        elif card.counter >= card.start_turn: 
            self.run_combat("r", card, repeat_swap_target_lane, card_target, card_all_targets, player_target, p1, p2)

    def get_combat_targets(self, card, p1, p2):
        # Order of operations for attacking: 1. Swap, 2. Card Damage, 3. Player Damage 
        card_target = ""
        card_all_targets = ""
        player_target = None
        repeat_swap_target_lane = None
        finale_swap_target_lane = None
        index = int(card.lane_num) - 1

        # Get targets based on card data 
        if card.player == p1:
            card_target = self.get_lane_by_number(int(card.lane_num) + 4).active_card
            card_all_targets = [self.lane1.active_card, self.lane2.active_card, self.lane3.active_card, self.lane4.active_card]
            player_target = p2

            if card.repeat_swap_direction == "l":
                if int(card.lane_num) != 1:
                    repeat_swap_target_lane = self.lane_list[(index - 1)]
            
            elif card.repeat_swap_direction == "r":
                if int(card.lane_num) != 4:
                    repeat_swap_target_lane = self.lane_list[(index + 1)]

            if card.finale_swap_direction == "l":
                if int(card.lane_num) != 1:
                    finale_swap_target_lane = self.lane_list[(index - 1)]
            
            elif card.finale_swap_direction == "r":
                if int(card.lane_num) != 4:
                    finale_swap_target_lane = self.lane_list[(index + 1)]


        elif card.player == p2:
            card_target = self.get_lane_by_number(int(card.lane_num) - 4).active_card
            card_all_targets = [self.lane1.active_card, self.lane2.active_card, self.lane3.active_card, self.lane4.active_card]
            player_target = p1

            if card.repeat_swap_direction == "l":
                if int(card.lane_num) != 5:
                    repeat_swap_target_lane = self.lane_list[(index - 1)]
            
            elif card.repeat_swap_direction == "r":
                if int(card.lane_num) != 8:
                    repeat_swap_target_lane = self.lane_list[(index + 1)]

            if card.finale_swap_direction == "l":
                if int(card.lane_num) != 5:
                    finale_swap_target_lane = self.lane_list[(index - 1)]
            
            elif card.finale_swap_direction == "r":
                if int(card.lane_num) != 8:
                    finale_swap_target_lane = self.lane_list[(index + 1)]

        return [card_target, card_all_targets, player_target, repeat_swap_target_lane, finale_swap_target_lane]

    def run_combat(self, finale_or_repeat: str, card:Card, swap_target_lane, card_target: Card, card_all_targets: list[Card], player_target: Player, p1: Player, p2: Player):
        # Set up vars for either repeat or finale damage 
        if finale_or_repeat == "f":
            card_dmg_target = getattr(card, "finale_card_target")
            card_dmg = getattr(card, "finale_card_damage")
            player_dmg = getattr(card, "finale_player_damage")
            m = "finale"

        elif finale_or_repeat == "r":
            card_dmg_target = getattr(card, "repeat_card_target")
            card_dmg = getattr(card, "repeat_card_damage")
            player_dmg = getattr(card, "repeat_player_damage")
            m = str()

        # Swapping 
        if swap_target_lane != None:
            self.swap_cards(card, swap_target_lane)
            card.log_swap = f"{card} swapped with card in lane {swap_target_lane}"

            # Re-determine card targets based on new board location 
            target_results = self.get_combat_targets(card, p1, p2)
            card_target = target_results[0]
            card_all_targets = target_results[1]
            player_target = target_results[2]

        # Combat
        if card_dmg_target == "c":
            if card_target.name != "empty": # Don't do opponent card attack if the card is empty 
                card_target.take_damage(card_dmg, card)

                # Check if this damage killed the card, if so add to combat log 
                if card_target.is_dead:
                    card.killed_cards_list.append(card_target)
                    card.log_killed_cards = f"{card} killed {card.killed_cards_list}"

                card.log_card = f"{card} dealt {card_dmg} {m} dmg to {card_target.name}"

        elif card_dmg_target == "a":
            for target in card_all_targets:
                if target.name != "empty": # Don't do opponent card attack if the card is empty 
                    target.take_damage(card_dmg, card)
                    # Check if this damage killed the card, if so add to combat log 
                    if target.is_dead:
                        card.killed_cards_list.append(target)
                        card.log_killed_cards = f"{card} killed {card.killed_cards_list}"

            card.log_card = f"{card} dealt {card_dmg} {m} dmg to all enemy cards"
            
        if player_dmg > 0:
            player_target.take_damage(player_dmg, card) 
            card.log_player = f"{card} dealt {player_dmg} {m} dmg to {player_target.name}"

    def swap_cards(self, card, swap_target_lane): # TODO Needs cleanup 
        # Save the target lanes card in a temp_card value
        # Place the current card into the target lane
        # Place the temp_card value into the original lane 

        temp_card = swap_target_lane.active_card
        swap_target_lane.set_active_card(card)
        original_lane = self.get_lane_by_number(card.lane_num)
        original_lane.set_active_card(temp_card)

        # Update both cards internal lane num
        card.lane_num = swap_target_lane.number
        temp_card.lane_num = original_lane.number

    def reset_combat_log(self):
        self.combat_data = [["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""],
                            ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""], ["", "", "", "", ""]]

    def reset_card_combat_logs(self):
        for card in self.active_card_list:
            card.log_swap = ""
            card.log_card = ""
            card.log_player = ""
            card.log_killed_cards = ""
            card.killed_cards_list = []

    def create_combat_log(self):
        # Add data from all active cards 
        for i, card in enumerate(self.active_card_list):
            # Check if the list is more than 1. Do different formatting depending on answer
            if len(card.killed_cards_list) == 0:
                card.log_killed_cards = ""

            elif len(card.killed_cards_list) == 1:
                card.log_killed_cards = f"{card} killed {card.killed_cards_list[0]}"
            
            self.combat_data[i] = [card.log_swap, card.log_card, card.log_player, card.log_killed_cards, card.log_left_board]

        # Fill in blank data until combat data list is filled
        while len(self.combat_data) != 8:
            self.combat_data.append(["", "", "", "", ""])

    def update(self):
        # Check if the card will leave the board, so combat log can be updated
        # This needs to be done before log is created and card is actually remvoed 
        for i, card in enumerate(self.active_card_list):
            if card.counter > card.end_turn:
                card.log_left_board = f"{card} left the board"

        self.create_combat_log()

        for i, card in enumerate(self.active_card_list[:]): # MUST USE COPY OF LIST WHEN REMOVING ITEMS OR WILL SKIP ITEMS (what the [:] helps with)
            card.create_description()
            if card.health <= 0:
                self.remove_active_card(card)
            
            elif card.counter > card.end_turn: # Possible problem area 
                self.remove_active_card(card)

    def remove_active_card(self, card):
        # Reset card's lane to empty
        lane = self.get_lane_by_number(card.lane_num)
        self.reset_lane(lane)

        # Delete card from memory 
        self.active_card_list.remove(card)

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
        #     case 5: return self.lane1
        #     case 6: return self.lane2
        #     case 7: return self.lane3
        #     case 8: return self.lane4
    
    def print_active_card_list(self):
        print("Gameboard Active Card List:")
        for card in self.active_card_list:
            print(card)
        time.sleep(2)

    def display_gameboard_p1(self): 
        print(f"""                                                                                                                                                                                      Combat Log
                X===================================X   X===================================X   X===================================X   X===================================X {self.combat_data[0][0]}
                |{self.lane5.active_card.name:^35}|   |{self.lane6.active_card.name:^35}|   |{self.lane7.active_card.name:^35}|   |{self.lane8.active_card.name:^35}| {self.combat_data[0][1]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[0][2]}
                |{self.lane5.active_card.desc_mana:^35}|   |{self.lane6.active_card.desc_mana:^35}|   |{self.lane7.active_card.desc_mana:^35}|   |{self.lane8.active_card.desc_mana:^35}| {self.combat_data[0][3]}
                |{self.lane5.active_card.desc_health:^35}|   |{self.lane6.active_card.desc_health:^35}|   |{self.lane7.active_card.desc_health:^35}|   |{self.lane8.active_card.desc_health:^35}| {self.combat_data[0][4]}
                |{self.lane5.active_card.desc_counter:^35}|   |{self.lane6.active_card.desc_counter:^35}|   |{self.lane7.active_card.desc_counter:^35}|   |{self.lane8.active_card.desc_counter:^35}| {self.combat_data[1][0]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[1][1]}
                |{self.lane5.active_card.desc_each:^35}|   |{self.lane6.active_card.desc_each:^35}|   |{self.lane7.active_card.desc_each:^35}|   |{self.lane8.active_card.desc_each:^35}| {self.combat_data[1][2]}
                |{self.lane5.active_card.desc_repeat_card_damage:^35}|   |{self.lane6.active_card.desc_repeat_card_damage:^35}|   |{self.lane7.active_card.desc_repeat_card_damage:^35}|   |{self.lane8.active_card.desc_repeat_card_damage:^35}| {self.combat_data[1][3]}
                |{self.lane5.active_card.desc_repeat_player_damage:^35}|   |{self.lane6.active_card.desc_repeat_player_damage:^35}|   |{self.lane7.active_card.desc_repeat_player_damage:^35}|   |{self.lane8.active_card.desc_repeat_player_damage:^35}| {self.combat_data[1][4]}
                |{self.lane5.active_card.desc_repeat_swap:^35}|   |{self.lane6.active_card.desc_repeat_swap:^35}|   |{self.lane7.active_card.desc_repeat_swap:^35}|   |{self.lane8.active_card.desc_repeat_swap:^35}| {self.combat_data[2][0]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[2][1]}
                |{self.lane5.active_card.desc_finale:^35}|   |{self.lane6.active_card.desc_finale:^35}|   |{self.lane7.active_card.desc_finale:^35}|   |{self.lane8.active_card.desc_finale:^35}| {self.combat_data[2][2]}
                |{self.lane5.active_card.desc_finale_card_damage:^35}|   |{self.lane6.active_card.desc_finale_card_damage:^35}|   |{self.lane7.active_card.desc_finale_card_damage:^35}|   |{self.lane8.active_card.desc_finale_card_damage:^35}| {self.combat_data[2][3]}
                |{self.lane5.active_card.desc_finale_player_damage:^35}|   |{self.lane6.active_card.desc_finale_player_damage:^35}|   |{self.lane7.active_card.desc_finale_player_damage:^35}|   |{self.lane8.active_card.desc_finale_player_damage:^35}| {self.combat_data[2][4]}
                |{self.lane5.active_card.desc_finale_swap:^35}|   |{self.lane6.active_card.desc_finale_swap:^35}|   |{self.lane7.active_card.desc_finale_swap:^35}|   |{self.lane8.active_card.desc_finale_swap:^35}| {self.combat_data[3][0]}
                X===================================X   X===================================X   X===================================X   X===================================X {self.combat_data[3][1]}
                                Lane 5                                  Lane 6                                  Lane 7                                Lane 8                  {self.combat_data[3][2]}
                ============================================================================================================================================================= {self.combat_data[3][3]}
                                Lane 1                                  Lane 2                                  Lane 3                                Lane 4                  {self.combat_data[3][4]}
                X===================================X   X===================================X   X===================================X   X===================================X {self.combat_data[4][0]}
                |{self.lane1.active_card.name:^35}|   |{self.lane2.active_card.name:^35}|   |{self.lane3.active_card.name:^35}|   |{self.lane4.active_card.name:^35}| {self.combat_data[4][1]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[4][2]}
                |{self.lane1.active_card.desc_mana:^35}|   |{self.lane2.active_card.desc_mana:^35}|   |{self.lane3.active_card.desc_mana:^35}|   |{self.lane4.active_card.desc_mana:^35}| {self.combat_data[4][3]}
                |{self.lane1.active_card.desc_health:^35}|   |{self.lane2.active_card.desc_health:^35}|   |{self.lane3.active_card.desc_health:^35}|   |{self.lane4.active_card.desc_health:^35}| {self.combat_data[4][4]}
                |{self.lane1.active_card.desc_counter:^35}|   |{self.lane2.active_card.desc_counter:^35}|   |{self.lane3.active_card.desc_counter:^35}|   |{self.lane4.active_card.desc_counter:^35}| {self.combat_data[5][0]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[5][1]}
                |{self.lane1.active_card.desc_each:^35}|   |{self.lane2.active_card.desc_each:^35}|   |{self.lane3.active_card.desc_each:^35}|   |{self.lane4.active_card.desc_each:^35}| {self.combat_data[5][2]}
                |{self.lane1.active_card.desc_repeat_card_damage:^35}|   |{self.lane2.active_card.desc_repeat_card_damage:^35}|   |{self.lane3.active_card.desc_repeat_card_damage:^35}|   |{self.lane4.active_card.desc_repeat_card_damage:^35}| {self.combat_data[5][3]}
                |{self.lane1.active_card.desc_repeat_player_damage:^35}|   |{self.lane2.active_card.desc_repeat_player_damage:^35}|   |{self.lane3.active_card.desc_repeat_player_damage:^35}|   |{self.lane4.active_card.desc_repeat_player_damage:^35}| {self.combat_data[5][4]}
                |{self.lane1.active_card.desc_repeat_swap:^35}|   |{self.lane2.active_card.desc_repeat_swap:^35}|   |{self.lane3.active_card.desc_repeat_swap:^35}|   |{self.lane4.active_card.desc_repeat_swap:^35}| {self.combat_data[6][0]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[6][1]}
                |{self.lane1.active_card.desc_finale:^35}|   |{self.lane2.active_card.desc_finale:^35}|   |{self.lane3.active_card.desc_finale:^35}|   |{self.lane4.active_card.desc_finale:^35}| {self.combat_data[6][2]}
                |{self.lane1.active_card.desc_finale_card_damage:^35}|   |{self.lane2.active_card.desc_finale_card_damage:^35}|   |{self.lane3.active_card.desc_finale_card_damage:^35}|   |{self.lane4.active_card.desc_finale_card_damage:^35}| {self.combat_data[6][3]}
                |{self.lane1.active_card.desc_finale_player_damage:^35}|   |{self.lane2.active_card.desc_finale_player_damage:^35}|   |{self.lane3.active_card.desc_finale_player_damage:^35}|   |{self.lane4.active_card.desc_finale_player_damage:^35}| {self.combat_data[6][4]}
                |{self.lane1.active_card.desc_finale_swap:^35}|   |{self.lane2.active_card.desc_finale_swap:^35}|   |{self.lane3.active_card.desc_finale_swap:^35}|   |{self.lane4.active_card.desc_finale_swap:^35}| {self.combat_data[7][0]}
                X===================================X   X===================================X   X===================================X   X===================================X {self.combat_data[7][1]}
                                                                                                                                                                              {self.combat_data[7][2]}""", end='')           
        
    def display_gameboard_p2(self): 
            print(f"""                                                                                                                                                                                      Combat Log
                X===================================X   X===================================X   X===================================X   X===================================X {self.combat_data[0][0]}
                |{self.lane1.active_card.name:^35}|   |{self.lane2.active_card.name:^35}|   |{self.lane3.active_card.name:^35}|   |{self.lane4.active_card.name:^35}| {self.combat_data[0][1]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[0][2]}
                |{self.lane1.active_card.desc_mana:^35}|   |{self.lane2.active_card.desc_mana:^35}|   |{self.lane3.active_card.desc_mana:^35}|   |{self.lane4.active_card.desc_mana:^35}| {self.combat_data[0][3]}
                |{self.lane1.active_card.desc_health:^35}|   |{self.lane2.active_card.desc_health:^35}|   |{self.lane3.active_card.desc_health:^35}|   |{self.lane4.active_card.desc_health:^35}| {self.combat_data[0][4]}
                |{self.lane1.active_card.desc_counter:^35}|   |{self.lane2.active_card.desc_counter:^35}|   |{self.lane3.active_card.desc_counter:^35}|   |{self.lane4.active_card.desc_counter:^35}| {self.combat_data[1][0]}
                |                                   |   |                                   |   |                                   |   |                                   |            {self.combat_data[1][1]}
                |{self.lane1.active_card.desc_each:^35}|   |{self.lane2.active_card.desc_each:^35}|   |{self.lane3.active_card.desc_each:^35}|   |{self.lane4.active_card.desc_each:^35}| {self.combat_data[1][2]}
                |{self.lane1.active_card.desc_repeat_card_damage:^35}|   |{self.lane2.active_card.desc_repeat_card_damage:^35}|   |{self.lane3.active_card.desc_repeat_card_damage:^35}|   |{self.lane4.active_card.desc_repeat_card_damage:^35}| {self.combat_data[1][3]}
                |{self.lane1.active_card.desc_repeat_player_damage:^35}|   |{self.lane2.active_card.desc_repeat_player_damage:^35}|   |{self.lane3.active_card.desc_repeat_player_damage:^35}|   |{self.lane4.active_card.desc_repeat_player_damage:^35}| {self.combat_data[1][4]}
                |{self.lane1.active_card.desc_repeat_swap:^35}|   |{self.lane2.active_card.desc_repeat_swap:^35}|   |{self.lane3.active_card.desc_repeat_swap:^35}|   |{self.lane4.active_card.desc_repeat_swap:^35}| {self.combat_data[2][0]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[2][1]}
                |{self.lane1.active_card.desc_finale:^35}|   |{self.lane2.active_card.desc_finale:^35}|   |{self.lane3.active_card.desc_finale:^35}|   |{self.lane4.active_card.desc_finale:^35}| {self.combat_data[2][2]}
                |{self.lane1.active_card.desc_finale_card_damage:^35}|   |{self.lane2.active_card.desc_finale_card_damage:^35}|   |{self.lane3.active_card.desc_finale_card_damage:^35}|   |{self.lane4.active_card.desc_finale_card_damage:^35}| {self.combat_data[2][3]}
                |{self.lane1.active_card.desc_finale_player_damage:^35}|   |{self.lane2.active_card.desc_finale_player_damage:^35}|   |{self.lane3.active_card.desc_finale_player_damage:^35}|   |{self.lane4.active_card.desc_finale_player_damage:^35}| {self.combat_data[2][4]}
                |{self.lane1.active_card.desc_finale_swap:^35}|   |{self.lane2.active_card.desc_finale_swap:^35}|   |{self.lane3.active_card.desc_finale_swap:^35}|   |{self.lane4.active_card.desc_finale_swap:^35}| {self.combat_data[3][0]}
                X===================================X   X===================================X   X===================================X   X===================================X {self.combat_data[3][1]}
                                Lane 1                                  Lane 2                                  Lane 3                                Lane 4                  {self.combat_data[3][2]}
                ============================================================================================================================================================= {self.combat_data[3][3]}
                                Lane 5                                  Lane 6                                  Lane 7                                Lane 8                  {self.combat_data[3][4]}
                X===================================X   X===================================X   X===================================X   X===================================X {self.combat_data[4][0]}
                |{self.lane5.active_card.name:^35}|   |{self.lane6.active_card.name:^35}|   |{self.lane7.active_card.name:^35}|   |{self.lane8.active_card.name:^35}| {self.combat_data[4][1]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[4][2]}
                |{self.lane5.active_card.desc_mana:^35}|   |{self.lane6.active_card.desc_mana:^35}|   |{self.lane7.active_card.desc_mana:^35}|   |{self.lane8.active_card.desc_mana:^35}| {self.combat_data[4][3]}
                |{self.lane5.active_card.desc_health:^35}|   |{self.lane6.active_card.desc_health:^35}|   |{self.lane7.active_card.desc_health:^35}|   |{self.lane8.active_card.desc_health:^35}| {self.combat_data[4][4]}
                |{self.lane5.active_card.desc_counter:^35}|   |{self.lane6.active_card.desc_counter:^35}|   |{self.lane7.active_card.desc_counter:^35}|   |{self.lane8.active_card.desc_counter:^35}| {self.combat_data[5][0]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[5][1]}
                |{self.lane5.active_card.desc_each:^35}|   |{self.lane6.active_card.desc_each:^35}|   |{self.lane7.active_card.desc_each:^35}|   |{self.lane8.active_card.desc_each:^35}| {self.combat_data[5][2]}
                |{self.lane5.active_card.desc_repeat_card_damage:^35}|   |{self.lane6.active_card.desc_repeat_card_damage:^35}|   |{self.lane7.active_card.desc_repeat_card_damage:^35}|   |{self.lane8.active_card.desc_repeat_card_damage:^35}| {self.combat_data[5][3]}
                |{self.lane5.active_card.desc_repeat_player_damage:^35}|   |{self.lane6.active_card.desc_repeat_player_damage:^35}|   |{self.lane7.active_card.desc_repeat_player_damage:^35}|   |{self.lane8.active_card.desc_repeat_player_damage:^35}| {self.combat_data[5][4]}
                |{self.lane5.active_card.desc_repeat_swap:^35}|   |{self.lane6.active_card.desc_repeat_swap:^35}|   |{self.lane7.active_card.desc_repeat_swap:^35}|   |{self.lane8.active_card.desc_repeat_swap:^35}| {self.combat_data[6][0]}
                |                                   |   |                                   |   |                                   |   |                                   | {self.combat_data[6][1]}
                |{self.lane5.active_card.desc_finale:^35}|   |{self.lane6.active_card.desc_finale:^35}|   |{self.lane7.active_card.desc_finale:^35}|   |{self.lane8.active_card.desc_finale:^35}| {self.combat_data[6][2]}
                |{self.lane5.active_card.desc_finale_card_damage:^35}|   |{self.lane6.active_card.desc_finale_card_damage:^35}|   |{self.lane7.active_card.desc_finale_card_damage:^35}|   |{self.lane8.active_card.desc_finale_card_damage:^35}| {self.combat_data[6][3]}
                |{self.lane5.active_card.desc_finale_player_damage:^35}|   |{self.lane6.active_card.desc_finale_player_damage:^35}|   |{self.lane7.active_card.desc_finale_player_damage:^35}|   |{self.lane8.active_card.desc_finale_player_damage:^35}| {self.combat_data[6][4]}
                |{self.lane5.active_card.desc_finale_swap:^35}|   |{self.lane6.active_card.desc_finale_swap:^35}|   |{self.lane7.active_card.desc_finale_swap:^35}|   |{self.lane8.active_card.desc_finale_swap:^35}| {self.combat_data[7][0]}
                X===================================X   X===================================X   X===================================X   X===================================X {self.combat_data[7][1]}
                                                                                                                                                                              {self.combat_data[7][2]}""", end='')