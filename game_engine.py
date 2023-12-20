from game_classes.card import Card
from game_classes.deck import Deck 
from game_classes.player import Player
from game_classes.gameboard import GameBoard
from game_classes.hand import Hand
import copy
import os
import time 
from helper_functions import shuffle_card_list, create_new_card, duplicate_cards, append_card_list

class Game_engine: 
    def __init__(self, card_data_file):
        self.deck = []
        self.card_data_file = card_data_file
        self.player_list = [Player("PLAYER 1"), Player("PLAYER 2")]
        self.player1 = self.player_list[0]
        self.player2 = self.player_list[1]
        self.hand_size = 4
        #self.gb = gb (down below)
        self.max_placement_cost_to_duplicate = 3
        self.current_player = self.player1
        self.round = 0 
        self.mana_per_turn = 1
        self.round_interval_to_increase_mana = 10
        self.max_mana_per_turn = 6
        self.winner = None

    def run_setup(self):
        self.assign_player_decks()
        self.assign_player_starting_hands()
        self.gen_gameboard_assign__player_lanes()

    def run_game_loop(self):
        # while self.winner == None: 
        self.round += 1 
        
        self.deal_mana()

        # Run display functions
        # self.display_round_info()

        # Run placement phase 
        self.placement_phase()

    def gen_player_decks(self):
        player1_deck = Deck() 
        player2_deck = Deck() 
        temp_card_list = []

        # Create cards based off data in self.card_data_file 
        card_data = open(self.card_data_file, "r")
        for line in card_data:
            line_data_list = line.split() 
            new_card = create_new_card(line_data_list)
    
            temp_card_list.append(new_card)
            # Have card create it's description here also
            new_card.create_description()
        
        # Duplicate all cards with value <= self.max_placement_cost_to_duplicate
        duplicated_cards = duplicate_cards(temp_card_list)

        # Append duplicated cards to temp_card_list
        append_card_list(temp_card_list, duplicated_cards)

        # Shuffle cards 
        shuffle_card_list(temp_card_list)

        # Assign decks to player (exact copies of each other w/ same shuffling)
        player1_deck.add_card_list(temp_card_list)
        player2_deck.add_card_list(copy.deepcopy(temp_card_list))

        return [player1_deck, player2_deck]

    def assign_player_decks(self):    
        deck_list = self.gen_player_decks() 

        self.player1.add_deck(deck_list[0])
        self.player2.add_deck(deck_list[1])
 
    def assign_player_starting_hands(self): 
        player1_hand = Hand()
        player2_hand = Hand()

        self.player1.add_hand(player1_hand)
        self.player2.add_hand(player2_hand)

        for i in range(self.hand_size): 
            self.player1.draw_card()
            self.player2.draw_card()

    def gen_gameboard_assign__player_lanes(self):
        gb = GameBoard()
        self.gb = gb

        self.player1.add_lane_list(gb.lane_list[0::2])
        self.player2.add_lane_list(gb.lane_list[1::2])

        # self.print_player_lanes()

    def deal_mana(self):
        self.determine_mana_amount()
        self.player1.add_mana(self.mana_per_turn)
        self.player2.add_mana(self.mana_per_turn)

    def placement_phase(self):
        # Create new combat round to store card placement order from this rounds placement phase 
        self.gb.create_new_combat_group()

        # Start as player 1 and display gameboard / player hand
        self.current_player = self.player1
        self.gb.display_gameboard()
        self.display_current_player_hand()

        # Card data per round 
        player1_card_data_list = []
        player2_card_data_list = []

        # Get player 1 card placements 
        option = input("(s)elect card or (e)nd turn:")
        print(f"SELECTED: {option}")
        while option != "e": 
            player1_card_data = self.player1.get_card_placement_data()
            player1_card_data_list.append(player1_card_data)
            option = input("(s)elect card or (e)nd turn:")

        # Switch to player 2 
        # Display gameboard and player 2 hand, no updates made from player 1's actions though
        self.current_player = self.player2
        self.gb.display_gameboard()
        self.display_current_player_hand()

        # Get player 2 card placements 
        option = input("(s)elect card or (e)nd turn:")
        print(f"SELECTED: {option}")
        while option != "e": 
            player2_card_data = self.player2.get_card_placement_data()
            player2_card_data_list.append(player2_card_data)
            option = input("(s)elect card or (e)nd turn:")

        # Make sure each player placement data pair list is 4 long (All added data will be None)
        for x in range(4):
            if len(player1_card_data_list) < 4:
                player1_card_data_list.append([None, None])
            if len(player2_card_data_list) < 4:
                player2_card_data_list.append([None, None])

        # print(f"Player 1 card data list: {player1_card_data_list}")
        # print(f"Player 2 card data list: {player2_card_data_list}")
        
        # # Add matching card pair to combat groups, based off data in each player_card_data_list
        for i in range(4):
            self.gb.add_card_to_combat_group(self.round, player1_card_data_list[i][0], player2_card_data_list[i][0])

        # Add cards to gameboard 
        for i in range(4):
            self.gb.add_card_to_lane(player1_card_data_list[i][0], player1_card_data_list[i][1])
            self.gb.add_card_to_lane(player2_card_data_list[i][0], player2_card_data_list[i][1])
        
        self.gb.display_gameboard()

    def print_player_decks(self):
        self.player1.print_deck()
        self.player2.print_deck()

    def print_player_hands(self):
        self.player1.print_hand()
        self.player2.print_hand()

    def print_player_lanes(self):
        self.player1.print_lane_list()
        self.player2.print_lane_list()

    def pretty_print_hands(self):
        self.player1.pretty_print_hand()
        self.player2.pretty_print_hand()
    
    def display_current_player_hand(self):
        self.current_player.display_hand()

    def display_current_player_lanes(self):
        self.current_player.print_lane_list()

    def display_round_info(self):
        # Display round, player health and mana, current mana dealt per turn 
        print(f"{self.player1.name} - HP: {self.player1.health} MP: {self.player1.mana}")
        print(f"{self.player2.name} - HP: {self.player2.health} MP: {self.player2.mana} ")
        print(f"Current mana per turn:{self.mana_per_turn}")
        print()
        print(f"{self.current_player.name}'s TURN")

    def determine_mana_amount(self):
        # Check round number and determine how much mana should be dealt each round currently
        if self.round % self.round_interval_to_increase_mana == 0:
            if self.mana_per_turn <= self.max_mana_per_turn: 
                self.mana_per_turn += 1 

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def sleep_terminal(self, time_to_sleep):
        time.sleep(time_to_sleep)
