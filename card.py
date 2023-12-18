class Card: 
    def __init__(self, name: str, mana: int, health: int, start_turn: int, end_turn, card_target: int, card_damage: int, player_damage: int, finale_card_target: str, finale_card_damage: int, finale_player_damage: int, swap_direction: str, swap_duration: int): 
        self.name = name 
        self.mana = mana 
        self.health = health
        self.start_turn = start_turn
        self.end_turn = end_turn
        self.card_target = card_target
        self.card_damage = card_damage
        self.player_damage = player_damage
        self.finale_card_target = finale_card_target
        self.finale_card_damage = finale_card_damage
        self.finale_player_damage = finale_player_damage
        self.swap_direction = swap_direction
        self.swap_duration = swap_duration

    def create_description(self):
        self.desc = ""

        # Add each turn flag if needed
        if self.start_turn < self.end_turn:
            self.desc + "Each turn: \n"

        # Card damage info
        if int(self.card_damage) > 0:
            if self.card_target == "c":
                self.desc + f"Deal {self.card_damage} to opposing card"
            if self.card_target == "a": 
                self.desc + f"Deal {self.card_damage} to all opposing cards"

        # Player damage info 
        if int(self.player_damage):
            if int(self.player_damage) > 0:
                self.desc + f"Deal {self.card_damage} to enemy player"


        def __str__(self):
            return f"{self.name} - PC:{self.placement_cost} / H:{self.health} / TTA:{self.turns_to_activate}" 
        
        

