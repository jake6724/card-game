class Hand():
    def __init__(self):
        self.card_list = []

    def add_card_to_hand(self, new_card: list):
        self.card_list.append(new_card)

    def print_card_list(self):
        for card in self.card_list:
            print(card)