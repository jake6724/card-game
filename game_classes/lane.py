from game_classes.card import Card

class Lane:
    def __init__(self, lane_number: int, starting_card: Card):
        self.lane_number = lane_number 
        self.active_card = starting_card

    def set_active_card(self, new_card):
        self.active_card = new_card
    
    def remove_active_card(self):
        self.active_card = None

    def __str__(self):
        return f"{self.lane_number}"