class Hand():
    # Unlike deck hand starts with an empty card list. Use player -> draw_card func to add cards 
    def __init__(self):
        self.card_list = []

    def add_card_to_hand(self, new_card: list):
        self.card_list.append(new_card)

        if len(self.card_list) == 4:
            self.card1 = self.card_list[0]
            self.card2 = self.card_list[1]
            self.card3 = self.card_list[2]
            self.card4 = self.card_list[3]

    def get_card_by_name(self):
        # is_card_in_hand = False

        # Check that card exists in hand 
        # while is_card_in_hand == False:
        card_to_place_name = str(input("Select Card: "))
        for card in self.card_list:
            if card.name == card_to_place_name:
                is_card_in_hand = True 
                found_card = card
        if is_card_in_hand:
            return found_card
        else:
            print("Card not in hand!")
            return None 

    def print_card_list(self):
        for card in self.card_list:
            print(card)
