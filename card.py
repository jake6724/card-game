class Card: 
    def __init__(self, name: str, mana: int, health: int, start_turn: int, end_turn, card_target: int, card_damage: int, player_damage: int, finale_card_target: str, finale_card_damage: int, finale_player_damage: int, swap_direction: str, swap_duration: int): 
        self.name = name 
        self.mana = mana 
        self.health = health
        self.start_turn = start_turn
        self.end_turn = end_turn
        self.card_target = card_target
        self.card_damage = int(card_damage)
        self.player_damage = int(player_damage)
        self.finale_card_target = finale_card_target
        self.finale_card_damage = int(finale_card_damage)
        self.finale_player_damage = int(finale_player_damage)
        self.swap_direction = swap_direction
        self.swap_duration = int(swap_duration)

    # def print_desc(self):
    #     print(f"Card Description:{self.desc}")

    def create_description(self):
        # Set up desc text vars 
        self.desc_each = ""
        self.desc_card_damage = ""
        self.desc_player_damage = "" 
        self.desc_swap = ""
        self.desc_finale_card_damage = ""
        self.desc_finale_card_target = ""
        self.desc_finale_player_damage = "" 
        self.desc_swap = ""
        self.desc_swap_duration = ""

        # Add each turn if needed
        if self.start_turn != self.end_turn:
            self.desc_each += "Each turn"

        # Set Card damage info
        if self.card_damage > 0:
            if self.card_target == "c":
                self.desc_card_damage += f"{self.card_damage} dmg to enemy card"
            elif self.card_target == "a": 
                self.desc_card_damage += f"{self.card_damage} dmg to all enemy cards"

        # Set Player damage info 
        if self.player_damage:
            if int(self.player_damage) > 0:
                self.desc_player_damage += f"{self.player_damage} dmg to enemy player"

        # Set Finale card damage 
        if self.finale_card_damage > 0:
            if self.finale_card_target == "c":
                self.desc_finale_card_damage += f"Fin: {self.finale_card_damage} to enemy card"
            elif self.finale_card_target == "a": 
                self.desc_finale_card_damage += f"Fin: {self.finale_card_damage} dmg to all enemy cards"

        # Set swap info 
        if self.swap_duration > 0:
            if self.swap_direction == "l":
                self.desc_swap += f"**Swap with left card**"
                self.desc_swap_duration += f"for {self.swap_duration} more turns"
            elif self.swap_direction == "r":
                self.desc_swap += f"**Swap with right card**"
                self.desc_swap_duration += f"for {self.swap_duration} more turns"

        def __str__(self):
            return f"{self.name} - PC:{self.placement_cost} / H:{self.health} / TTA:{self.turns_to_activate}" 
        
        

