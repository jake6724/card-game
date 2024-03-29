from game_classes.card import Card
from game_classes.deck import Deck 
from game_classes.player import Player
from game_classes.gameboard import GameBoard
from game_classes.hand import Hand
import copy
import os
import time 
from helper_functions import shuffle_card_list, create_new_card, duplicate_cards, append_card_list, get_cards_by_mana

class Game_engine: 
    def __init__(self, card_data_file):
        self.deck = []
        self.card_data_file = card_data_file
        self.player_list = [Player("P1"), Player("P2")]
        self.player1 = self.player_list[0]
        self.player2 = self.player_list[1]
        self.hand_size = 4
        #self.gb = gb (down below)
        self.max_placement_cost_to_duplicate = 3
        self.current_player = self.player1
        self.round = 0 
        self.mana_per_turn = 0
        self.round_interval_to_increase_mana = 10
        self.max_mana_per_turn = 6
        self.winner = None
        self.loser = None

    def run_setup(self):
        self.assign_player_decks()
        self.assign_starting_hands()
        self.gen_gameboard_assign_player_lanes()

    def run_game_loop(self):
        while self.winner == None: 
            self.round += 1 

            self.deal_mana()
            
            self.placement_phase()

            self.combat_phase()

            self.cleanup_phase()

            if self.player1.is_dead:
                self.winner = self.player2
                self.loser = self.player1
                self.end_game()

            elif self.player2.is_dead:
                self.winner = self.player1
                self.loser = self.player2
                self.end_game()

    def gen_player_decks(self):
        # player1_deck = Deck() 
        # player2_deck = Deck() 
        temp_card_list = []

        # Create cards based off data in self.card_data_file 
        card_data = open(self.card_data_file, "r")
        for line in card_data:
            line_data_list = line.split() 
            new_card = create_new_card(line_data_list)
    
            temp_card_list.append(new_card)

        # Duplicate all cards with value <= self.max_placement_cost_to_duplicate
        duplicated_cards = duplicate_cards(temp_card_list)

        # Append duplicated cards to temp_card_list
        append_card_list(temp_card_list, duplicated_cards)

        # Shuffle cards 
        shuffle_card_list(temp_card_list)

        player1_deck = Deck(temp_card_list) 
        player2_deck = Deck(copy.deepcopy(temp_card_list)) 

        # Set player value for each card in player decks 
        for i in range(len(temp_card_list)):
            p1_card = player1_deck.get_card_by_number(i)
            p1_card.add_player(self.player1)

            p2_card = player2_deck.get_card_by_number(i)
            p2_card.add_player(self.player2)

        return [player1_deck, player2_deck]

    def assign_player_decks(self):    
        deck_list = self.gen_player_decks() 

        self.player1.add_deck(deck_list[0])
        self.player2.add_deck(deck_list[1])

    def gen_gameboard_assign_player_lanes(self):
        gb = GameBoard()
        self.gb = gb

        self.player1.add_lane_list(gb.lane_list[0:4])
        self.player2.add_lane_list(gb.lane_list[4:])

        # self.print_player_lanes()

    def deal_mana(self):
        self.player1.clear_mana()
        self.player2.clear_mana()

        self.determine_mana_amount()
        self.player1.add_mana(self.mana_per_turn)
        self.player2.add_mana(self.mana_per_turn)

    def assign_starting_hands(self):
        # Set up hand for player 1 
        one_mana_cards = get_cards_by_mana(self.player1.deck, 1, 3) 
        two_mana_cards = get_cards_by_mana(self.player1.deck, 2, 1) 
        p1_initial_hand = one_mana_cards + two_mana_cards

        # Set up hand for player 2
        one_mana_cards = get_cards_by_mana(self.player2.deck, 1, 3)  
        two_mana_cards = get_cards_by_mana(self.player2.deck, 2, 1) 
        p2_initial_hand = one_mana_cards + two_mana_cards

        # Assign starting hands 
        player1_hand = Hand(p1_initial_hand)
        player2_hand = Hand(p2_initial_hand)

        self.player1.add_hand(player1_hand)
        self.player2.add_hand(player2_hand)

    def draw_player_cards(self):
        # Remove the empty card if it exists currently. There is only 1 that is a placeholder for all empty spaces in the hand
        for i, card in enumerate(self.player1.hand.card_list[:]):
            if card.name == "empty":
                self.player1.hand.card_list.remove(card)

        for i, card in enumerate(self.player2.hand.card_list[:]):
            if card.name == "empty":
                self.player2.hand.card_list.remove(card)

        # Only draw cards for a player if they have enough to draw
        while len(self.player1.deck.card_list) > 0:
            if len(self.player1.hand.card_list) != self.hand_size:
                self.player1.draw_card()
            elif len(self.player1.hand.card_list) == self.hand_size:
                break

        while len(self.player2.deck.card_list) > 0:
            if len(self.player2.hand.card_list) != self.hand_size:
                self.player2.draw_card()
            elif len(self.player2.hand.card_list) == self.hand_size:
                break
        
    def placement_phase(self):
        # Draw cards back to full
        self.draw_player_cards()

        self.current_player = self.player1
        p1_cards_to_add = self.player_placement_phase()

        self.current_player = self.player2
        p2_cards_to_add = self.player_placement_phase()

        if len(p1_cards_to_add) != 0:
            for card in p1_cards_to_add:
                self.gb.add_to_active_cards(card)
                self.gb.add_card_to_lane(card)

        if len(p2_cards_to_add) != 0:
            for card in p2_cards_to_add:
                self.gb.add_to_active_cards(card)
                self.gb.add_card_to_lane(card)

    def player_placement_phase(self):
        if len(self.current_player.deck.card_list) != 0:
            self.display_game()
            card_options = ["1", "2", "3", "4"]
            card_priority_counter = 1
            cards_to_add = []
            option = ""

            # option = input("Enter card or (e)nd turn:")
            option = input("Enter card or ENTER to end turn:")

            # Get current player card placements 
            while option != "":
                # if self.current_player.is_card_in_hand(option):
                if option in card_options:
                    card = self.current_player.get_card_by_number(option)
                    print(f"Selected Card: {card}")
                    if self.current_player.has_enough_mana(card):
                        lane_option = input(f"Enter lane ({self.current_player.get_lane_list_string()}):")
                        if self.current_player.is_lane_valid(lane_option):
                            lane = self.current_player.get_lane_by_number(lane_option)
                            if self.current_player.is_lane_occupied(lane) == False:
                                # Update card priority
                                card.add_priority(self.round, card_priority_counter)
                                card_priority_counter += 1 

                                # Remove card from player hand 
                                self.current_player.remove_card_from_hand(card)

                                # Add lane number to card 
                                card.add_lane_number(lane.number)

                                # Remove player mana based on card mana cost 
                                self.current_player.remove_mana(card.mana)

                                # Add card to list to add to gameboard
                                cards_to_add.append(card)

                                # Redisplay board with updated player info
                                self.display_game()
                            else:
                                print("Lane occupied!")
                        else:
                            print("Invalid Lane!")
                    else:
                        print("Not enough mana!")
                else:
                    # print("You don't have this card!")
                    print("Invalid card number!")
                
                # option = input("Enter card or (e)nd turn:")
                option = input("Enter card or ENTER to end turn:")
        else: 
            # End the game if a player runs of cards 
            print(f"{self.current_player} is out of cards! They lose!")
            self.current_player.is_dead = True 
            if self.player1.is_dead:
                self.winner = self.player2
                self.loser = self.player1
                self.end_game()
                return []

            elif self.player2.is_dead:
                self.winner = self.player1
                self.loser = self.player2
                self.end_game()
                return []

        return cards_to_add

    def combat_phase(self):
        # Sort gb.active_card list based on card priority var
        self.gb.sort_active_cards()
        self.gb.reset_card_combat_logs()
        self.gb.reset_combat_log()

        # Main combat loop 
        # Get each card in sorted active cards list 
        for i, card in enumerate(self.gb.active_card_list):
            # Run its combat actions if alive 
            if card.is_dead == False:
                self.gb.run_card_combat_actions(card, self.player1, self.player2)
                card.increase_counter()
            
                # Check that current card is not the last card in list (index would go out of range)
                if i != (len(self.gb.active_card_list) - 1):
                    # Update GB if next card **DOES NOT** have the same priority as current card 
                    if self.gb.active_card_list[(i + 1)].priority != card.priority:
                        self.gb.update()
                # else: # Update if last card in the list (Also ensures board is always updated atleast once after a combat round)
                #     self.gb.update()
        self.gb.update()

    def cleanup_phase(self):
        # Remove all dead cards from gameboard
        # print(f"Start of cleanup phase: {self.gb.active_card_list}")
        for i, card in enumerate(self.gb.active_card_list[:]):
            if card.is_dead == True:
                self.gb.remove_active_card(card)
        # print(f"End of cleanup phase: {self.gb.active_card_list}")

    def end_game(self):
        print(f"{self.winner} is the winner! {self.loser} was killed by {self.loser.killed_by}")

    def add_cards_to_gameboard(self, player1_card_data_list, player2_card_data_list):
        # Add cards to gameboard 
        for i in range(4):
            self.gb.add_card_to_lane(player1_card_data_list[i][0], player1_card_data_list[i][1])
            self.gb.add_card_to_lane(player2_card_data_list[i][0], player2_card_data_list[i][1])

    def is_placement_data_all_null(self, data_to_check):
        for data in data_to_check:
            if data[0] != None: 
                return False 
        return True 
        
    def print_player_decks(self):
        self.player1.print_deck()
        self.player2.print_deck()

    def print_player_hands(self):
        print(f"{self.player1}'s Hand: {self.player1.hand.card_list}")
        print(f"{self.player2}'s Hand: {self.player2.hand.card_list}")

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

    def display_current_player_stats(self):
        print(f"Playing as {self.current_player}")
        print(f"Mana: {self.current_player.mana}")
        print(f"Health: {self.current_player.health}")

    def display_game(self):
        # self.clear_terminal()
        self.display_round_info()
        self.display_gameboard()
        self.display_current_player_hand()
        self.display_current_player_stats()

    def display_gameboard(self):
        if self.current_player == self.player1:
            self.gb.display_gameboard_p1()
        else: 
            self.gb.display_gameboard_p2()

        # self.gb.display_gameboard_p1()
           
    def display_round_info(self):
        if self.current_player == self.player1:
            opponent = self.player2
        else:
            opponent = self.player1

        print(f"                [ Round Number: {self.round}      Mana Per Turn: {self.mana_per_turn}      Opponent Health: {opponent.health}      Opponent Mana: {opponent.mana} ]")

    def determine_mana_amount(self):
        # # Check round number and determine how much mana should be dealt each round currently
        # if self.round % self.round_interval_to_increase_mana == 0:
        #     if self.mana_per_turn <= self.max_mana_per_turn: 
        #         self.mana_per_turn += 1 
        
        if self.round <= 6:
            self.mana_per_turn += 1

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def sleep_terminal(self, time_to_sleep):
        time.sleep(time_to_sleep)