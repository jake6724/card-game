from card import Card
from deck import Deck 
from player import Player
from hand import Hand
import copy
from helper_functions import shuffle_card_list, create_new_card

class Game_engine: 
    def __init__(self, card_data_file):
        self.deck = []
        self.card_data_file = card_data_file
        self.player_list = [Player("player1"), Player("player2")]
        self.player1 = self.player_list[0]
        self.player2 = self.player_list[1]

    def run_setup(self):
        self.assign_player_decks()
        self.assign_player_starting_hands()

    def gen_player_decks(self):
        print("Generating Deck")
        player1_deck = Deck() 
        player2_deck = Deck() 
        temp_card_list = []

        # TODO: Find every card with a value of <= 3, make a deepcopy and add to a new list. Combine this with the master list 

        # Create cards based off data in self.card_data_file 
        card_data = open(self.card_data_file, "r")
        for line in card_data:
            line_data_list = line.split() 
            new_card = create_new_card(line_data_list)
            temp_card_list.append(new_card)

        # Shuffle cards 
        shuffle_card_list(temp_card_list)

        # Assign decks to player (exact copies of each other same shuffling)
        player1_deck.add_card_list(temp_card_list)
        player2_deck.add_card_list(copy.deepcopy(temp_card_list))

        return [player1_deck, player2_deck]

    def assign_player_decks(self):    
        deck_list = self.gen_player_decks() 

        self.player1.add_deck(deck_list[0])
        self.player2.add_deck(deck_list[1])

        print("Player 1's deck:")
        self.player1.print_deck()

        print("Player 2's deck:")
        self.player1.print_deck()

    def assign_player_starting_hands(self): # Take top 3 cards off the top assign to player hands 

        # TODO: Improve adding card to hand so that the players deck gets updated with the new card order that has been created. 

        player1_hand = Hand()
        player2_hand = Hand()

        self.player1.add_hand(player1_hand)
        self.player2.add_hand(player2_hand)

        for i in range(4): 
            self.player1.draw_card()
            self.player2.draw_card()

        print("player 1's hand")
        self.player1.print_hand()
        print()
        print("player 2's hand")
        self.player2.print_hand()
            


