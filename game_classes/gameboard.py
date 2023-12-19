from game_classes.lane import Lane
from game_classes.card import Card 
import textwrap


class GameBoard:
    def __init__(self, empty_lane_card): 
        self.empty_lane_card = empty_lane_card
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

    def add_card_to_lane(self, new_card: Card, lane_number: int):
        for lane in self.lane_list:
            if lane.number == lane_number:
                lane.set_active_card(new_card)

    def display_gameboard(self): 
        print(f"""   
                Gameboard:
                X===================================X   X===================================X   X===================================X   X===================================X
                |{self.lane2.active_card.name:^35}|   |{self.lane4.active_card.name:^35}|   |{self.lane6.active_card.name:^35}|   |{self.lane8.active_card.name:^35}|
                |                                   |   |                                   |   |                                   |   |                                   |    
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |         
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |         
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |         
                |                                   |   |                                   |   |                                   |   |                                   |         
                X===================================X   X===================================X   X===================================X   X===================================X
                                Lane 2                                  Lane 4                                  Lane 6                                Lane 8               
                =============================================================================================================================================================
                                Lane 1                                  Lane 3                                  Lane 5                                Lane 7               
                X===================================X   X===================================X   X===================================X   X===================================X
                |{self.lane1.active_card.name:^35}|   |{self.lane3.active_card.name:^35}|   |{self.lane5.active_card.name:^35}|   |{self.lane7.active_card.name:^35}|
                |                                   |   |                                   |   |                                   |   |                                   |    
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |         
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |         
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |
                |                                   |   |                                   |   |                                   |   |                                   |         
                |                                   |   |                                   |   |                                   |   |                                   |         
                X===================================X   X===================================X   X===================================X   X===================================X
        """)

    # def display_gameboard(self): 
    #     print(textwrap.dedent(f"""   
    #     Gameboard:
    #     X===================================X   X===================================X   X===================================X   X===================================X
    #     |{self.lane2.active_card.name:^35}|   |{self.lane4.active_card.name:^35}|   |{self.lane6.active_card.name:^35}|   |{self.lane8.active_card.name:^35}|
    #     |                                   |   |                                   |   |                                   |   |                                   |    
    #     |MP:{c1m:<32}|   |MP:{c2m:<32}|   |MP:{c3m:<32}|   |MP:{c4m:<32}|
    #     |HP:{c1hp:<32}|   |HP:{c2hp:<32}|   |HP:{c3hp:<32}|   |HP:{c4hp:<32}|         
    #     |                                   |   |                                   |   |                                   |   |                                   |         
    #     |{c1de:^35}|   |{c2de:^35}|   |{c3de:^35}|   |{c4de:^35}|         
    #     |{c1dc:^35}|   |{c2dc:^35}|   |{c3dc:^35}|   |{c4dc:^35}|         
    #     |{c1dp:^35}|   |{c2dp:^35}|   |{c3dp:^35}|   |{c4dp:^35}|         
    #     |{c1dfc:^35}|   |{c2dfc:^35}|   |{c3dfc:^35}|   |{c4dfc:^35}|         
    #     |                                   |   |                                   |   |                                   |   |                                   |         
    #     |{c1ds:^35}|   |{c2ds:^35}|   |{c3ds:^35}|   |{c4ds:^35}|         
    #     |{c1dsd:^35}|   |{c2dsd:^35}|   |{c3dsd:^35}|   |{c4dsd:^35}|         
    #     |                                   |   |                                   |   |                                   |   |                                   |         
    #     |                                   |   |                                   |   |                                   |   |                                   |         
    #     X===================================X   X===================================X   X===================================X   X===================================X
    #                     Lane 2                                  Lane 4                                  Lane 6                                Lane 8               
    #     =============================================================================================================================================================
    #                     Lane 1                                  Lane 3                                  Lane 5                                Lane 7               
    #     X===================================X   X===================================X   X===================================X   X===================================X
    #     |{self.lane1.active_card.name:^35}|   |{self.lane3.active_card.name:^35}|   |{self.lane5.active_card.name:^35}|   |{self.lane7.active_card.name:^35}|
    #     |                                   |   |                                   |   |                                   |   |                                   |    
    #     |MP:{c1m:<32}|   |MP:{c2m:<32}|   |MP:{c3m:<32}|   |MP:{c4m:<32}|
    #     |HP:{c1hp:<32}|   |HP:{c2hp:<32}|   |HP:{c3hp:<32}|   |HP:{c4hp:<32}|         
    #     |                                   |   |                                   |   |                                   |   |                                   |         
    #     |{c1de:^35}|   |{c2de:^35}|   |{c3de:^35}|   |{c4de:^35}|         
    #     |{c1dc:^35}|   |{c2dc:^35}|   |{c3dc:^35}|   |{c4dc:^35}|         
    #     |{c1dp:^35}|   |{c2dp:^35}|   |{c3dp:^35}|   |{c4dp:^35}|         
    #     |{c1dfc:^35}|   |{c2dfc:^35}|   |{c3dfc:^35}|   |{c4dfc:^35}|         
    #     |                                   |   |                                   |   |                                   |   |                                   |         
    #     |{c1ds:^35}|   |{c2ds:^35}|   |{c3ds:^35}|   |{c4ds:^35}|         
    #     |{c1dsd:^35}|   |{c2dsd:^35}|   |{c3dsd:^35}|   |{c4dsd:^35}|         
    #     |                                   |   |                                   |   |                                   |   |                                   |         
    #     |                                   |   |                                   |   |                                   |   |                                   |         
    #     X===================================X   X===================================X   X===================================X   X===================================X
    #     """))