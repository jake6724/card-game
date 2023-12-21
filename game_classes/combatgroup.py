from game_classes.card import Card

# Combat group defines group of cards which have the same ROUND attack priority, and then their own internal attack order 
# within the combat group. This is done in pairs of cards for each player. 
# Pairs CAN only have 1 card if 1 player did not play a matching one
class CombatGroup:
    def __init__(self):
        self.card_pair_list = []
    
    def add_card_pair(self, card1, card2):
        if card1 != None or card2 != None:
            self.card_pair_list.append([card1, card2])

    
