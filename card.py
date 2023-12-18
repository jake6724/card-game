class Card: 
    def __init__(self, name: str, placement_cost: int, health: int, turns_to_activate: int, pawn_target, pawn_damage: int, 
                 opponent_target: bool, opponent_damage: int, swap_target: str, each_turn_target, each_turn_damage ): 
        self.name = name
        self.placement_cost = placement_cost
        self.health = health
        self.turns_to_activate = turns_to_activate
        self.pawn_target = pawn_target
        self.pawn_damage = pawn_damage
        self.opponent_target = opponent_target
        self.opponent_damage = opponent_damage
        self.swap_target = swap_target
        self.each_turn_target = each_turn_target
        each_turn_damage = each_turn_damage

    def __str__(self):
        return f"{self.name} - PC:{self.placement_cost} / H:{self.health} / TTA:{self.turns_to_activate}" 