class Lane:
    def __init__(self, lane_number: int):
        self.lane_number = lane_number 
        self.active_card = None # ??

    def add_card(self, new_card):
        self.active_card = new_card
    
    def remove_card(self):
        self.active_card = None

    def __str__(self):
        return f"{self.lane_number}"