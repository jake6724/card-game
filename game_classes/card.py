import random

class Card: 
    def __init__(self, name: str, mana: int, health: int, start_turn: int, end_turn: int, repeat_card_target: str, repeat_card_damage: int, repeat_player_damage: int, repeat_swap_direction: str, repeat_swap_duration: int, finale_card_target: str, finale_card_damage: int, finale_player_damage: int, finale_swap_direction: str): 
        self.name = name.replace("_", " ")
        self.mana = int(mana) 
        self.health = int(health)
        self.start_turn = int(start_turn)
        self.end_turn = int(end_turn)
        self.repeat_card_target = str(repeat_card_target)
        self.repeat_card_damage = int(repeat_card_damage)
        self.repeat_player_damage = int(repeat_player_damage)
        self.repeat_swap_direction = str(repeat_swap_direction)
        self.repeat_swap_duration = int(repeat_swap_duration)
        self.finale_card_target = str(finale_card_target)
        self.finale_card_damage = int(finale_card_damage)
        self.finale_player_damage = int(finale_player_damage)
        self.finale_swap_direction = str(finale_swap_direction)

        self.player = None
        self.priority = None
        self.lane_num = None
        self.taken_turn = False
        self.counter = 0 

        self.log_swap = ""
        self.log_card = ""
        self.log_player = ""

        self.create_description()

    def create_description(self):                                         
        # Set up desc text vars 
        if self.name == "empty": # Make empty card desc invs. on gameboard 
            self.desc_mana = ""
            self.desc_health = ""
            self.desc_counter = ""
            self.desc_start_end = ""
        else:
            self.desc_mana = f"MP:{self.mana}"
            self.desc_health = f"HP:{self.health}"  
            self.desc_counter = f"Turns until Finale:{(self.end_turn - self.counter)}"
            self.desc_start_end = f"ST/ET: {self.start_turn}/{self.end_turn}"

        self.desc_each = ""
        self.desc_repeat_card_damage = ""
        self.desc_repeat_player_damage = "" 
        self.desc_repeat_swap = "" 

        self.desc_finale = ""
        self.desc_finale_card_damage = ""
        self.desc_finale_player_damage = "" 
        self.desc_finale_swap = ""

        # Check if each turn needed 
        if self.start_turn != self.end_turn:
            self.desc_each += "Each turn:"

        # Set repeat card damage info
        if self.repeat_card_damage > 0:
            if self.repeat_card_target == "c":
                self.desc_repeat_card_damage += f"{self.repeat_card_damage} dmg to enemy card"
            elif self.repeat_card_target == "a": 
                self.desc_repeat_card_damage += f"{self.repeat_card_damage} dmg to all enemy cards"

        # Set repeat player damage info 
        if self.repeat_player_damage > 0:
            self.desc_repeat_player_damage += f"{self.repeat_player_damage} dmg to enemy player"

        # Set repeat swap info 
        if self.repeat_swap_duration > 0:
            if self.repeat_swap_direction == "l":
                self.desc_repeat_swap += f"Swap Left"
            else:
                self.desc_repeat_swap += f"Swap Right"

        # Set finale line 
        if self.finale_card_damage > 0 or self.finale_player_damage > 0 or self.finale_swap_direction != "n":
            self.desc_finale += "Finale:"
        
        # Set Finale card damage 
        if self.finale_card_damage > 0:
            if self.finale_card_target == "c":
                self.desc_finale_card_damage += f"{self.finale_card_damage} dmg to enemy card"
            elif self.finale_card_target == "a": 
                self.desc_finale_card_damage += f"{self.finale_card_damage} dmg to all enemy cards"

        # Set Finale player damage 
        if self.finale_player_damage > 0:
            self.desc_finale_player_damage += f"{self.finale_player_damage} dmg to enemy player"
        
        # Set finale swap info 
        if self.finale_swap_direction != "n":
            if self.finale_swap_direction == "l":
                self.desc_finale_swap += f"Swap Left"
            else:
                self.desc_finale_swap += f"Swap Right"

    # def create_combat_log(self):
    #     self.log_repeat_card = ""
    #     self.log_repeat_player = ""
    #     self.log_repeat_swap = ""
    #     self.log_finale_card = ""
    #     self.log_finale_player = ""
    #     self.log_finale_swap = ""

    def take_damage(self, damage_amount):
        print(f"{self}: I took {damage_amount} dmg")
        self.health -= damage_amount

    def increase_counter(self):
        self.counter = self.counter + 1 
        print(f"{self.name} counter increased to {self.counter}")

    def add_priority(self, round_num, card_priority):
        p = str(round_num) + str(card_priority)
        self.priority = int(p)

    def add_player(self, player):
        self.player = player 
        
    def add_lane_number(self, l):
        self.lane_num = l 

    def __str__(self):
        return f"{self.player}:{self.name}" 
        
    def __repr__(self):
        return f"{self.player}:{self.name}:{self.priority}"