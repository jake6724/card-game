from game_classes.lane import Lane
from game_classes.card import Card
from game_classes.combatgroup import CombatGroup

class GameBoard:
    def __init__(self): 
        self.empty_lane_card = Card("empty",0,0,0,0,"c",0,0,"c",0,0,"l",0)
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

        # Combat set up 
        self.combat_group_list = []

    def create_new_combat_group(self):
        # This should be called at the start of each placement phase round 
        new_combat_group = CombatGroup()
        self.combat_group_list.append(new_combat_group)

    def add_card_to_combat_group(self, round_number, card1, card2):
        # This should be called during card placement 
        cg = self.get_combat_group_by_round_num(round_number)
        cg.add_card_pair(card1, card2)

    def add_card_to_lane(self, new_card: Card, lane_number: int):
        for lane in self.lane_list:
            if lane.number == lane_number:
                lane.set_active_card(new_card)

    def get_combat_group_by_round_num(self, round_number):
        # Make round number accurate for indexing self.combat_group_list 
        round_number =- 1 
        return self.combat_group_list[round_number]

    def display_gameboard(self): 
        # TODO: Somehow it cant display card data only when the lane is empty............
        print(f"""   
                Gameboard:
                X===================================X   X===================================X   X===================================X   X===================================X
                |{self.lane2.active_card.name:^35}|   |{self.lane4.active_card.name:^35}|   |{self.lane6.active_card.name:^35}|   |{self.lane8.active_card.name:^35}|
                |                                   |   |                                   |   |                                   |   |                                   |    
                |{self.lane2.active_card.desc_mana:^35}|   |{self.lane4.active_card.desc_mana:<35}|   |{self.lane6.active_card.desc_mana:<35}|   |{self.lane8.active_card.desc_mana:<35}|
                |{self.lane2.active_card.desc_health:^35}|   |{self.lane4.active_card.desc_health:<35}|   |{self.lane6.active_card.desc_health:<35}|   |{self.lane8.active_card.desc_health:<35}|
                |                                   |   |                                   |   |                                   |   |                                   |         
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |{self.lane2.active_card.desc_each:^35}|   |{self.lane4.active_card.desc_each:^35}|   |{self.lane6.active_card.desc_each:^35}|   |{self.lane8.active_card.desc_each:^35}|
                |{self.lane2.active_card.desc_card_damage:^35}|   |{self.lane4.active_card.desc_card_damage:^35}|   |{self.lane6.active_card.desc_card_damage:^35}|   |{self.lane8.active_card.desc_card_damage:^35}|
                |{self.lane2.active_card.desc_player_damage:^35}|   |{self.lane4.active_card.desc_player_damage:^35}|   |{self.lane6.active_card.desc_player_damage:^35}|   |{self.lane8.active_card.desc_player_damage:^35}|
                |{self.lane2.active_card.desc_finale_card_damage:^35}|   |{self.lane4.active_card.desc_player_damage:^35}|   |{self.lane6.active_card.desc_player_damage:^35}|   |{self.lane8.active_card.desc_player_damage:^35}|
                |                                   |   |                                   |   |                                   |   |                                   |
                |{self.lane2.active_card.desc_swap:^35}|   |{self.lane4.active_card.desc_swap:^35}|   |{self.lane6.active_card.desc_swap:^35}|   |{self.lane8.active_card.desc_swap:^35}|
                |{self.lane2.active_card.desc_swap_duration:^35}|   |{self.lane4.active_card.desc_swap_duration:^35}|   |{self.lane6.active_card.desc_swap_duration:^35}|   |{self.lane8.active_card.desc_swap_duration:^35}|
                X===================================X   X===================================X   X===================================X   X===================================X
                                Lane 2                                  Lane 4                                  Lane 6                                Lane 8               
                =============================================================================================================================================================
                                Lane 1                                  Lane 3                                  Lane 5                                Lane 7               
                X===================================X   X===================================X   X===================================X   X===================================X
                |{self.lane1.active_card.name:^35}|   |{self.lane3.active_card.name:^35}|   |{self.lane5.active_card.name:^35}|   |{self.lane7.active_card.name:^35}|
                |                                   |   |                                   |   |                                   |   |                                   |    
                |{self.lane1.active_card.desc_mana:^35}|   |{self.lane3.active_card.desc_mana:<35}|   |{self.lane5.active_card.desc_mana:<35}|   |{self.lane7.active_card.desc_mana:<35}|
                |{self.lane1.active_card.desc_health:^35}|   |{self.lane3.active_card.desc_health:<35}|   |{self.lane5.active_card.desc_health:<35}|   |{self.lane7.active_card.desc_health:<35}|
                |                                   |   |                                   |   |                                   |   |                                   |         
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |{self.lane1.active_card.desc_each:^35}|   |{self.lane3.active_card.desc_each:^35}|   |{self.lane5.active_card.desc_each:^35}|   |{self.lane7.active_card.desc_each:^35}|
                |{self.lane1.active_card.desc_card_damage:^35}|   |{self.lane3.active_card.desc_card_damage:^35}|   |{self.lane5.active_card.desc_card_damage:^35}|   |{self.lane7.active_card.desc_card_damage:^35}|
                |{self.lane1.active_card.desc_player_damage:^35}|   |{self.lane3.active_card.desc_player_damage:^35}|   |{self.lane5.active_card.desc_player_damage:^35}|   |{self.lane7.active_card.desc_player_damage:^35}|
                |{self.lane1.active_card.desc_finale_card_damage:^35}|   |{self.lane3.active_card.desc_player_damage:^35}|   |{self.lane5.active_card.desc_player_damage:^35}|   |{self.lane7.active_card.desc_player_damage:^35}|
                |                                   |   |                                   |   |                                   |   |                                   |
                |{self.lane1.active_card.desc_swap:^35}|   |{self.lane3.active_card.desc_swap:^35}|   |{self.lane5.active_card.desc_swap:^35}|   |{self.lane7.active_card.desc_swap:^35}|
                |{self.lane1.active_card.desc_swap_duration:^35}|   |{self.lane3.active_card.desc_swap_duration:^35}|   |{self.lane5.active_card.desc_swap_duration:^35}|   |{self.lane7.active_card.desc_swap_duration:^35}|
                X===================================X   X===================================X   X===================================X   X===================================X
        """)